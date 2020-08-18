from rest_framework import viewsets, generics
from .serializers import RecipeSerializer
from .models import Recipe
from rest_framework import filters

class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]