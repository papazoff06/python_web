# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from furry_funnies.utils import get_author_obj


def index(request):
    profile = get_author_obj()
    context = {
        'profile': profile,
    }
    return render(request, 'common/index.html', context)

def dashboard(request):
    return render(request, 'common/dashboard.html')
