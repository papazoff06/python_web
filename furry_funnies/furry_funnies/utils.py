from furry_funnies.authors.models import Author
from furry_funnies.posts.models import Post


def get_author_obj():
    return Author.objects.first()

def get_post_obj():
    return Post.objects.all()