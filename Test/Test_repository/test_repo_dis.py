import unittest
import os
from repository.repository_discipline import RepoDiscipline
from domain.disciplina import Discipline

class TestRepository(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Incep testele pentru repo.discipline")

    @classmethod
    def tearDownClass(cls):
        print("Teste: OK!")

    def setUp(self):
        self.cale_fiser = r"E:\Coding\Python\LC\LAB_7-9\Test\Test_repository\test_repo_storage.txt"
        with open(self.cale_fiser, "w", encoding="utf-8") as f:
            f.write("")
        self.repo = RepoDiscipline(self.cale_fiser)

    def tearDown(self):
        if os.path.exists(self.cale_fiser):
            os.remove(self.cale_fiser)

    def test_adauga_disciplina(self):
        dis = Discipline(123, "Mate", "Ionescu Mihai")
        self.repo.adauga_disciplina(dis)
        self.assertEqual(len(self.repo.get_all_all()), 1)
        self.assertEqual(str(self.repo.cauta(123)), "123 | Mate | Ionescu Mihai")

    def test_sterge_disciplina(self):
        dis = Discipline(123, "Mate", "Ionescu Mihai")
        self.repo.adauga_disciplina(dis)
        self.assertEqual(len(self.repo.get_all_all()), 1)
        self.repo.sterge_disciplina(123)
        self.assertEqual(len(self.repo.get_all_all()), 1)
        lista = self.repo.get_all()
        self.assertEqual(len(lista), 0)

    def test_modifica_disciplina(self):
        dis = Discipline(123, "Mate", "Ionescu Mihai")
        dis_new = Discipline(123, "Info", "Matrice")
        self.repo.adauga_disciplina(dis)
        self.assertEqual(str(self.repo.cauta(123)), "123 | Mate | Ionescu Mihai")
        self.repo.modifica_disciplina(dis_new)
        self.assertEqual(len(self.repo.get_all()), 1)
        self.assertEqual(str(self.repo.cauta(123)), "123 | Info | Matrice")

    def test_cauta(self):
        dis = Discipline(123, "Mate", "Ionescu Mihai")
        self.repo.adauga_disciplina(dis)
        self.assertEqual(str(self.repo.cauta(123)), "123 | Mate | Ionescu Mihai")

    def test_get_all(self):
        dis1 = Discipline(123, "Mate", "Ionescu Mihai")
        dis2 = Discipline(567, "Info", "Matrice")
        dis3 = Discipline(890, "Geo", "Blea")
        self.repo.adauga_disciplina(dis1)
        self.repo.adauga_disciplina(dis2)
        self.repo.adauga_disciplina(dis3)
        self.repo.sterge_disciplina(123)
        self.assertEqual(len(self.repo.get_all()), 2)

    def test_get_all_all(self):
        dis1 = Discipline(123, "Mate", "Ionescu Mihai")
        dis2 = Discipline(567, "Info", "Matrice")
        dis3 = Discipline(890, "Geo", "Blea")
        self.repo.adauga_disciplina(dis1)
        self.repo.adauga_disciplina(dis2)
        self.repo.adauga_disciplina(dis3)
        self.repo.sterge_disciplina(123)
        self.assertEqual(len(self.repo.get_all_all()), 3)


