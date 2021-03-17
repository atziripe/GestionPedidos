from django.contrib import admin
from .models import Categorias, Post

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Categorias, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
