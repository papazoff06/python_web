from django.core.exceptions import ValidationError


def validate_name(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError("Your name must contain letters only!")

def validate_passcode(value):
    if len(value) != 6:
        raise ValidationError("Your passcode must be exactly 6 digits")