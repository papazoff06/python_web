from django.utils.text import slugify


def username_validator(value):
    if not(value.isalnum() or value == '_'):
        raise ValueError('Ensure this value contains only letters, numbers, and underscore.')

