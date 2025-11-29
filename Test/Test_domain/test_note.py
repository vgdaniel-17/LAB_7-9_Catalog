import unittest
from domain.note import Note

class TestNote(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Incep testele pentru domain.note")

    @classmethod
    def tearDownClass(cls):
        print("Teste: OK!")

    def test_create_note(self):
        nota = Note(123, 121, 10)
        self.assertEqual(nota.get_student(), 123)
        self.assertEqual(nota.get_disciplina(), 121)
        self.assertEqual(nota.get_nota(), 10)
    def test_str(self):
        nota = Note(123, 121, 10)
        self.assertEqual(str(nota), "123 121 10")