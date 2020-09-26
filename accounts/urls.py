from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('profile/<int:pk>/update/', views.profile_update, name='profile_update'),
    path('register/', views.register, name="register")
]
