from repository.repository_discipline import RepoDiscipline

from domain.note import Note

class RepoNote:
    def __init__(self, calea_fiser):
        self.__note = {}
        self.__calea_fiser = calea_fiser
        self.__citeste()


    # I/O --------------------------------------------------------------------------------------------------------------

    def __citeste(self):
        self.__note = {}

        try:
            with open(self.__calea_fiser, "r", encoding="utf-8") as fiser:
                for line in fiser:
                    line = line.strip()
                    if line == "":
                        continue
                    parts = line.split(",")
                    if len(parts) >= 3:
                        id_student_new = parts[0]
                        id_disciplina_new = parts[1]
                        nota_cutenta = parts[2]

                        note_object = Note(id_student_new, id_disciplina_new, nota_cutenta)
                        self.__note[id_student_new] = note_object

        except FileNotFoundError:
            self.__note = {}

    def __scrie(self):
        with open(self.__calea_fiser, "w", encoding="utf-8") as fiser:
            for n in self.__note.values():
                linie = f"{n.get_student()},{n.get_disciplina()},{n.get_nota()}\n"
                fiser.write(linie)



    # ADD --------------------------------------------------------------------------------------------------------------
    def adauga_note(self, nota):
        """
        adauga o note pe baza unui 'id_student', 'id_disciplina' si 'nota_cutenta'
        :param nota: object
        :return:
        """
        self.__note[nota.get_student()] = nota
        self.__scrie()

    # GET --------------------------------------------------------------------------------------------------------------
    def get_all_note(self):
        return list(self.__note.values())

    # DEL-LIST ---------------------------------------------------------------------------------------------------------

    def sterge_tot(self):
        self.__citeste()

        for note in self.__note.values():
            note.deactivate()

        self.__scrie()

