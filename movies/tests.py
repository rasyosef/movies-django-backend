from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Movie


class MovieTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@user.com",
            password="checkcheck",
        )

        cls.movie = Movie.objects.create(
            title="Django Unchained",
            year_of_release=2012,
            description="With the help of a German bounty-hunter, a freed slave sets out to rescue his wife from a brutal plantation owner in Mississippi.",
            categories="Drama, Western",
            director="Quentin Tarantino",
            writers="Quentin Tarantino",
            image="https://m.media-amazon.com/images/M/MV5BMjIyNTQ5NjQ1OV5BMl5BanBnXkFtZTcwODg1MDU4OA@@._V1_FMjpg_UX1000_.jpg",
            created_by=cls.user,
        )

    def test_movie_model(self):
        self.assertEqual(self.movie.title, "Django Unchained")
        self.assertEqual(self.movie.year_of_release, 2012)
        self.assertEqual(
            self.movie.description,
            "With the help of a German bounty-hunter, a freed slave sets out to rescue his wife from a brutal plantation owner in Mississippi.",
        )
        self.assertEqual(self.movie.director, "Quentin Tarantino")
        self.assertEqual(str(self.movie), "Django Unchained")
