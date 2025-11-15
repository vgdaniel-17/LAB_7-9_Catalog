class Studenti:
    def __init__(self, id_student, nume_student):
        """
        :param id_student: id student, numar intreg
        :param nume_student: nume student, string
        :return:
        """
        # self.__id_student = id_student
        # self.__nume_student = nume_student
        self.__student_data = {
            "id_student": id_student,
            "nume_student": nume_student

        }

    def get_id_student(self):
        return self.__student_data["id_student"]

    def get_nume_student(self):
        return self.__student_data["nume_student"]

    def set_nume_student(self, nume_student_nou):
        self.__nume_student["nume_student"] = nume_student_nou

    def __str__(self):
        return f"Id: {self.__student_data["id_student"]} -> Nume:{self.__student_data["nume_student"]}"