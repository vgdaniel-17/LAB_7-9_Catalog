import random

from domain.studenti import Studenti
from repository.repository_studenti import RepoStudent


class service_student:
    def __init__(self, repo_studenti, validator_studenti):
        self.__repo = repo_studenti
        self.__validator = validator_studenti

    def adauga_student(self, id_student, nume):
        self.__validator.validare_student(id_student, nume)
        self.__repo.adauga_studenti(id_student, nume)

    def sterge_student(self, id_student, nume):
        self.__validator.validare_student(id_student, nume)
        self.__repo.sterge_student(id_student, nume)

    def modifica_student(self, id_student, nume_nou):
        self.__validator.validare_student(id_student, nume_nou)
        self.__repo.modifica_student(id_student, nume_nou)

    def cauta_student(self, id_student):
        return self.__validator.cauta_student(id_student)

    def generare(self, nr_studenti):
        prenume = ["Nechifor", "Haralambie", "Sergiuț", "Baptist", "Gherasim", "Titus_Liviu", "Ravel", "Codrinel",
                   "Zotic", "Samson", "Sebald", "Geluț", "Ludovic", "Simeonel", "Timoftei", "Prisilia", "Paraschiva",
                   "Domnica", "Catrina", "Smaranda", "Varvara", "Zenovia", "Agripina", "Gențiana", "Melania_Ruxandra",
                   "Florimonda", "Pulheria", "Sevastiana", "Steluța", "Zinaida"]

        nume = ["Ciubotariu", "Hagiu", "Bârloagă", "Rânjea", "Moțoc", "Făgărășanu", "Papadopol", "Țicleanu", "Zăgan",
                "Cireșar", "Mălăiescu", "Plopeanu", "Urziceanu"]

        for _ in range(nr_studenti):

            id_student = random.randint(123141, 999999)
            nume_nou = random.choice(nume) + " " + random.choice(prenume)
            student_gen = Studenti(id_student, nume_nou)
            self.__repo.addStudent(student_gen)


    def get_all_studenti(self):
        return self.__repo.get_all()