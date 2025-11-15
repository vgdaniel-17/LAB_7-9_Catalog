from domain.studenti import Studenti

class service_student:
    def __init__(self, repo_studenti, validator_studenti):
        self.__repo = repo_studenti
        self.__validator = validator_studenti