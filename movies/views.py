from rest_framework import generics

from .models import Movie
from .serializers import MovieSerializer
from .permissions import IsAuthorOrReadOnly


class MovieList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthorOrReadOnly,)
