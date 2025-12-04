from django.shortcuts import render
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
        article = Article.objects.get(id = id)
        if article:
            data = {
                'article':article
            }
        else:
            data = {
                'article':False
            }
        
        return render(req,"main/detail.html",context=data)
            
            

def detail(req,id):
    article = Article.objects.get(id = id)
    if article:
        data = {
            'article':article
        }
    else:
        data = {
            'article':False
        }
    
    return render(req,"main/detail.html",context=data)
        