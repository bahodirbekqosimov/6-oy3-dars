from django.contrib import admin
from .models import Article, User, Category


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ['fullname',"username",'email']
    ordering = ('created_at',)
    
    
@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display = ['title', 'category','user',"is_active"]
    list_filter = ("category",'user',"is_active")
    ordering = ("created_at",)
    

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name','is_active']
    list_filter = ("is_active",)

    