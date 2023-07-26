from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from api.resources import NoteResource

note_resource = NoteResource()

urlpatterns = [
    path('admin/', admin.site.urls),
]
