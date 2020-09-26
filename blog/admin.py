from django.contrib import admin
from . import models


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.Article,admin_class=ArticleAdmin)