from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from my_music_app.profiles.validators import username_validator


# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        max_length=145,
        validators=[
            MinLengthValidator(2),
            username_validator
        ]
    )

    email = models.EmailField()
    age = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0)])

