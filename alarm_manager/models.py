from django.db import models


# Create your models here.
class Alarm(models.Model):
    timestamp = models.DateTimeField(
        auto_now_add=True
    )
