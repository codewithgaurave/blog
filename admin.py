from django.contrib import admin
from .models import Category, Post



# for configuration of category admin.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description','url','add_date')
    search_fields = ('title',)


# for configuration of post

class PostAdmin(admin.ModelAdmin):
    list_display = ('image_post','post_id','title','content','url','cat')
    list_filter = ('cat',)
    search_fields = ('title',)
    list_per_page = 50

    class Media:
        js=('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js' , 'js/script.js',)


# Register your models here.


admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)


