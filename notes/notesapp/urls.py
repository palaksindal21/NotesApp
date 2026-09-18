from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . views import *

router = DefaultRouter()
router.register('notes', NoteViewSet)


urlpatterns = [
    path('', home, name='home'),
    path('create/',create_note, name='create_note'),
    path('edit/<int:id>/',edit_note, name='edit_note'),
    path('delete/<int:id>/', delete_note, name='delete_note'),
    path('api/', include(router.urls)),
]