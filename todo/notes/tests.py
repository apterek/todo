from django.test import TestCase
from notes.models import Note


class Testnotes(TestCase):
    def test_create_note(self) -> None:
        self.notes = Note.objects.create(title="test", text="test_text")
