from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Note, Tag
from .serializers import NoteSerializer


def index(request):
    all_notes = Note.objects.all()

    return render(request, 'notes/index.html', {'notes': all_notes})

def add(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    tag = request.POST.get('tag')

    new_tag, created = Tag.objects.get_or_create(name=tag)

    new_note = Note(title=title, content=content, tag_id=new_tag)
    new_note.save()

    return redirect('index')

def update(request):

    request_string = request.GET.get('update')

    params = {}

    for chave_valor in request_string.split('&'):
        chave = chave_valor.split('=')[0]
        valor = chave_valor.split('=')[1]
        params[chave] = valor

    note_id, title, content, tag_id = params["id"], params["title"], params["content"], params["tag_id"]
    
    new_tag, created = Tag.objects.get_or_create(name=tag_id)

    note_to_update = Note.objects.get(id=int(note_id))
    note_to_update.title = title
    note_to_update.content = content
    note_to_update.tag_id = new_tag

    note_to_update.save()

    return redirect('index')

def delete(request):
    note_id = request.GET.get('delete')

    note_to_delete = Note.objects.get(id=int(note_id))
    note_to_delete.delete()

    return redirect('index')

def tags(request):
    all_tags = Tag.objects.all()

    return render(request, 'notes/tags.html', {'tags': all_tags})

def details(request):

    name = request.GET.get("name")

    tag = Tag.objects.get(name=name)

    notes = Note.objects.filter(tag_id=tag.id)

    return render(request, 'notes/details.html', {'notes': notes, 'name': name})

@api_view(['GET', 'POST'])
def api_note(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        raise Http404()

    if request.method == 'POST':
        new_note_data = request.data
        note.title = new_note_data['title']
        note.content = new_note_data['content']
        note.save()
    
    serialized_note = NoteSerializer(note)
    return Response(serialized_note.data)

@api_view(['GET', 'POST'])
def api_notes(request):
    try:
        notes = Note.objects.all()
    except Note.DoesNotExist:
        raise Http404()

    if request.method == 'POST':
        new_note_data = request.data
        new_note = Note(title=new_note_data['title'], content=new_note_data['content'])
        new_note.save()
    
    serialized_notes = NoteSerializer(notes, many=True)

    return Response(serialized_notes.data)
