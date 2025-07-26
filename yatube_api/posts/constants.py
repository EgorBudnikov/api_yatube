from http.client import FORBIDDEN
from rest_framework import status

FORBIDDEN_403 = status.HTTP_403_FORBIDDEN
COMMENT_NOT_AUTHOR = {'detail': 'Вы не автор этого комментария.'}
POST_NOT_AUTHOR = {"detail": "Вы не автор этого поста."}