# core/urls.py
from django.urls import path
from . import views  # Импортируем наши обработчики из соседнего файла

urlpatterns = [
    path('', views.hello_world), # Привязываем адрес /hello/ к функции
]