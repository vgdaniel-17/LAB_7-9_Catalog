import unittest
import os
from domain.studenti import Student
from repository.repository_studenti import RepoStudent

class TestRepoStudent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Incep testele pentru repo.studenti")

    @classmethod
    def tearDownClass(cls):
        print("Teste: OK!")

    def setUp(self):
        self.cale_fiser = r"E:\Coding\Python\LC\LAB_7-9\Test\Test_repository\test_repo_storage.txt"
        with open(self.cale_fiser, "w", encoding="utf-8") as f:
            f.write("")
        self.repo = RepoStudent(self.cale_fiser)

    def tearDown(self):
        # Stergem fiserul
        if os.path.exists(self.cale_fiser):
            os.remove(self.cale_fiser)

    def test_adauga_student(self):
        stud1 = Student(123, "Gabi")
        stud2 = Student(456, "Miha")
        self.setUp()
        self.repo.adauga_student(stud1)
        self.repo.adauga_student(stud2)
        lista = self.repo.get_all_all()
        self.assertEqual(len(lista), 2)

    def test_sterge_student(self):
        stud1 = Student(123, "Gabi")
        self.repo.adauga_student(stud1)
        self.assertEqual(len(self.repo.get_all_all()), 1)
        self.repo.sterge_student(123)
        self.assertEqual(len(self.repo.get_all_all()), 1)
        self.assertEqual(len(self.repo.get_all()), 0)

    def test_modifica_student(self):
        stud = Student(123, "Gabi")
        stud_new = Student(123, "Mihi")
        self.repo.adauga_student(stud)
        self.assertEqual(len(self.repo.get_all()), 1)
        self.assertEqual(str(self.repo.cauta_student(123)), "123 | Gabi")
        self.repo.modifica_student(stud_new)
        self.assertEqual(str(self.repo.cauta_student(123)), "123 | Mihi")
        self.assertEqual(len(self.repo.get_all()), 1)

    def cauta_student(self):
        stud = Student(123, "Gabi")
        self.repo.adauga_student(stud)
        self.assertEqual(str(self.repo.cauta_student(123)), "123 | Gabi")

    def test_get_all_all(self):
        stud1 = Student(123, "Gabi")
        stud2 = Student(456, "Mihi")
        stud3 = Student(789, "Ionut")
        self.repo.adauga_student(stud1)
        self.repo.adauga_student(stud2)
        self.repo.adauga_student(stud3)
        lista = self.repo.get_all_all()
        self.assertEqual(len(lista), 3)

    def test_get_all(self):
        stud1 = Student(123, "Gabi")
        stud2 = Student(456, "Mihi")
        stud3 = Student(789, "Ionut")
        self.repo.adauga_student(stud1)
        self.repo.adauga_student(stud2)
        self.repo.adauga_student(stud3)
        self.repo.sterge_student(123)
        lista = self.repo.get_all()
        self.assertEqual(len(lista), 2)