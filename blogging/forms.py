from django.forms import ModelForm
from blogging.models import Post


class BlogForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title",
                  "text",
                  "author",
                  ]
