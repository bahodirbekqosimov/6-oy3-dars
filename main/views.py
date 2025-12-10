from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, User, Category
from django.views import View
from django.core.handlers.wsgi import WSGIRequest


class HomeView(View):
    def get(self,req):
        articles = Article.objects.all().filter(is_active = True).order_by("-created_at")[:3]
        data = {
            "articles" : articles
        }
        return render(req,'main/index.html',context=data)
    

    
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
            return redirect("404")
            
            

      

class ArticlesView(View):
    def get(self,req):
        articles = Article.objects.all().filter(is_active = True).order_by("-created_at")[:6]
        categories = Category.objects.all().filter(is_active = True)

        
        data = {
            "articles" : articles,
            'categories':categories
        }
        
        return render(req,"main/articles.html",context=data)


class LoginView(View):
    def get(self,req):
        return render(req,"main/login.html")
    
    
class RegisterView(View):
    def get(self,req:WSGIRequest):
        if req.user.id:
            return redirect("home")
        return render(req,"main/register.html")
    
    
class ProfilView(View):
    def get(self,req:WSGIRequest,):
        id = req.user.id
        print(id)
        try:
            user = User.objects.get(id = id)
            posts = user.articles.all().filter(is_active = True).order_by("-created_at")
  
            data = {
                'user':user,
                'articles':posts,
                'posts':len(posts)
                
            
            }
            return render(req,"main/profile.html",context=data)
        except:
            if id is None:
                return render(req,"main/login.html")
            return redirect("404")
        
        
class UserView(View):
    def get(self,req:WSGIRequest,username):
        try:
            user = User.objects.get(id = req.user.id)
            if user.username == username:
                return redirect('profile')
        except:
            pass
        try:
            user = User.objects.get(username = username)

            posts = user.articles.all().filter(is_active = True).order_by("-created_at")
            data = {
                'user':user,
                'articles':posts,
                'posts':len(posts)
            }
            return render(req,"main/user.html",context=data)
        except:

            return redirect("404")
        
        
def Error404(req:WSGIRequest):
    return render(req,"main/404.html")
    



class DeleteArticleView(View):
    def get(self,req,id):
        try:
            article = Article.objects.get(id=id, is_active=True)

  
            data = {
                'article':article,
                "title": article.title
            }
            return render(req,"main/delete.html",context=data)
        except:
            return redirect("404")
    
    def post(self,req:WSGIRequest,id):
        try:
            article = Article.objects.get(id=id)
            
            if article.user.id == req.user.id:
                article.is_active =False
            
            article.save()
            return redirect("profile")
        except:
            return redirect("profile")
            
    
           
           
class AddView(View):
    def get(self,req:WSGIRequest):
        if not req.user.id:
            return redirect("profile")
        
        categories = Category.objects.all().filter(is_active = True)
        data = {"categories":categories}
        return render(req,"main/add.html" ,context=data)
    
    def post(self,req:WSGIRequest):
        if not req.user.id:
            return redirect("404")
        
        title = req.POST.get("title")
        info = req.POST.get("info")
        description = req.POST.get("description")
        category_id = req.POST.get("category")
        image = req.FILES.get("image")
        user_id = req.user.id
        
        
     
        Article.objects.create(
            title=title,
            info=info,
            image=image,
            category = Category.objects.get(id=category_id),
            user = User.objects.get(id=user_id),
            description=description
        )
        return redirect("profile")
        
        
        
        
        
class EditPosts(View):
    def get(self,req:WSGIRequest,id):
         
        try:
            article = Article.objects.get(id = id)
            if not req.user.id == article.user.id:
                return redirect("profile")
            
            categories = Category.objects.all().filter(is_active = True)
            

            data = {
                'article':article,
                "title": article.title,
                "categories":categories
            }
            return render(req,"main/edit_post.html",context=data)
        except:
            return redirect("404")
        
    def post(self,req:WSGIRequest,id):
        try:
            article = Article.objects.get(id = id)
            if not req.user.id == article.user.id:
                return redirect("profile")
            
            title = req.POST.get("title")
            info = req.POST.get("info")
            description = req.POST.get("description")
            category_id = req.POST.get("category")
            image = req.FILES.get("image")
            
            if title:
                article.title = title
            if info:
                article.info = info    
            if description:
                article.description = description
            if category_id:
                article.category = Category.objects.get(id = category_id)
            if image:
                article.image = image
                
            article.save()
            
            return redirect("detail",id)           
            
                
        except:
            redirect( "profile")
            
            
        
    
        
        
class EditProfile(View):
    def get(self,req:WSGIRequest):
        try:
            user = User.objects.get(id = req.user.id)
            data = {"user":user}
            return render(req, "main/edit_profile.html", context=data)
        except:
            return redirect("profile")
         
        
        
# from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

from random import randint


from environs import Env

env = Env()
env.read_env()
from .message import message
print("EMAIL_USER =", env.str("EMAIL_USER"))
print("EMAIL_PASS =", env.str("EMAIL_PASS"))

def test_email(request:WSGIRequest):
    random = randint(100000, 999999)
        
    user = User.objects.get(id = request.user.id)
    data = message(user,random)

    send_mail(
        subject="Verification password",
        message=f"<h1>{random}</h1>",
        from_email=None,
        recipient_list=[user.email,],
        fail_silently=False,
        html_message=f"{data}"
    )
    # except:
    #     return HttpResponse("xato")
        
    
    return HttpResponse(f"{user.email} ga yuborildi ✅")
