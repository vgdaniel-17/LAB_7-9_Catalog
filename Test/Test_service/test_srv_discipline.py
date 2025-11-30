from service.srv_discipline import Service_Discipline
from domain.disciplina import Discipline
import unittest

# Copie fake pentru repo
class RepoDisciplineMock:
    def __init__(self):
        self.__discipline = {}

    def adauga_disciplina(self, disciplina):
        if disciplina.get_id_disciplina() in self.__discipline:
            raise Exception("ID Disciplina duplicat")
        self.__discipline[disciplina.get_id_disciplina()] = disciplina

    def sterge_disciplina(self, id_disciplina):
        if id_disciplina in self.__discipline:
            del self.__discipline[id_disciplina]
        else:
            raise Exception("Nu exista disciplina")

    def modifica_disciplina(self, disciplina_noua):
        id_d = disciplina_noua.get_id_disciplina()
        if id_d in self.__discipline:
            self.__discipline[id_d] = disciplina_noua
        else:
            raise Exception("Nu exista disciplina")

    def cauta(self, id_disciplina):
        if id_disciplina in self.__discipline:
            return self.__discipline[id_disciplina]
        raise Exception("Nu exista disciplina")

    def get_all(self):
        return list(self.__discipline.values())

    def sterge_tot(self):
        self.__discipline = {}

class ValidatorDisciplineMock:
    def validare_disciplina(self, id_d, nume, prof):
        if id_d < 0: raise Exception("ID invalid")
        if not nume: raise Exception("Nume vid")
        if not prof: raise Exception("Profesor vid")

    def id(self, id_d):
        if id_d < 0: raise Exception("ID invalid")

    def profesor(self, prof):
        if not prof: raise Exception("Profesor vid")

class RepoDisciplineTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Incep testele pentru service.studenti")

    @classmethod
    def tearDownClass(cls):
        print("Teste: OK!")


    def setUp(self):
        self.repo = RepoDisciplineMock()
        self.validator = ValidatorDisciplineMock()
        self.service = Service_Discipline(self.repo, self.validator)

    def test_adauga_disciplina(self):
        self.service.adauga_disciplina(123, "Mate", "Gabi")
        lista = self.service.get_all_dis()

        self.assertEqual(len(lista), 1)
        self.assertEqual(lista[0].get_nume_disciplina(), "Mate")
        self.assertEqual(lista[0].get_id_disciplina(), 123)
        self.assertEqual(lista[0].get_profesor(), "Gabi")
        with self.assertRaises(Exception):
            self.service.adauga_disciplina(123, "Altceva", "Z")

    def test_sterge_disciplina(self):
        self.service.adauga_disciplina(123, "Mate", "Gabi")
        self.assertEqual(len(self.service.get_all_dis()), 1)

        self.service.sterge_disciplina(123)

        self.assertEqual(len(self.service.get_all_dis()), 0)

        with self.assertRaises(Exception):
            self.service.sterge_disciplina(123)

    def test_modifica_disciplina(self):
        self.service.adauga_disciplina(123, "Mate", "Gabi")
        self.assertEqual(len(self.service.get_all_dis()), 1)
        self.service.modifica_disciplina(123, "Info", "Jhon")
        dis = self.service.get_all_dis()[0]
        self.assertEqual(dis.get_nume_disciplina(), "Info")
        self.assertEqual(dis.get_profesor(), "Jhon")

    def test_cauta(self):
        self.service.adauga_disciplina(123, "Mate", "Gabi")
        dis = self.service.cauta_disciplina(123)
        self.assertEqual(dis.get_nume_disciplina(), "Mate")
        self.assertEqual(dis.get_profesor(), "Gabi")

    def test_generare(self):
        nr = 5
        self.service.generare(nr)
        self.assertEqual(len(self.service.get_all_dis()), nr)

    def test_golire_lista_dis(self):
        self.service.generare(10)
        self.assertEqual(len(self.service.get_all_dis()), 10)
        self.service.golire_lista_dis()
        self.assertEqual(len(self.service.get_all_dis()), 0)





