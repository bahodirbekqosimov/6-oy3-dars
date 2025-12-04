
from django.urls import path
from .views import HomeView, DetatilView

urlpatterns = [
    
    path('',HomeView.as_view(), name='home'),
    path("detail/<int:id>/",DetatilView.as_view(),name="detail")
    
]
