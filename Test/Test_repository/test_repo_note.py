import unittest
import os
from repository.repository_note import RepoNote
from domain.note import Note

class TestRepoStudent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Incep testele pentru repo.note")

    @classmethod
    def tearDownClass(cls):
        print("Teste: OK!")

    def setUp(self):
        self.cale_fiser = r"E:\Coding\Python\LC\LAB_7-9\Test\Test_repository\test_repo_storage.txt"
        with open(self.cale_fiser, "w", encoding="utf-8") as f:
            f.write("")
        self.repo = RepoNote(self.cale_fiser)

    def tearDown(self):
        # Stergem fiserul
        if os.path.exists(self.cale_fiser):
            os.remove(self.cale_fiser)

    def test_adauga_nota(self):
        nota = Note(123, 999, 10)
        self.repo.adauga_note(nota)
        self.assertEqual(len(self.repo.get_all_note()), 1)

    def test_get_all_note(self):
        nota1 = Note(123, 999, 10)
        nota2 = Note(234, 124, 3)
        self.repo.adauga_note(nota1)
        self.repo.adauga_note(nota2)
        self.assertEqual(len(self.repo.get_all_note()), 2)

