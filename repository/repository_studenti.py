from Error.Repo_Error import RepoError
from domain.studenti import Student


class RepoStudent:
    """
        Repository Student
        Stocam intr-o lista datele studentilor
    """
    def __init__(self):
        self.__studenti = []


    # ADD --------------------------------------------------------------------------------------------------------------
    def adauga_student(self, student):
        """
        Adauga un student pe baza unui 'id' , iar daca 'id' este folosit arunca eroarea "Id student existent"

        :param student: Student
        :return: -
        """

        for stu in self.__studenti:
            if stu.get_id_student() == student.get_id_student():
                raise RepoError("Id student existent!")
        self.__studenti.append(student)


    # DEL --------------------------------------------------------------------------------------------------------------
    def sterge_student(self, id_student):
        """
        Sterge logic un student: marcheaza studentul ca inactiv (active = False)

        :param id_student: numar intreg, pozitiv
        :return: -
        """

        for stu in self.__studenti:
            if stu.get_id_student() == id_student and stu.is_active():
                stu.deactivate()
                return
        raise RepoError("Id student nu exista sau este sters!")

    # UPDATE -----------------------------------------------------------------------------------------------------------

    def modifica_student(self, student_nou):
        """
         Modifica numele stundetului (daca este activ = True)

        :param student_nou: student
        :return:
        """

        for stu in self.__studenti:
            if stu.get_id_student() == student_nou.get_id_student() and stu.is_active():
                stu.set_nume_student(student_nou.get_nume_student())
                return
        raise RepoError("Student nu exista sau este sters!")

    # FIND -------------------------------------------------------------------------------------------------------------

    def cauta_student(self, id_student):
        """
        Cauta student

        :param id_student: numar intreg, pozitiv
        :return:
        """

        for stu in self.__studenti:
            if stu.get_id_student() == id_student and stu.is_active():
                return stu

        raise RepoError("Student nu exista sau este sters!")

    # ALL-LIST-ACTIVE --------------------------------------------------------------------------------------------------

    def get_all(self):
        return [s for s in self.__studenti if s.is_active()]

    # ALL-LIST

    def get_all_all(self):
        return self.__studenti[:]





