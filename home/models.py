from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    email   = models.CharField(max_length=192)
    mobile   = models.CharField(max_length=50)
    subject = models.CharField(max_length=192)
    message = models.TextField()
    created_at = models.DateField()

    def __str__(self) -> str:
        return self.name