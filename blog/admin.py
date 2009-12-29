from django.contrib import admin
from blog.models import *

class CategoryAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    exclude = ('created',)

    class Media:
        pass

class TagPostAdmin(admin.ModelAdmin):
    list_display = ('tag', 'post')

class BlogRollAdmin(admin.ModelAdmin):
    exclude = ('created',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(TagPost, TagPostAdmin)
admin.site.register(BlogRoll, BlogRollAdmin)
