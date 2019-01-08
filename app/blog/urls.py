from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
)

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:id>', ArticleDetailView.as_view(), name='article-detail'),
    # path('create/', ArticleCreateView.as_view(), name='article-create'),
    # path('update/', ArticleUpdateView.as_view(), name='article-update'),
    # path('delete/', ArticleDeleteView.as_view(), name='article-delete'),
]