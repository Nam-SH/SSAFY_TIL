from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)
    list_filter = ('created_at',)
    list_display_links = ('content',)
    list_editable = ('title',)
    list_per_page = 4


admin.site.register(Article, ArticleAdmin)