from logging import NOTSET

from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView,ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NotesForm
from .models import Notes


def change_visibility(request, pk):
    if request.method == 'POST':
        note=get_object_or_404(Notes, pk=pk)
        note.is_public= not note.is_public
        note.save()
        return HttpResponseRedirect(reverse("notes.detail", args=[note.pk]))
    raise Http404


class NotesCreateView(CreateView):
    model = Notes
    template_name = "notes_form.html"
    success_url = '/smart/notes'
    form_class = NotesForm

    #to fix IntegrityError at /smart/notes/new
    #we create an object with user before directly saving to the db
    #commit=False ->  prohibit saving to the database
    def form_valid(self, form):
        self.object = form.save(commit=False) #do not directly store to the db
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes_list.html"
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes_detail.html"

class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    template_name = "notes_form.html"
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesDeleteView(LoginRequiredMixin,DeleteView):
    model = Notes
    template_name = 'notes_delete.html'
    success_url = '/smart/notes'

class NotesPublicDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes_detail.html"
    queryset = Notes.objects.filter(is_public=True)