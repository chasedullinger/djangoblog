from django.urls import path
from blogging.views import stub_view, list_view, detail_view, form_view

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/form', form_view, name="blog_form"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
]
