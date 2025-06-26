from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer
from django.shortcuts import render

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

def movie_list_html(request):
    movies = Movie.objects.all()
    thedict = {'movies': movies}
    return render(request, 'app2/movie_list.html',context = thedict)
    

