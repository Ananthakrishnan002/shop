from django.urls import path
from .import views




urlpatterns = [

    path('',views.listProduct,name = 'list'),
    path('add/', views.addProduct, name='add')

]
