from django.urls import path
from user_app.views import *

urlpatterns = [
    path('list', UserList.as_view()),
    path('<int:pk>/', UserSingById.as_view()),
    path('insert', AddUser.as_view()),
    path('delete/<int:pk>', DelectUserById.as_view()),
    path('update/<int:pk>', UpdataUserById.as_view()),
]
