from django.contrib import admin
from .models import post


@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'outher', 'status', 'datetime_modified')


# admin.site.register(post, PostAdmin)
