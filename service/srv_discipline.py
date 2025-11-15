from domain.disciplina import Discipline

class Service_Discipline:
    def __init__(self, repo_discipline, validator_disicipline, business):
        self.__repo = repo_discipline
        self.__validator = validator_disicipline
        self.__business  = business

    def add_discipline(self, id_disciplina, nume_disciplina, profesor):
        disciplina = Discipline(id_disciplina, nume_disciplina, profesor)
        self.__validator.add_discipline(disciplina)
        self.__repo.add_discipline(disciplina)

    def del_discipline(self, id_disciplina):
        self.__validator.disciplina(id_disciplina)
        self.__repo.del_disciplina(id_disciplina)

    def modifica_profesor_disciplina(self, id_disciplina, profesor):
        #Modifica un profesor de la o disciplina
        self.__validator.profesor(profesor)
        self.__validator.disciplina(id_disciplina)
        self.__repo.modifica_profesor_disciplina(id_disciplina, profesor)

    def cauta_profesor_disciplina(self, id_disciplina):
        self.__validator.disciplina(id_disciplina)
        return self.__business.cauta_disciplina(id_disciplina)

    def get_all_disciplinas(self):
        return self.__repo.get_all_disciplinas()

