from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_code(value):
    if value > 999999999:
        raise ValidationError(
            _('%(value)s is to long'),
            params={'value': value},
        )
