from django.contrib import admin
from .models import post


@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'datetime_modified', 'image')


# admin.site.register(post, PostAdmin)
