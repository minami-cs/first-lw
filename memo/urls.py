from django.urls import path
from .views import index, second, create, new, detail, update, delete, create_comment
urlpatterns = [
    # memo/라고 요청이 들어오면 여기 urls.py로 오게되고 memo/second요청이 오면 얘가 실행됩니다.
    path('second/', second, name="second"),
    path('create/', create, name="create"),
    path('new/', new, name="new"),
    path('detail/<int:detail_id>', detail, name="detail"),
    path('update/<int:update_id>', update, name="update"),
    path('delete/<int:delete_id>', delete, name="delete"),
    path('create_comment/<int:memo_id>', create_comment, name="create_comment"),
]