class Discipline:
    def __init__(self, id_disciplina, nume_disciplina, profesor):
        # self.id_disciplina = id_disciplina
        # self.nume_disciplina = nume_disciplina
        # self.profesor = profesor
        self.__disciplina_data = {
            "id_disciplina": id_disciplina,
            "nume_disciplina": nume_disciplina,
            "profesor": profesor
        }
    def get_id_disciplina(self):
        return self.__disciplina_data["id_disciplina"]

    def get_nume_disciplina(self):
        return self.__disciplina_data["nume_disciplina"]

    def get_profesor(self):
        return self.__disciplina_data["profesor"]

    def set_nume_disciplina(self, nume_disciplina_nou):
        self.nume_disciplina["nume_disciplina"] = nume_disciplina_nou

    def set_profesor(self, profesor_nou):
        self.__disciplina_data['profesor'] = profesor_nou

    def __str__(self):
        return f"Id: {self.__disciplina_data["id_disciplina"]} \nNume: {self.__disciplina_data["nume_disciplina"]} \nProfesor: {self.__disciplina_data['profesor']}"
