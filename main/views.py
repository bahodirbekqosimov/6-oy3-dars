from django.shortcuts import render, get_object_or_404
from .models import Article
from django.views import View



class HomeView(View):
    def get(self,req):
        articles = Article.objects.all().filter(is_active = True).order_by("-created_at")[:3]
        data = {
            "articles" : articles
        }
        return render(req,'main/index.html',context=data)
    


# def home(req):
#     articles = Article.objects.all().filter(is_active = True).order_by("-created_at")[:3]
#     data = {
#         "articles" : articles
#     }

    
#     return render(req,'main/index.html',context=data)
class DetatilView(View):
    def get(self,req,id):
        try:
            article = Article.objects.get(id = id)
  
            data = {
                'article':article,
                "title": article.title
            }
            return render(req,"main/detail.html",context=data)
        except:
            return render(req,"main/404.html")
            
            

# def detail(req,id):
#     article = Article.objects.get(id = id)
#     if article:
#         data = {
#             'article':article
#         }
#     else:
#         data = {
#             'article':False
#         }
    
#     return render(req,"main/detail.html",context=data)
        
        

class ArticlesView(View):
    def get(self,req):
        articles = Article.objects.all().filter(is_active = True).order_by("-created_at")[:6]

        
        data = {
            "articles" : articles
        }
        
        return render(req,"main/articles.html",context=data)


class LoginView(View):
    def get(self,req):
        return render(req,"main/login.html")
    
    
class RegisterView(View):
    def get(self,req):
        return render(req,"main/register.html")