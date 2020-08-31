from django.urls import path

from .views import DepartamentoList, DepartamentoCreate, DepartamentoEdit, DepartamentoDelete

urlpatterns = [
    path('', DepartamentoList.as_view(), name='list_departamentos'),
    path('new/', DepartamentoCreate.as_view(), name='create_departamento'),
    path('edit/<int:pk>', DepartamentoEdit.as_view(), name='edit_departamento'),
    path('delete/<int:pk>', DepartamentoDelete.as_view(), name='delete_departamento')
]