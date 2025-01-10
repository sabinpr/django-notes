from django.shortcuts import render
from django.http import HttpResponse
from .models import Note
from .models import NoteType

# Create your views here.


def home_view(request):
    note_objs = Note.objects.all().order_by('id')
    data = {'notes': note_objs}
    return render(request, 'index.html', context=data)


def notetype_view(request):
    notetype_obj = NoteType.objects.all().order_by('id')
    note_data = {"notetypes": notetype_obj}
    return render(request, 'notetype.html', context=note_data)


def create_note(request):
    return render(request, 'createnote.html')
