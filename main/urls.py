
from django.urls import path
from .views import HomeView, DetatilView,ArticlesView,LoginView,RegisterView

urlpatterns = [
    
    path('',HomeView.as_view(), name='home'),
    path("detail/<int:id>/",DetatilView.as_view(),name="detail"),
    path("articles/",ArticlesView.as_view(),name="articles" ),
    path('login/',LoginView.as_view(),name="login"),
    path('register/',RegisterView.as_view(),name="register"),
    
]
