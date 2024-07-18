from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class MinimalPasswordValidator:
    def validate(self, password, user=None):
        if len(password) < 8:
            raise ValidationError(
                _("Password must contain at least 8 characters."),
                code='password_too_short',
            )
    
    def get_help_text(self):
        return _("Your password must contain at least 8 characters.")
