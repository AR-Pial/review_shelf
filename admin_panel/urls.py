from django.urls import path
from .views import *

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('book', BookView.as_view(), name='book'),
    # Author
    path('author/list', AuthorListView.as_view(), name='author'),
    path('author/create', AuthorCreateView.as_view(), name='author_create'),
    path('author/<uuid:pk>/edit/', AuthorUpdateView.as_view(), name='author_edit'),
    path('author/<uuid:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete'),
    # Genre
    path('genre/list', GenreListView.as_view(), name='genre_list'),
    path('genre/create', GenreCreateView.as_view(), name='genre_create'),
    path('genre/<int:pk>/update/', GenreUpdateView.as_view(), name='genre_update'),
    path('genre/<int:pk>/delete/', GenreDeleteView.as_view(), name='genre_delete'),
    # Type
    path('type/list', TypeListView.as_view(), name='type_list'),
    path('type/create', TypeCreateView.as_view(), name='type_create'),
    path('type/<int:pk>/update/', TypeUpdateView.as_view(), name='type_update'),
    path('type/<int:pk>/delete/', TypeDeleteView.as_view(), name='type_delete'),
]
