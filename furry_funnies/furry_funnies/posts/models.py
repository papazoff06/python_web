from django.core.validators import MinLengthValidator
from django.db import models

from furry_funnies.authors.models import Author


# Create your models here.
class Post(models.Model):
    title = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(5)],
        unique=True,
        error_messages={
            'unique': "Oops! That title is already taken. How about something fresh and fun?"
        }
    )
    image_url = models.URLField(
        help_text = "Share your funniest furry photo URL!"
    )
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
