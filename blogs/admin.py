from django.contrib import admin
from .models import Category, Blogs, Comment

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'Category_name', 'created_at', 'updated_at')

class BlogAdmin(admin.ModelAdmin):
    list_display  = ('id','title','Category','author','blog_image','status','is_feachered','created_at','updated_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('id', 'title', 'Category__Category_name', 'status')
    list_editable = ('is_feachered',)



admin.site.register(Category,CategoryAdmin)
admin.site.register(Blogs,BlogAdmin)
admin.site.register(Comment)
