import random

from domain.studenti import Student
from repository.repository_studenti import RepoStudent


class service_student:
    def __init__(self, repo_studenti, validator_studenti):
        self.__repo = repo_studenti
        self.__validator = validator_studenti

    # ADD --------------------------------------------------------------------------------------------------------------

    def adauga_student(self, id_student, nume):
        self.__validator.validare_student(id_student, nume)
        self.__repo.adauga_studenti(id_student, nume)

    # DEL --------------------------------------------------------------------------------------------------------------

    def sterge_student(self, id_student, nume):
        self.__validator.validare_student(id_student, nume)
        self.__repo.sterge_student(id_student, nume)

    # UPDATE -----------------------------------------------------------------------------------------------------------

    def modifica_student(self, id_student, nume_nou):
        #Modifica student
        self.__validator.validare_student(id_student, nume_nou)
        student_nou = self.__repo.cauta(id_student)
        student_nou.get_nume_student(nume_nou)

    # FIND -------------------------------------------------------------------------------------------------------------
    def cauta_student(self, id_student):
        """
        Cauta un stundent
        :param id_student:
        :return: stundet activ cu 'id' dat
        """
        return self.__repo.cauta(id_student)

    # GEN --------------------------------------------------------------------------------------------------------------

    def generare(self, nr_studenti):
        """
        Genereaza un numar 'nr_studenti' de stundenti si ii adauga in repo
        :param nr_studenti: numar intreg, pozitiv
        :return:
        """

        prenume = ["Nechifor", "Haralambie", "Sergiuț", "Baptist", "Gherasim", "Titus_Liviu", "Ravel", "Codrinel",
                   "Zotic", "Samson", "Sebald", "Geluț", "Ludovic", "Simeonel", "Timoftei", "Prisilia", "Paraschiva",
                   "Domnica", "Catrina", "Smaranda", "Varvara", "Zenovia", "Agripina", "Gențiana", "Melania_Ruxandra",
                   "Florimonda", "Pulheria", "Sevastiana", "Steluța", "Zinaida"]

        nume = ["Ciubotariu", "Hagiu", "Bârloagă", "Rânjea", "Moțoc", "Făgărășanu", "Papadopol", "Țicleanu", "Zăgan",
                "Cireșar", "Mălăiescu", "Plopeanu", "Urziceanu"]

        for _ in range(nr_studenti):

            id_student = random.randint(123141, 999999)
            nume_nou = random.choice(nume) + " " + random.choice(prenume)
            student_gen = Student(id_student, nume_nou)
            self.__repo.adauga_student(student_gen)

    # ALL-LIST-ACTIVE --------------------------------------------------------------------------------------------------

    def get_all_student_active(self):
        return self.__repo.get_all()

    # ALL-LIST

    def get_all_student(self):
        return self.__repo.get_all_all()