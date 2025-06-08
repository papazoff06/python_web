
from my_music_app.profiles.models import Profile


def get_user_obj():
    return Profile.objects.first()