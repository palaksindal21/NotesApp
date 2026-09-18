from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from . models import *
from . serializers import *

class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


def home(request):
    notes = Note.objects.all().order_by('-created_at')

    return render(request, 'notesapp/index.html', {'notes': notes})


def create_note(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category = request.POST.get('category')
        is_pinned = request.POST.get('is_pinned') == 'on'
        is_archived = request.POST.get('is_archived') == 'on'

        Note.objects.create(
            title = title,
            content = content,
            category = category,
            is_pinned = is_pinned,
            is_archived = is_archived
        )

        return redirect('home')
    return redirect('home')


def edit_note(request, id):

    note = get_object_or_404(Note, id=id)

    if request.method == 'POST':

        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.category = request.POST.get('category')

        note.is_pinned = request.POST.get('is_pinned') == 'on'
        note.is_archived = request.POST.get('is_archived') == 'on'

        note.save()

        return redirect('home')

    return render(
        request,
        'notesapp/edit.html',
        {'note': note}
    )


def delete_note(request, id):

    note = get_object_or_404(Note, id=id)

    if request.method == 'POST':
        note.delete()

    return redirect('home')


