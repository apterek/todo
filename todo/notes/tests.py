from django.test import TestCase, RequestFactory
from notes.models import Note
from notes.views import index


class Testnotes(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.notes = Note.objects.create(title="test", text="test_text")

    def test_maker(self):
        request = self.factory.get("")
        responce = index(request)
        self.assertEqual(responce.status_code, 200)
        self.assertEqual(self.notes.pk, 1)

