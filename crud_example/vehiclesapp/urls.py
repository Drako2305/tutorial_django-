from django.contrib import admin
from django.urls import path
from vehiclesapp.views import create_view, list_view, update_view, delete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_view),
    path('create/', create_view),
    path('update/<id>', update_view),
    path('delete/<id>', delete_view),
]
