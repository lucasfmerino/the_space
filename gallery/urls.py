from django.urls import path
from gallery.views import index, image

urlpatterns = [
    path('', index, name='index'),
    path('image/<int:photography_id>', image, name='image'),
]