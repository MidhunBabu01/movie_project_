from django.http.response import JsonResponse
from django.shortcuts import render
from movie_app.models import MovieDetailss
from django.db.models import Q

# Create your views here.

def search(request):
    movielist = None
    query = None
    if "q" in request.GET:
        query = request.GET.get('q')
        movielist = MovieDetailss.objects.all().filter(Q(moviename__icontains=query))
    return render(request,'SearchResult.html', {'query':query,'movielist':movielist})