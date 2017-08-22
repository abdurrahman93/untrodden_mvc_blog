from django import forms
from posts.models import Posts, Comments


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = [
            "title",
            "content",
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = [
            "content",
        ]