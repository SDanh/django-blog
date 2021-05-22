from django.contrib import admin
from blogging.models import Post, Category

class CategoryInline(admin.TabularInline):
    model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    fields = ('title', 'author', 'published_date', 'text')
    inlines = [CategoryInline,]
    pass

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)
    inlines = [CategoryInline,]
    pass

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)