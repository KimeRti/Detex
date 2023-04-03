from django.db import models


class Messages(models.Model):
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=100)

    def __str__(self):
        return self.message
