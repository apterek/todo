from notes.models import Note


def created_notes(form, title, text):
    Note.objects.create(
        title=form.cleaned_data[title], text=form.cleaned_data[text]
    )
