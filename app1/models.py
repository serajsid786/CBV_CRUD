from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    mobile=models.CharField(max_length=10)
    email=models.EmailField()

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return self.first_name
    