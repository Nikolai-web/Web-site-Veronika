from django.contrib import admin
from .models import Bd, Rubric

admin.site.register(Rubric)
@admin.register(Bd)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'price', 'published_time', 'rubric', 'status']
    search_fields = ['title', 'content']

