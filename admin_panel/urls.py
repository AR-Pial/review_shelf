from django.urls import path
from .views import *

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('book', BookView.as_view(), name='book'),
    # Author
    path('author/list', AuthorListView.as_view(), name='author'),
    path('author/create', AuthorCreateView.as_view(), name='author_create'),
    path('author/<uuid:uuid>/edit/', AuthorUpdateView.as_view(), name='author_edit'),
    path('author/<uuid:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete'),
]
