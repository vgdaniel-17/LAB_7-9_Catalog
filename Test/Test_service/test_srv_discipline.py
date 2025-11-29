from service.srv_student import service_student
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
    def setUp(self):
        self.repo = RepoDisciplineMock()
        self.validator = ValidatorDisciplineMock()
        self.service = service_student(self.repo, self.validator)
