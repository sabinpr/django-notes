"""
URL configuration for Notes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base.views import create_note, notetype_view, home_view, create_note_type, edit_note_view, delete_note_view, delete_notetype_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('notetype/', notetype_view, name='notetype'),
    path('createnote/', create_note),
    path('create_note_type/', create_note_type),
    path('edit_note/<int:pk>/', edit_note_view, name='edit_note'),
    path('delete_note/<int:pk>/', delete_note_view, name='delete_note'),
    path('delete_notetype/<int:pk>/', delete_notetype_view, name='delete_notetype')
]
