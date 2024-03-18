from django.db import models

class Reminder(models.Model):
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    reminder_type = models.CharField(max_length=20)

    def __str__(self):
        return f'Reminder Message: {self.message}'
