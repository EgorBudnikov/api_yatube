from django.shortcuts import get_object_or_404

from posts.models import Post


def get_post(pk):
    return get_object_or_404(Post, pk=pk)
