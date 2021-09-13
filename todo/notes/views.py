from django.shortcuts import render
from notes.forms import AddNoteForm
from notes.models import Note
from notes.services import created_notes
import logging


logger = logging.getLogger(__name__)


def index(request):
    if request.method == "POST":
        form = AddNoteForm(request.POST)
        if form.is_valid():
            created_notes(form, title="title", text="text")
    else:
        form = AddNoteForm()
    notes = Note.objects.all()

    return render(request, "note_list.html", {"notes": notes, "form": form})
