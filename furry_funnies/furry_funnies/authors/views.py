from django.urls import reverse_lazy
from django.views.generic import CreateView

from furry_funnies.authors.forms import CreateAuthorForm
from furry_funnies.authors.models import Author
from furry_funnies.utils import get_author_obj


# Create your views here.
class AuthorCreate(CreateView):
    model = Author
    form_class = CreateAuthorForm
    template_name = 'authors/create-author.html'
    success_url = reverse_lazy('dashboard')
    def form_valid(self, form):
        form.instance.owner = get_author_obj()
        return super().form_valid(form)


def author_details_page(request):
    return None

def author_edit_page(request):
    return None

def author_delete_page(request):
    return None