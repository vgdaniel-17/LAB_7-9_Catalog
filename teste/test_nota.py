import unittest

from domain.studenti import Student
from domain.disciplina import Discipline
from domain.note import Note

from repository.repository_studenti import RepoStudent
from repository.repository_discipline import RepoDiscipline
from repository.repository_note import RepoNote

from validation.validator_note import NotaValidator

from service.srv_note import Service_Note


class TestStatisticaTop20(unittest.TestCase):

    def setUp(self):

        self.repo_stud = RepoStudent()
        self.repo_dis = RepoDiscipline()
        self.repo_note = RepoNote()


        self.validator = NotaValidator()

        self.service = Service_Note(
            self.repo_note,
            self.repo_stud,
            self.repo_dis,
            self.validator,
        )

        self.repo_stud.adauga_student(Student(1, "Andrei Marin"))
        self.repo_stud.adauga_student(Student(2, "Bogdan Camino"))
        self.repo_stud.adauga_student(Student(3, "Carmen Ciuca"))
        self.repo_stud.adauga_student(Student(4, "Daria Elena"))
        self.repo_stud.adauga_student(Student(5, "Gabita Miha"))

        self.repo_dis.adauga_disciplina(Discipline(10, "Mate", "Popescu Andrei"))

        note_test = [
            Note(1, 10, 10),
            Note(2, 10, 9),
            Note(3, 10, 5),
            Note(4, 10, 10),
            Note(5, 10, 4)
        ]

        for n in note_test:
            self.repo_note.adauga_note(n)

    def test_statistica_top20(self):
        rezultat = self.service.statistica_top20()

        self.assertEqual(len(rezultat), 1)

        self.assertIn("Andrei", rezultat[0])

        self.assertTrue("Media:" in rezultat[0])


if __name__ == '__main__':
    unittest.main()
