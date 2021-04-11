from django.db import models

class Student(models.Model):
    gender_choices = (
        ('male', "男"),
        ('female', "女"),
    )
    student_id = models.CharField(max_length=8,unique=True)
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=256)
    gender = models.CharField(max_length=32, choices=gender_choices)
    age = models.IntegerField(null=True)
    department = models.CharField(max_length=32,null=True)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"





