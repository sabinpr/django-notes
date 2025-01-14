from django.shortcuts import render, redirect
from .models import Note
from .models import NoteType
from .forms import NoteForm, NoteTypeForm

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
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = NoteForm()
    return render(request, 'createnote.html', {'form': form})


def success(request):
    return render(request, 'success.html')


def create_note_type(request):
    if request.method == 'POST':
        form = NoteTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notetype_view')
    else:
        form = NoteTypeForm()
    return render(request, 'create_note_type.html', {'form': form})
