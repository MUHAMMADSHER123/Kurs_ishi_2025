from django.urls import path
from editor.views import index

urlpatterns = [
    path('', index, name='index'),
]