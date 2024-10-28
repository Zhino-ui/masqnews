from django.db import models

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, null=False)

    def __str__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles')
    content = models.TextField()
    writer = models.CharField(max_length=255)  # Or you could use a ForeignKey to a User/Author model
    writer_image = models.ImageField(upload_to='images/', default='images/images_4.jpg')
    is_featured = models.BooleanField(default=False)
    is_latest = models.BooleanField(default=False)
    is_banner = models.BooleanField(default=False)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Banner(models.Model):
    alt = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    is_home_banner_top = models.BooleanField(default=False)
    is_home_banner_center = models.BooleanField(default=False)
    is_home_banner_bottom = models.BooleanField(default=False)
    is_category_banner = models.BooleanField(default=False)
    is_side_banner = models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.alt
