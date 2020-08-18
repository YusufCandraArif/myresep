from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)


urlpatterns = [
    path("", include(router.urls))
]

# endpoint search
# http://127.0.0.1:8000/api/recipes/?search=sate