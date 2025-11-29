from pickletools import read_int4

from Error.Repo_Error import RepoError
from domain.disciplina import Discipline

class RepoDiscipline:
    def __init__(self, calea_fiser):
        self.__discipline = {}
        self.__calea_fiser = calea_fiser
        self.__citeste()


    # I/O

    def __citeste(self):
        self.__discipline = {}

        try:
            with open(self.__calea_fiser, 'r', encoding='utf-8') as fiser:
                for linie in fiser:
                    linie = linie.strip()
                    if linie == '':
                        continue
                    parts = linie.split(',')
                    if len(parts) >= 4:
                        id_discipline = int(parts[0])
                        nume = parts[1]
                        prof = parts[2]
                        active = parts[3]

                        dis = Discipline(id_discipline, nume, prof)

                        if active == "False":
                            dis.deactivate()

                        self.__discipline[id_discipline] = dis
        except FileNotFoundError:
            self.__discipline = {}

    def __scrie(self):
        with open(self.__calea_fiser, 'w', encoding='utf-8') as fiser:
            for d in self.__discipline.values():
                linie = f"{d.get_id_disciplina()},{d.get_nume_disciplina()},{d.get_profesor()},{d.is_active()}\n"
                fiser.write(linie)


    # ADD --------------------------------------------------------------------------------------------------------------
    def adauga_disciplina(self, disciplina):
        """
        Adauga o disciplina pe baza unui 'id', iar daca 'id' este folosit arunca "ID disciplina deja existent!"
        :param disciplina: Disciplina
        :return: -
        """

        if disciplina in self.__discipline:
            raise RepoError("Id disciplina deja existent!")
        self.__discipline[disciplina.get_id_disciplina()] = disciplina
        self.__scrie()

    # DEL --------------------------------------------------------------------------------------------------------------
    def sterge_disciplina(self, id_disciplina):
        """
        Sterge
        :param id_disciplina: numar intreg, pozitiv
        :return: -
        """
        self.__citeste()

        if not self.__discipline[id_disciplina].is_active():
            raise RepoError("Disciplina inexistenta sau deja stearsa!")

        if id_disciplina in self.__discipline and self.__discipline[id_disciplina].is_active():
            self.__discipline[id_disciplina].deactivate()
        self.__scrie()


    # UPDATE -----------------------------------------------------------------------------------------------------------
    def modifica_disciplina(self, disciplina_nou):
        """
        Modifica numele disciplinei si numele profesorului
        :param disciplina_nou: disciplina noua
        :return: -
        """

        self.__citeste()


        id_disciplina = disciplina_nou.get_id_disciplina()
        if id_disciplina not in self.__discipline:
            raise RepoError("Disciplina inexistenta!")
        dis = self.__discipline[id_disciplina]
        if not dis.is_active():
            raise RepoError("Disciplina stearsa!")
        dis.set_profesor(disciplina_nou.get_profesor())
        dis.set_nume_disciplina(disciplina_nou.get_nume_disciplina())
        self.__scrie()


    # FIND -------------------------------------------------------------------------------------------------------------
    def cauta(self, id_disciplina):
        """
        Cauta o disciplina pe baza unui id
        :param id_disciplina: numar intreg, pozitiv
        :return: disciplina
        """
        self.__citeste()
        if id_disciplina in self.__discipline:
            dis = self.__discipline[id_disciplina]
            if dis.is_active():
                return dis
        raise RepoError("Disciplina inexistenta sau deja stearsa!")



    # LIST-ACTIVE ------------------------------------------------------------------------------------------------------
    def get_all(self):
        self.__citeste()
        return [d for d in self.__discipline.values() if d.is_active()]

    # LIST-ALL ---------------------------------------------------------------------------------------------------------
    def get_all_all(self):
        self.__citeste()
        return list(self.__discipline.values())





