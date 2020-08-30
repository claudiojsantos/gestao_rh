from django.urls import path, include
from .views import ColaboradoresList, ColaboradorEdit, ColaboradorDelete, ColaboradorCreate

urlpatterns = [
    path('', ColaboradoresList.as_view(), name='list_colaboradores'),
    path('edit/<int:pk>/', ColaboradorEdit.as_view(), name='edit_colaborador'),
    path('delete/<int:pk>/', ColaboradorDelete.as_view(), name='delete_colaborador'),
    path('new/', ColaboradorCreate.as_view(), name='create_colaborador'),
]
