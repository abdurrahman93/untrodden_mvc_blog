from django.contrib import admin
from posts.models import Posts, Comments


class PostsAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "created_at", "updated_at")


class CommentsAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_at", "updated_at")


admin.site.register(Posts, PostsAdmin)
admin.site.register(Comments, CommentsAdmin)
