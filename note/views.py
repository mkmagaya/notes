from ast import Try
from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView

from .forms import NoteForm
from .models import Note

# class based views

class NotesDeleteView(DeleteView):
    model = Note
    success_url = '/smart/notes'
    template_name = 'note/notes_delete.html'

class NotesUpdateView(UpdateView):
    model = Note
    success_url = '/smart/notes'
    form_class = NoteForm

class NotesCreateView(CreateView):
    model = Note
    # fields = ['title', 'notes']
    success_url = '/smart/notes'
    form_class = NoteForm

class NotesListView(ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'note/notes_list.html'

class NoteDetailListView(DetailView):
    model = Note
    context_object_name = 'note'    
    

# def list(request):
#     all_notes = Note.objects.all()
#     return render(request, 'note/notes_list.html', {'notes': all_notes})


# handling non existing data
# def handle_existence(model):
#     def check_entity(fun):
#         @wraps(fun)
#         def inner_fun(*args, **kwargs):
#             try:
#                 x = fun(*args, **kwargs)
#                 return x
#             except model.DoesNotExist:
#                 raise Http404('Note Does Not Exist')
#             return inner_fun
#         return check_entity



# @handle_existence(Note)
# def detail(self, request, pk, format=None):
#     note = Note.objects.get(pk=pk)
#     return render(request, 'note/note_detail.html', {'note':note})

# def detail(request, pk):
#     try:
#         note = Note.objects.get(pk=pk)
#     except Note.DoesNotExist:
#         raise Http404('Note Does Not Exist, Sorry Hako Wanzwa')
#     return render(request, 'note/note_detail.html', {'note':note})


