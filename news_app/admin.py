from django.contrib import admin
from django.contrib import admin
from news_app.models import Author, NewsCategory,NewsArticle

class AuthorAdmin(admin.ModelAdmin):
    pass

class NewsCategoryAdmin(admin.ModelAdmin):
    pass

class NewsArticleAdmin(admin.ModelAdmin):
    pass
admin.site.register(Author, AuthorAdmin)
admin.site.register(NewsCategory, NewsCategoryAdmin)
admin.site.register(NewsArticle, NewsArticleAdmin)


