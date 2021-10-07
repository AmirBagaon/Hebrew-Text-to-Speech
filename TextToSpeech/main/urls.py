from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('temp', views.temp, name='temp'),
    path('translate', views.translate_view, name='translate'),
    path('text_utils', views.text_utils, name='text_utils'),
    path('text_to_speech', views.text_to_speech, name='text_to_speech'),
]