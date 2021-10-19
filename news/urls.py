from django.urls import path
# from .views import (article_list_create_api_view, article_detail)
from .views import (ArticleDetailAPIView, ArticleListCreateAPIView, JournalistListCreateAPIView)

urlpatterns = [
    # path('articles/', article_list_create_api_view, name='article-list'),
    # path('articles-details/<int:pk>/', article_detail, name='article-detail')

    path('articles/', ArticleListCreateAPIView.as_view(), name='article-list'),
    path('articles-details/<int:pk>/', ArticleDetailAPIView.as_view(), name='article-detail'),
    path('journalists/', JournalistListCreateAPIView.as_view(), name='journalist-list')
]