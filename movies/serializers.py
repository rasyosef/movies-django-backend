from rest_framework.serializers import ModelSerializer
from .models import Movie


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "year_of_release",
            "description",
            "categories",
            "director",
            "writers",
            "image",
            "created_at",
            "created_by",
        )
