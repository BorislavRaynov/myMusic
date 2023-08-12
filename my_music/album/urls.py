from django.urls import path
from .views import add_album, album_details, album_edit, album_delete

urlpatterns = [
    path('add/', add_album, name='add-album'),
    path('details/<int:album_id>/', album_details, name='album-details'),
    path('edit/<int:album_id>/', album_edit, name='album-edit'),
    path('delete/<int:album_id>/', album_delete, name='album-delete')
]