from django.urls import include, path # noqa: F401
from rest_framework.routers import DefaultRouter

from .views import CommentAPIView, CommentListCreate, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path(
        'posts/<int:post_id>/comments/',
        CommentListCreate.as_view(),
        name='post-comment-list-create'
    ),
    path(
        'posts/<int:post_id>/comments/<int:comment_id>/',
        CommentAPIView.as_view(),
        name='comment-create-get-gelete-putch'
    ),
    path('', include(router.urls)),
]
