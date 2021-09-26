from django.shortcuts import render, redirect
from .models import Note


def index(request):
    last_note = Note.objects.last()

    if last_note == None: 
      last_note = "" 

    return render(request, 'notes/index.html', { "content": last_note.content })

def add(request):
    content = request.POST.get('content')

    new_note = Note(content=content)
    new_note.save()

    return redirect('index')

