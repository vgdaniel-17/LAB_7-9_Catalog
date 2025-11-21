from pickletools import read_int4

from Error.Repo_Error import RepoError
from domain.disciplina import Discipline

class RepoDiscipline:
    def __init__(self):
        self.__discipline = []


    # ADD --------------------------------------------------------------------------------------------------------------
    def adauga_disciplina(self, disciplina):
        """
        Adauga o disciplina pe baza unui 'id', iar daca 'id' este folosit arunca "ID disciplina deja existent!"
        :param disciplina: Disciplina
        :return: -
        """

        for d in self.__discipline:
            if d.get_id_disciplina == disciplina.get_id_disciplina():
                raise RepoError("Id disciplina deja existent!")
        self.__discipline.append(disciplina)

    # DEL --------------------------------------------------------------------------------------------------------------
    def sterge_disciplina(self, id_disciplina):
        """
        Sterge
        :param id_disciplina: numar intreg, pozitiv
        :return: -
        """
        for d in self.__discipline:
            if d.get_id_disciplina() == id_disciplina and d.active:
                d.deactivate()
                return
        raise RepoError("Disciplina inexistenta sau deja stearsa!")

    # UPDATE -----------------------------------------------------------------------------------------------------------
    def modifica_disciplina(self, disciplina_nou):
        """
        Modifica numele disciplinei si numele profesorului
        :param disciplina_nou: disciplina noua
        :return: -
        """
        for d in self.__discipline:
            if d.get_id_disciplina() == disciplina_nou.get_id_disciplina() and d.is_active():
                d.set_nume_disciplina(disciplina_nou.get_nume_disciplina())
                d.set_profesor(disciplina_nou.get_profesor())
                return
        raise RepoError("Disciplina inexistenta sau deja stearsa!")

    # FIND -------------------------------------------------------------------------------------------------------------
    def cauta(self, id_disciplina):
        """
        Cauta o disciplina pe baza unui id
        :param id_disciplina: numar intreg, pozitiv
        :return: disciplina
        """
        for d in self.__discipline:
            if d.get_id_disciplina() == id_disciplina and d.active:
                return d
        raise RepoError("Disciplina inexistenta sau deja stearsa!")



    # LIST-ACTIVE ------------------------------------------------------------------------------------------------------
    def get_all(self):
        return [d for d in self.__discipline if d.is_active()]

    # LIST-ALL ---------------------------------------------------------------------------------------------------------
    def get_all_all(self):
        return self.__discipline[:]





