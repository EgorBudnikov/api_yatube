from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Пермишен для проверки авторства."""

    def has_object_permission(self, request, view, obj):
        author = obj.author
        methods = permissions.SAFE_METHODS
        return request.method in methods or request.user == author
