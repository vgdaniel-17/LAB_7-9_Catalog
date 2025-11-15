from domain.disciplina import Discipline

class RepoDiscipline:
    def __init__(self):
        self.__discipline = []

    def addDiscipline(self, disciplina):
        self.__discipline.append(disciplina)
    def getAllDiscipline(self):
        return self.__discipline


