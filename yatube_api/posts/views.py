from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.serializers import CommentSerializer, GroupSerializer, PostSerializer
from api.permissions import IsAuthorOrReadOnly
from posts.models import Group, Post


def get_post(pk):
    return get_object_or_404(Post, pk=pk)


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для получения,редактирования, удаления поста/постов."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        """При создании поста автор устанавливается автоматически."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет только для чтения групп."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для получения и создания новых комментариев к посту."""

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        """Получение комментариев к посту."""
        post = get_post(self.kwargs.get('post_id'))
        queryset = post.comments.all()
        return queryset

    def perform_create(self, serializer):
        """При создании комментария автор устанавливается автоматически."""
        post = get_post(self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)
