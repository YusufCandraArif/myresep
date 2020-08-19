from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, RegisterAPI, LoginAPI
from knox import views as knox_views

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)
# router.register(r'register', RegisterAPI, basename='register')


urlpatterns = [
    path("", include(router.urls)),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]

# endpoint search
# http://127.0.0.1:8000/api/recipes/?search=sate