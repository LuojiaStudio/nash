from django.contrib import admin
from news_management.models import UncheckedArticle, CheckedArticle, Tag
# Register your models here.

admin.site.register(UncheckedArticle)
admin.site.register(CheckedArticle)
admin.site.register(Tag)
