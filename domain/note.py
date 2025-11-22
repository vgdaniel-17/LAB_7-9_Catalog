

class Note:
    def __init__(self, id_student, id_disciplina, nota_stud):
        self.__data_note = {
            "id_student": id_student,
            "id_disciplina": id_disciplina,
            "nota_stud": nota_stud,
        }


    # GET --------------------------------------------------------------------------------------------------------------
    def get_student(self):
        return self.__data_note["id_student"]

    def get_disciplina(self):
        return self.__data_note["id_disciplina"]

    def get_nota(self):
        return self.__data_note["nota_stud"]

    def get_all(self):
        return self.__data_note

    def __str__(self):
        return f"{self.__data_note['id_student']} {self.__data_note['id_disciplina']} {self.__data_note['nota_stud']}"


