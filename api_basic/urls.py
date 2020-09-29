from django.contrib import admin
from django.urls import path
from api_basic.views import *
from .views import *

urlpatterns = [
    # path('article/', article_list ),
    path('', apiOverview, name='api-oveview'),
    path('task-list/', ArticleAPIView.as_view()),
    path('task-man/', GenericAPIView.as_view()),
    path('task-detail/<int:pk>/', article_detail ),
    # path('detail/<int:pk>/', ArticleDetailAPIView.as_view() ),
]