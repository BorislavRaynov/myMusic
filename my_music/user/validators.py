from django.core.exceptions import ValidationError

def check_valid_username(value):
    for v in value:
        if not v.isdigit() and not v.isalpha() and not v == '_':
            raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')
