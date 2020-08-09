from django.db import models
from .validators import validate_code


# Create your models here.

class Code(models.Model):
    name = models.CharField(
        verbose_name="Name",
        max_length=250,
        null=True
    )

    code = models.PositiveIntegerField(
        verbose_name="Code",
        unique=True,
        validators=[validate_code]
    )

    last_used = models.DateTimeField(
        blank=True,
        null=True
    )

    ALLOWED_CHOICES = [
        ("always", "Immer"),
        ("alarm", "Nach Alarm")
    ]

    allowed = models.CharField(
        verbose_name="Erlaubt",
        max_length=100,
        choices=ALLOWED_CHOICES,
        default=ALLOWED_CHOICES[0][0]
    )

    valid_after_alarm = models.PositiveIntegerField(
        verbose_name="Gültig x Min nach Alarm",
        default=10,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        permissions = [
            ('check_code', 'Kann Code prüfen')
        ]
