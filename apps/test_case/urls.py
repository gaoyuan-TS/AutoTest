from django.urls import path

from test_case.views import *
from user_app.views import *

urlpatterns = [
    path('list', TestCaseList.as_view()),
    path('insert',TestCaseAdd.as_view()),
    path('<int:pk>/', TestDetailById.as_view()),
    path('runner', TestRunner.as_view()),


]
