
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