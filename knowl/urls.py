from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="knowl-home"),
    path('<int:file_id>/share/', views.share_file, name='share_file'),
]