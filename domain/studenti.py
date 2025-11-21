class Student:
    def __init__(self, id_student, nume_student):
        """
        :param id_student: id student, numar intreg
        :param nume_student: nume student, string
        :return: -
        """
        self.__student_data = {
            "id_student": id_student,
            "nume_student": nume_student,
            "active": True

        }

    # GET --------------------------------------------------------------------------------------------------------------

    def get_id_student(self):
        return self.__student_data["id_student"]

    def get_nume_student(self):
        return self.__student_data["nume_student"]

    def is_active(self):
        return self.__student_data["active"]

    # SET --------------------------------------------------------------------------------------------------------------

    def set_nume_student(self, id_stundet, nume_student_nou):
        self.__nume_student["nume_student"] = nume_student_nou

    def deactivate(self):
        self.__student_data["active"] = False

    def __str__(self):
        status = "" if self.__student_data["active"] else " (sters)"
        return f"{self.__student_data['id_student']} | {self.__student_data['nume_student']}{status}"