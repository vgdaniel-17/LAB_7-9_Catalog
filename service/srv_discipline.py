from domain.disciplina import Discipline

class Service_Discipline:
    def __init__(self, repo_discipline, validator_disicipline):
        self.__repo = repo_discipline
        self.__validator = validator_disicipline


    # ADD --------------------------------------------------------------------------------------------------------------
    def adauga_disciplina(self, id_disciplina, nume_disciplina, profesor):
        disciplina = Discipline(id_disciplina, nume_disciplina, profesor)
        self.__validator.validare_disciplina(id_disciplina, nume_disciplina, profesor)
        self.__repo.adauga_disciplina(disciplina)

    # DEL --------------------------------------------------------------------------------------------------------------
    def sterge_disciplina(self, id_disciplina):
        self.__validator.id(id_disciplina)
        self.__repo.sterge_disciplina(id_disciplina)

    # UPDATE -----------------------------------------------------------------------------------------------------------
    def modifica_disciplina(self, id_disciplina, nume, profesor):
        self.__validator.profesor(profesor)
        self.__validator.id(id_disciplina)
        disciplina_nou = Discipline(id_disciplina, nume, profesor)
        self.__repo.modifica_disciplina(disciplina_nou)

    # FIND -------------------------------------------------------------------------------------------------------------
    def cauta_profesor_disciplina(self, id_disciplina):
        self.__validator.disciplina(id_disciplina)
        return self.__repo.cauta(id_disciplina)

    # LIST-ACITVE ------------------------------------------------------------------------------------------------------
    def get_all_dis(self):
        return self.__repo.get_all()

    # ALL-LIST ---------------------------------------------------------------------------------------------------------
    def get_all_all_dis(self):
        #Toata lista, inclusiv si cele sterse
        return self.__repo.get_all_all()

