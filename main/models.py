from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname


class Article(models.Model):
    title = models.CharField(max_length=150)
    info = models.CharField(max_length=100)
    image = models.FileField(upload_to="image/")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="articles")
    author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name="articles")
    description = models.TextField(max_length=5000)
    is_active = models.BooleanField(default=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
