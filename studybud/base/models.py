from django.db import models

# Create your models here.


class students(models.Model):
    student_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gpa = models.FloatField()
    email = models.EmailField()
    field_of_study = models.CharField(max_length=30)

    def __str__(self):
        return f"student: {self.first_name} {self.last_name}"
