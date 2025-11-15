from domain import studenti
from domain.studenti import Studenti

class RepoStudent:
    def __init__(self):
        self.__studenti = []

    def addStudent(self, student):
        self.__studenti.append(student)

    def getAll(self):
        return self.__studenti



