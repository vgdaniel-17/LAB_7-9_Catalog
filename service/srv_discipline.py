from domain.disciplina import Discipline
import random

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
    def cauta_disciplina(self, id_disciplina):
        self.__validator.id(id_disciplina)
        return self.__repo.cauta(id_disciplina)

    # GEN --------------------------------------------------------------------------------------------------------------

    def generare(self, nr):
        disciplina = ["Limba si literatura romana", "Matematica", "Limba engleza", "Limba franceza", "Biologie", "Fizica", "Chimie", "Istorie", "Geografie", "Educatie civica", "Educatie plastica", "Educatie muzicala", "Educatie fizica si sport", "Informatica", "TIC", "Educatie tehnologica", "Consiliere si orientare"]
        profesori = ["Ion Popescu", "Maria Ionescu", "Andrei Vasilescu", "Elena Georgescu", "Radu Stan", "Laura Marinescu", "Daniel Petrescu", "Cristina Pavel", "Mihai Tudor", "Ana Dumitru", "Sorin Matei", "Irina Neagu", "Alexandru Barbu", "Oana Stoica", "Florin Dobre"]

        for _ in range(nr):
            id_dis = random.randint(1, 99999)
            nume_dis = random.choice(disciplina)
            profesor_dis = random.choice(profesori)
            self.__repo.adauga_disciplina(Discipline(id_dis, nume_dis, profesor_dis))

    # LIST-ACITVE ------------------------------------------------------------------------------------------------------
    def get_all_dis(self):
        return self.__repo.get_all()

    # ALL-LIST ---------------------------------------------------------------------------------------------------------
    def get_all_all_dis(self):
        #Toata lista, inclusiv si cele sterse
        return self.__repo.get_all_all()

