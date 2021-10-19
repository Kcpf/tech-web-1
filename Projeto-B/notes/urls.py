from django.urls import path

from . import views

urlpatterns = [
    path('api/notes/<int:note_id>/', views.api_note),
    path('api/notes/', views.api_notes),
    path('details', views.details, name="details"),
    path('tags', views.tags, name="tags"),
    path('update', views.update, name="update"),
    path('add', views.add, name="add"),
    path('delete', views.delete, name="delete"),
    path('', views.index, name='index')
]