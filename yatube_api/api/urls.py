from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

from posts.views import CommentViewSet, PostViewSet, GroupViewSet

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet, basename='v1-posts')
router_v1.register('groups', GroupViewSet, basename='v1-groups')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='v1-comments'
)

urlpatterns = [
    re_path('^', include(router_v1.urls))
]
