
class Note:
    def __init__(self, student, disciplina, nota_stud):
        self.__student = student
        self.__disciplina = disciplina
        self.__nota_stud = nota_stud

    def get_student(self):
        return self.__student

    def get_disciplina(self):
        return self.__disciplina

    def get_nota_stud(self):
        return self.__nota_stud

    def __str__(self):
        return f"{self.__student} {self.__disciplina} {self.__nota_stud}"


