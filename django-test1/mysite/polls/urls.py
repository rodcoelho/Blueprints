from django.urls import path

from . import views

urlpatterns = [
    # path('', views.FUNCTION, name='FUNCTION')
    path('', views.index, name='index')
]

