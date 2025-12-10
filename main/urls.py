
from django.urls import path
from .views import HomeView, DetatilView,ArticlesView,LoginView,RegisterView,ProfilView,UserView,DeleteArticleView,AddView,Error404,EditPosts,EditProfile

urlpatterns = [
    
    path('',HomeView.as_view(), name='home'),
    path("detail/<int:id>/",DetatilView.as_view(),name="detail"),
    path("posts/",ArticlesView.as_view(),name="articles" ),
    path('login/',LoginView.as_view(),name="login"),
    path('register/',RegisterView.as_view(),name="register"),
    path('profile/',ProfilView.as_view(),name="profile"),
    path('user/<str:username>/',UserView.as_view(),name="user"),
    path('delete/<int:id>/',DeleteArticleView.as_view(),name='delete'),
    path('add-post/',AddView.as_view(),name='add'),
    path('edit-post/<int:id>/',EditPosts.as_view(),name='edit'),
    path('edit/my-profile/',EditProfile.as_view(),name="editprofile"),
    
    
    
    path('404/',Error404,name='404')
    
    
    
    
    
    
]
