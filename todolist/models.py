from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=10, unique=True)

    class Meta:
        db_table = 'tag'  # Link this model to the existing tag table
        managed = False

    def __str__(self):
        return self.tag_name

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_detail = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE, db_column='tag_id')  # Reference to tag table
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')  # Reference to auth_user table
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'task'  # Link this model to the existing task table
        managed = False

    def __str__(self):
        return self.task_detail
