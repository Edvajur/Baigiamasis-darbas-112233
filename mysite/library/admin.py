from django.contrib import admin
from .models import Game, Developer, Publisher, Genre

# Register your models here.

class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'developer', 'publisher')
    list_filter = ('developer', 'publisher', 'genre')
    search_fields = ('title', 'developer__name', 'publisher__name')
    filter_horizontal = ('genre',)  # Use for ManyToMany fields

# Register your models and admin classes
admin.site.register(Game, GameAdmin)
admin.site.register(Developer)
admin.site.register(Publisher)
admin.site.register(Genre)