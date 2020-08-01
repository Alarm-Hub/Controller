from django.db import models
from .validators import validate_code


# Create your models here.

class Code(models.Model):
    code = models.PositiveIntegerField(
        verbose_name="Code",
        unique=True,
        validators=[validate_code]
    )

    def __str__(self):
        return self.code.__str__()
