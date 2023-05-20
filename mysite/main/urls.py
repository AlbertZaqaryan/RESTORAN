from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('delete/', views.delete_prod, name='delete'),
    path('category/<int:id>/', views.index_detail, name='index_detail')
]