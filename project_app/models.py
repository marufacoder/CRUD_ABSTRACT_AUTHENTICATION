from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserModel(AbstractUser):
    student_name = models.CharField(max_length=200, null=True)
    student_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{ self.username}'


class ProjectModel(models.Model):
    STATUS = [
        ('NotStarted','NotStarted'),
        ('Inprogress','Inprogress'),
        ('Completed','Completed'),
    ]
    project_name= models.CharField(max_length=200, null=True)
    project_description = models.TextField(null=True)
    image = models.ImageField(upload_to='media/project_img', null=True)
    status = models.CharField(choices=STATUS, max_length=20, null=True)
    created_by = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=True
    )
    def __str__(self):
        return f'{self.project_name}'
    