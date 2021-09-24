from django.shortcuts import render, redirect
from .models import Note, Tag


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
