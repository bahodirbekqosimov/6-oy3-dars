from django.contrib import admin
from .models import Article, Author, Category


@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    list_display = ['fullname',"username",'email']
    ordering = ('created_at',)
    
    
@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display = ['title', 'category','author',"is_active"]
    list_filter = ("category",'author',"is_active")
    ordering = ("created_at",)
    

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name','is_active']
    list_filter = ("is_active",)

    