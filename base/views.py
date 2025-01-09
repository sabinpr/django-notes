from django.shortcuts import render
from django.http import HttpResponse
from .models import Note

# Create your views here.


def home_view(request):
    note_objs = Note.objects.all().order_by('id')
    data = {'notes': note_objs}
    return render(request, 'index.html', context=data)
