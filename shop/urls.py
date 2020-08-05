from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name="mainpage"),
    path('index/', views.redirect_to_mainpage, name="mainpage_index"),
    path('home/', views.redirect_to_mainpage, name="mainpage_red"),
    path('<int:item_id>/', views.detail, name='detail'),
    path('search/', views.search, name="search"),
    path('<str:cat>/', views.category_filter, name="category_filter"),
]
