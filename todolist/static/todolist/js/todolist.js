
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('.task-list-panel').addEventListener('change', function(e) {
        if (e.target.classList.contains('custom-checkbox')) {
            const checkbox = e.target;
            // Correct ID parsing from checkbox element
            const taskId = checkbox.id.split('-')[1]; // Changed from [1] to [2]
           
            const taskElement = document.getElementById(`task-item-${taskId}`);
            // Validate task ID
            if (!taskId || isNaN(taskId)) {
                console.error('Invalid task ID:', taskId);
                checkbox.checked = false;
                return;
            }

            fetch(`/task_complete/${taskId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ is_done: true })
            })
            .then(response => {
                if (!response.ok) throw new Error('Network response was not ok');
                return response.json();
            })
            .then(data => {
                if (data.status === 'success') {
                    taskElement.style.opacity = '0';
                    setTimeout(() => taskElement.remove(), 500);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                checkbox.checked = false;
                alert('Failed to update task status');
            });
        }
    });

// AJAX to add new task
document.getElementById('task-form').addEventListener('submit', function(e) {
    // console.log('form sumitted')
    e.preventDefault();
    const form = e.target;
    const formData = new FormData(form);
    
    fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': '{{ csrf_token }}'
        }
    })
    .then(response => response.json())
    .then(data => {
        // console.log('response data:', data)
        if (data.status === 'success') {
            // Add new task to list
            const taskListPanel = document.querySelector('.task-list-panel');
        
        // Check if "No tasks found" message exists and remove it
        const noTasksMessage = taskListPanel.querySelector('.list-group-item:only-child');
        if (noTasksMessage && noTasksMessage.textContent.trim() === 'No tasks found.') {
            noTasksMessage.remove();
        }
    
        // console.log("Task data :", data.task)
        // Create the new task HTML
        const taskHTML = `
            <li class="list-group-item p-0" id="task-item-${data.task.task_id}">
                <div class="d-flex justify-content-between align-items-center">
                    <div class="d-flex justify-content-between align-items-center">
                        <div class="mb-0 border-end border-2 p-2">
                            <input
                                type="checkbox"
                                class="form-check-input custom-checkbox"
                                id="task-${data.task.task_id}"
                                ${data.task.is_done ? 'checked' : ''}
                                aria-label="Mark task ${data.task.task_id} as done"
                                data-bs-toggle="tooltip" 
                                data-bs-title="Check to remove"
                            >
                        </div>
                        <div class="me-2">
                            <p class="ms-3 mb-0 task-text">${data.task.task_detail}</p>
                        </div>
                    </div>
                    <div class="pe-3">
                        ${data.task.tag ? `<span class="badge bg-secondary">${data.task.tag.tag_name}</span>` : ''}
                    </div>
                </div>
            </li>
        `;
        
        // Add the new task to the task list
        taskListPanel.insertAdjacentHTML('beforeend', taskHTML);
            
            // Reset form
            form.reset();
            document.querySelector('.error-message').textContent = '';
        } else {
            // Show validation errors
            const errors = JSON.parse(data.errors);
            let errorText = '';
            for (const field in errors) {
                errorText += errors[field][0].message + '\n';
            }
            document.querySelector('.error-message').textContent = errorText;
        }
    })
    .catch(error => console.error('Error:', error));
});




    // CSRF token helper function remains the same
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});