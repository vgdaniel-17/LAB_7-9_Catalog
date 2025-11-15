
from domain.studenti import Studenti

class service_student:
    def __init__(self, repo_studenti, validator_studenti):
        self.__repo = repo_studenti
        self.__validator = validator_studenti

    def adauga_studenti(self, id_student, nume):
        self.__validator.adauga_studenti(id_student, nume)
        self.__repo.adauga_studenti(id_student, nume)

    def sterge_studenti(self, id_student, nume):
        self.__validator.sterge_studenti(id_student, nume)
        self.__repo.sterge_studenti(id_student, nume)

    def