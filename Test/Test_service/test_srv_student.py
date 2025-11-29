import unittest
from service.srv_student import service_student


# O copie fake pentru repo
class RepoStudentMock:
    def __init__(self, repo_studenti):
        self.__studenti = {}

    def adauga_student(self, student):
        if student.get_id_student() in self.__studenti:
            raise Exception('id dubilcat')
        self.__studenti[student.get_id_student()] = student

    def sterge_student(self, id_student):
        if id_student in self.__studenti:
            del self.__studenti[id_student]
        else:
            raise Exception('Nu exista student cu id respectiv')

    def cauta_student(self, id_student):
        if id_student in self.__studenti:
            return self.__studenti[id_student]
        else:
            raise Exception('Nu exista student cu id respectiv')

    def modifica_student(self, student):
        self.__studenti[student.get_id_student()] = student

    def get_all(self):
        return list(self.__studenti.values())

    def sterge_tot(self):
        self.__studenti = {}

# O copie fake pentru validare_student
class ValidatorStudentMock:
    def validare_student(self, id_stud, nume):
        if id_stud < 0: raise Exception("ID invalid")
        if not nume: raise Exception("Nume vid")

    def validare_id(self, id_stud):
        if id_stud < 0: raise Exception("ID invalid")




class SrvStudentTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Incep testele pentru service.studenti")

    @classmethod
    def tearDownClass(cls):
        print("Teste: OK!")

    def setUp(self):
        self.repo_mock = RepoStudentMock(self)
        self.validator_mock = ValidatorStudentMock()
        self.service = service_student(self.repo_mock, self.validator_mock)


    def test_adauga_student(self):
        self.service.adauga_student(123, 'Mihai')
        lista = self.service.get_all_student_active()
        self.assertEqual(len(lista), 1)
        self.assertEqual(lista[0].get_id_student(), 123)
        with self.assertRaises(Exception):
            self.service.adauga_student(-1, 'Mihai')
        with self.assertRaises(Exception):
            self.service.adauga_student(123, 'Bogdan')

    def test_sterge_student(self):
        self.service.adauga_student(123, 'Andrei')
        self.assertEqual(len(self.service.get_all_student_active()), 1)

        self.service.sterge_student(123)
        self.assertEqual(len(self.service.get_all_student_active()), 0)

        with self.assertRaises(Exception):
            self.service.sterge_student(1234)

    def test_modifica_student(self):
        self.service.adauga_student(123, 'Mihai')
        self.service.modifica_student(123, "Matei")

        student = self.service.cauta_student(123)

        self.assertEqual(student.get_id_student(), 123)
        self.assertEqual(student.get_nume_student(), "Matei")

        with self.assertRaises(Exception):
            self.service.modifica_student(1234,"ceva")

    def test_cauta_student(self):
        self.service.adauga_student(123, 'Mihai')
        cautat = self.service.cauta_student(123)
        self.assertEqual(cautat.get_nume_student(), "Mihai")

        with self.assertRaises(Exception):
            self.service.cauta_student(123421)

    def test_generare(self):
        nr = 10

        self.service.generare(nr)

        lista = self.service.get_all_student_active()

        self.assertTrue(len(lista) > 0)
        self.assertEqual(len(lista), nr)

    def test_golire_lista_student(self):
        self.service.adauga_student(1, 'A')
        self.service.adauga_student(2, 'B')
        self.service.adauga_student(3, 'C')
        self.service.adauga_student(4, 'D')
        self.service.adauga_student(5, 'E')
        self.service.adauga_student(6, 'F')
        self.service.adauga_student(7, 'G')
        self.assertEqual(len(self.service.get_all_student_active()), 7)
        self.service.golire_lista_student()
        self.assertEqual(len(self.service.get_all_student_active()), 0)




