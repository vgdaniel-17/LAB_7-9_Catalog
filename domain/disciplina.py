class Discipline:
    def __init__(self, id_disciplina, nume_disciplina, profesor):
        """

        :param id_disciplina: string
        :param nume_disciplina: string
        :param profesor: string
        :return: -
        """
        self.__disciplina_data = {
            "id_disciplina": id_disciplina,
            "nume_disciplina": nume_disciplina,
            "profesor": profesor,
            "active" : True
        }

    # GET --------------------------------------------------------------------------------------------------------------

    def get_id_disciplina(self):
        return self.__disciplina_data["id_disciplina"]

    def get_nume_disciplina(self) -> str:
        return self.__disciplina_data["nume_disciplina"]

    def get_profesor(self):
        return self.__disciplina_data["profesor"]

    def is_active(self):
        return self.__disciplina_data["active"]

    # SET --------------------------------------------------------------------------------------------------------------

    def set_nume_disciplina(self, nume_disciplina_nou):
        self.__disciplina_data["nume_disciplina"] = nume_disciplina_nou

    def set_profesor(self, profesor_nou):
        self.__disciplina_data['profesor'] = profesor_nou

    def deactivate(self):
        self.__disciplina_data["active"] = False

    def __str__(self):
        status = "" if self.__disciplina_data['active'] else " (sters)"
        return f"{self.__disciplina_data['id_disciplina']} | {self.__disciplina_data['nume_disciplina']} | {self.__disciplina_data['profesor']}{status}"
