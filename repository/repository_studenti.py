
from Error.Repo_Error import RepoError
from domain.studenti import Student


class RepoStudent:
    """
        Repository Student
        Stocam datele studentilor intr un fiser text
    """
    def __init__(self, cale_fiser):
        self.__cale_fiser = cale_fiser
        self.__studenti = {}
        self.__citeste()


    # I/O


    def __citeste(self):
        self.__studenti = {}
        try:
            with open(self.__cale_fiser, "r", encoding="utf-8") as fiser:
                for linie in fiser:
                    linie = linie.strip()
                    if linie == "":
                        continue
                    parts = linie.split(",")
                    if len(parts) >=  3:
                        id_student = int (parts[0])
                        nume = parts[1]
                        active = parts[2]
                        student = Student(id_student, nume)
                        if active == "False":
                            student.deactivate()

                        self.__studenti[id_student] = student
        except FileNotFoundError:
            self.__studenti = {}

    def __scrie(self):
        with open(self.__cale_fiser, "w", encoding="utf-8") as fiser:
            for s in self.__studenti.values():
                linie = f"{s.get_id_student()},{s.get_nume_student()},{s.is_active()}\n"
                fiser.write(linie)


    # ADD --------------------------------------------------------------------------------------------------------------
    def adauga_student(self, student):
        """
        Adauga un student pe baza unui 'id' , iar daca 'id' este folosit arunca eroarea "Id student existent"

        :param student: Student
        :return: -
        """
        self.__citeste()

        if student.get_id_student() in self.__studenti and student.is_active():
            raise RepoError("Id student existent!")
        self.__studenti[student.get_id_student()] = student
        self.__scrie()



    # DEL --------------------------------------------------------------------------------------------------------------
    def sterge_student(self, id_student):
        """
        Sterge logic un student: marcheaza studentul ca inactiv (active = False)

        :param id_student: numar intreg, pozitiv
        :return: -
        """

        self.__citeste()


        if id_student not in self.__studenti:
         raise RepoError("Id student nu exista!")

        student = self.__studenti[id_student]

        if not student.is_active():
            raise RepoError("Id student nu sters!")

        student.deactivate()
        self.__scrie()

    # UPDATE -----------------------------------------------------------------------------------------------------------

    def modifica_student(self, student_nou):
        """
         Modifica numele stundetului (daca este activ = True)

        :param student_nou: student
        :return:
        """
        self.__citeste()

        id_cautat = student_nou.get_id_student()

        if id_cautat not in self.__studenti:
            raise RepoError("Studentu nu exista!")

        student = self.__studenti[id_cautat]

        if not student.is_active():
            raise RepoError("Studentul este sters!")

        student.set_nume_student(student_nou.get_nume_student())
        self.__scrie()

    # FIND -------------------------------------------------------------------------------------------------------------

    def cauta_student(self, id_student):
        """
        Cauta student

        :param id_student: numar intreg, pozitiv
        :return:
        """

        self.__citeste()

        lista_curenta = list(self.__studenti.values())
        return self.__cauta_rec(lista_curenta, id_student)


    def __cauta_rec(self, id_student, lista):

        if not lista:
            raise RepoError("Student nu exista sau este sters!")

        student_curent = lista[0]


        if student_curent.get_id_student() == id_student:
            if student_curent.is_active():
                return student_curent
            else:
                raise RepoError("Student nu exista sau este sters!")

        return self.__cauta_rec(id_student, lista[1: ])



    # ALL-LIST-ACTIVE --------------------------------------------------------------------------------------------------

    def get_all(self):
        self.__citeste()
        return [s for s in self.__studenti.values() if s.is_active()]

    # ALL-LIST ---------------------------------------------------------------------------------------------------------

    def get_all_all(self):
        self.__citeste()
        return list(self.__studenti.values())

    # DEL-LIST ---------------------------------------------------------------------------------------------------------

    def sterge_tot(self):
        self.__citeste()

        for student in self.__studenti.values():
            student.deactivate()

        self.__scrie()



