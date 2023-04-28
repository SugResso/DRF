from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from films.models import Film


class FilmSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Film
        fields = "__all__"
