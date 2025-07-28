from rest_framework import status

COMMENT_NOT_AUTHOR = {'detail': 'Вы не автор этого комментария.'}
COUNT_TEXT_MODEL = 20
FORBIDDEN_403 = status.HTTP_403_FORBIDDEN
POST_NOT_AUTHOR = {"detail": "Вы не автор этого поста."}
