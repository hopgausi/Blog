from django.urls import path
from  . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('post/<int:pk>/<slug:slug>/', views.ArticleDetailView.as_view(), name='detail'),
   # path('post/create/', views.BlogCreateView.as_view(), name='create'),
    path('post/create/', views.create_post, name='create'),
    path('post/<int:pk>/<slug:slug>/update/', views.PostUpdateView.as_view(), name='update'),
    path('post/<int:pk>/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='delete'),
]
