from django.db import models

class Complaint(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
