from django.shortcuts import render, redirect
from django.contrib import messages
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
            messages.success(request, 'New note created!')
            return redirect('home')

        else:
            messages.error(request, form.errors)
    else:
        form = NoteForm()
    return render(request, 'createnote.html', {'form': form})


def create_note_type(request):
    if request.method == 'POST':
        form = NoteTypeForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'note type created!')
            return redirect('notetype')
        else:
            messages.error(request, form.errors)
    else:
        form = NoteTypeForm()
    data = {'form': form}
    return render(request, 'create_note_type.html', context=data)


def edit_note_view(request, pk):
    note_obj = Note.objects.get(id=pk)
    if request.method == "POST":
        note_form_obj = NoteForm(data=request.POST, instance=note_obj)
        if note_form_obj.is_valid():
            note_form_obj.save()
            messages.success(request, 'note type Updated!')
            return redirect('home')
        else:
            messages.error(request, note_form_obj.errors)

    note_form_obj = NoteForm(instance=note_obj)
    data = {'form': note_form_obj}
    return render(request, 'edit_note.html', context=data)


def delete_note_view(request, pk):
    note_obj = Note.objects.get(id=pk)
    note_obj.delete()

    messages.success(request, 'note deleted!')
    return redirect('home')


def delete_notetype_view(request, pk):
    notetype_obj = NoteType.objects.get(id=pk)
    notetype_obj.delete()
    messages.success(request, 'notetype deleted!')
    return redirect('notetype')
