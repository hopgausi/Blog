from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Article(models.Model):
    title = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)
    content = RichTextField()
    pub_date = models.DateField(auto_now=True)
    publish = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("blog:home")
    
        
    
    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title
