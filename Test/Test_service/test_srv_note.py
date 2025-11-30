from domain.studenti import Student
from domain.disciplina import Discipline
from domain.note import Note
from service.srv_note import Service_Note
import unittest
from Error.Srv_note import ErrorSN

class RepoStudentMock:
    def __init__(self):
        self.studenti = {
            1: Student(1, "Mihai"),
            2: Student(2, "Gabi"),
            3: Student(3, "Ioana"),
            4: Student(4, "Kim"),
            5: Student(5, "Jim"),
        }
    def cauta_student(self, id_student):
        if id_student in self.studenti:
            return self.studenti[id_student]
        raise Exception("id_student not found")

    def get_all(self):
        return list(self.studenti.values())

class RepoDisciplinaMock:
    def __init__(self):
        self.disciplina = {
            10: Discipline(10, "Mate", "Matei"),
            20: Discipline(20, "Mate", "Raul"),
            30: Discipline(30, "Mate", "Jhon"),
            40: Discipline(40, "Mate", "Juan"),
            50: Discipline(50, "Mate", "Ion"),
        }

    def cauta(self, id_disciplina):
        if id_disciplina in self.disciplina:
            return self.disciplina[id_disciplina]
        else:
            raise Exception("id_disciplina not found")

    def get_all(self):
        return list(self.disciplina.values())

class RepoNoteMock:
    def __init__(self):
        self.note = []

    def adauga_note(self, nota):
        self.note.append(nota)

    def get_all_note(self):
        return self.note[:]

    def sterge_tot(self):
        self.note = []

class ValidatorNoteMock:
    def valideaza_nota(self, nota):
        if nota.get_nota() <= 0 or nota.get_nota() > 10:
            raise Exception("nota invalida")


class TestServiceNote(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Incep testele pentru service.studenti")

    @classmethod
    def tearDownClass(cls):
        print("Teste: OK!")

    def setUp(self):
        self.repo_note_mock = RepoNoteMock()
        self.repo_stud_mock = RepoStudentMock()
        self.repo_dis_mock = RepoDisciplinaMock()
        self.val_mock = ValidatorNoteMock()
        self.srv = Service_Note(
            self.repo_note_mock,
            self.repo_stud_mock,
            self.repo_dis_mock,
            self.val_mock
        )

    def test_adauga_nota(self):

        self.srv.adauga_note(1, 10, 7)
        self.assertEqual(len(self.repo_note_mock.get_all_note()), 1)

        nota = self.repo_note_mock.get_all_note()[0]
        self.assertEqual(nota.get_nota(), 7)
        self.assertEqual(nota.get_student(), 1)
        self.assertEqual(nota.get_disciplina(), 10)


        with self.assertRaises(Exception):
            self.srv.adauga_note(999, 10, 5)

        with self.assertRaises(Exception):
            self.srv.adauga_note(1, 999, 5)

        with self.assertRaises(Exception):
            self.srv.adauga_note(1, 10, 15)

    def test_list_note(self):
        self.srv.adauga_note(1, 10, 8)
        self.srv.adauga_note(1, 20, 9)

        rezultat = self.srv.list_note(1)
        self.assertEqual(len(rezultat), 2)
        self.assertIn("Mate", rezultat[0])
        self.assertIn("Mate", rezultat[1])

    def test_generare(self):
        self.srv.generare(3)
        self.assertEqual(len(self.repo_note_mock.get_all_note()), 3)

        self.repo_stud_mock.studenti = {}
        with self.assertRaises(Exception):
            self.srv.generare(1)

    def test_golire_lista_note(self):
        self.srv.generare(5)
        self.srv.golire_lista_note()
        self.assertEqual(len(self.repo_note_mock.get_all_note()), 0)

    def test_statistica_top20(self):
        self.srv.adauga_note(1, 10, 10)
        self.srv.adauga_note(2, 10, 9)
        self.srv.adauga_note(3, 10, 8)
        self.srv.adauga_note(4, 10, 7)
        self.srv.adauga_note(5, 10, 6)

        top = self.srv.statistica_top20()

        self.assertEqual(len(top), 1)
        self.assertIn("Mihai", top[0])
        self.assertIn("10.0", top[0])

    def test_sortare_stud_dis(self):
        self.srv.adauga_note(1, 10, 9)
        self.srv.adauga_note(2, 10, 10)

        rez = self.srv.sortare_stud_dis(10)

        self.assertIn("Gabi", rez[0])
        self.assertIn("Mihai", rez[1])