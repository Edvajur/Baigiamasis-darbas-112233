from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View

from .models import Game, Developer, Publisher, Genre
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def index(request):
    game_list = Game.objects.all()
    paginator = Paginator(game_list, 3)  # Show 3 games per page
    page = request.GET.get('page')
    games = paginator.get_page(page)
    return render(request, 'library/index.html', {'page_obj': games})

def game_list(request):
    games = Game.objects.all()
    default_image_path = 'default.jpg'  # Adjust if your default image is located elsewhere.
    default_image_url = settings.MEDIA_URL + default_image_path
    return render(request, 'library/game_list.html', {'games': games, 'DEFAULT_IMAGE_URL': default_image_url})

def developer_list(request):
    developers = Developer.objects.all()  # Get all developers
    return render(request, 'library/developer_list.html', {'developers': developers})

def publisher_list(request):
    publishers = Publisher.objects.all()  # Get all publishers
    return render(request, 'library/publisher_list.html', {'publishers': publishers})

def genre_list(request):
    genres = Genre.objects.all()  # Get all genres
    return render(request, 'library/genre_list.html', {'genres': genres})

def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'library/game_detail.html', {'game': game})
def my_view(request):
    # Your logic here
    default_image_url = settings.MEDIA_URL + 'default.jpg'
    return render(request, 'my_template.html', {'DEFAULT_IMAGE_URL': default_image_url})

def search_view(request):
    query = request.GET.get('query')
    if query:
        # Perform search operation based on the query
        games = Game.objects.filter(title__icontains=query)
    else:
        games = Game.objects.all()
    return render(request, 'library/search_results.html', {'query': query, 'games': games})

# class MyView(LoginRequiredMixin, View):
#     login_url = '/login/'
#     redirect_field_name = 'redirect_to'
#
#     def get(self, request):
#         # Your logic here
#         default_image_url = settings.MEDIA_URL + 'default.jpg'
#         return render(request, 'my_template.html', {'DEFAULT_IMAGE_URL': default_image_url})




# def search_results(request):
#     query = request.GET.get('q', '')  # Get the query parameter 'q' from the URL
#
#     # Retrieve the objects based on the search query
#     games = Game.objects.filter(title__icontains=query) if query else []
#     developers = Developer.objects.filter(name__icontains=query) if query else []
#     publishers = Publisher.objects.filter(name__icontains=query) if query else []
#     genres = Genre.objects.filter(name__icontains=query) if query else []
#
#     return render(request, 'search_results.html', {
#         'query': query,
#         'games': games,
#         'developers': developers,
#         'publishers': publishers,
#         'genres': genres,
#     })