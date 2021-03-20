from django.contrib import admin

# Register your models here.
from blogging.models import Post, Category

admin.site.register(Post)
admin.site.register(Category)


class CategoryInLine(admin.TabularInline):
    model = Category


class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = [CategoryInLine, ]
