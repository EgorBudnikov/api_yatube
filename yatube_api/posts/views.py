from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.response import Response

from api.serializers import CommentSerializer, GroupSerializer, PostSerializer
from .constants import COMMENT_NOT_AUTHOR, FORBIDDEN_403, POST_NOT_AUTHOR
from .models import Comment, Group, Post


class PostViewSet(viewsets.ModelViewSet):
    """Вьсет для получения,редактирования, удаления поста/постов."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def update(self, request, *args, **kwargs):
        """PUT, PATCH обновление."""
        instance = self.get_object()
        if instance.author != request.user:
            return Response(
                POST_NOT_AUTHOR,
                status=FORBIDDEN_403
            )
        return super().update(request, *args, **kwargs)

    def perform_create(self, serializer):
        """При создании поста автор устанавливается автоматически."""
        serializer.save(author=self.request.user)

    def destroy(self, request, *args, **kwargs):
        """Удаление поста."""
        instance = self.get_object()
        if instance.author != request.user:
            return Response(
                POST_NOT_AUTHOR,
                status=FORBIDDEN_403
            )
        return super().destroy(request, *args, **kwargs)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет только для чтения групп."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentListCreate(generics.ListCreateAPIView):
    """Дженерик для получения и создания новых комментариев к посту."""
    serializer_class = CommentSerializer

    def get_queryset(self):
        """Получение комментариев к посту."""
        post = self.kwargs['post_id']
        queryset = Comment.objects.filter(post=post)
        return queryset

    def perform_create(self, serializer):
        """При создании комментария автор устанавливается автоматически."""
        post = Post.objects.get(id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class CommentAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Дженерик для получения, удаления, изменения комментария к посту."""
    serializer_class = CommentSerializer

    def get_object(self):
        """Получение конкретного комментария."""
        post_id = self.kwargs['post_id']
        comment_id = self.kwargs['comment_id']
        queryset = get_object_or_404(
            Comment.objects.filter(post=post_id),
            id=comment_id
        )
        return queryset

    def update(self, request, *args, **kwargs):
        """PUT, PATCH обновление."""
        instance = self.get_object()
        if instance.author != request.user:
            return Response(
                COMMENT_NOT_AUTHOR,
                status=FORBIDDEN_403
            )
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Удаление комментария."""
        instance = self.get_object()
        if instance.author != request.user:
            return Response(
                COMMENT_NOT_AUTHOR,
                status=FORBIDDEN_403
            )
        return super().destroy(request, *args, **kwargs)
