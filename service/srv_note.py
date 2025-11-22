from domain.note import Note


class Service_Note:
    def __init__(self, repo_note, repo_studenti, repo_discipline, validator_note):
        self.__repo_note = repo_note
        self.__validator = validator_note
        self.__repo_studenti = repo_studenti
        self.__repo_discipline = repo_discipline

    # ADD --------------------------------------------------------------------------------------------------------------
    def adauga_note(self, id_student, id_diciplina, nota):
        """
        Adauga o nota pe baza unui 'id_studenti' si 'id_diciplina'
        :param id_student:
        :param id_diciplina:
        :param nota:
        :return:
        """

        _ = self.__repo_studenti.cauta_student(id_student)
        _ = self.__repo_discipline.cauta(id_diciplina)

        new_nota = Note(id_student, id_diciplina, nota)
        self.__validator.valideaza_nota(new_nota)
        self.__repo_note.adauga_note(new_nota)


    # LIST NOTE --------------------------------------------------------------------------------------------------------

    def list_note(self, id_student):
        rezultat = []

        for nota in self.__repo_note.get_all_note():
            if nota.get_student() == id_student:
                disciplina = self.__repo_discipline.cauta(nota.get_disciplina())
                linie = f"Disciplina: {disciplina.get_nume_disciplina()} | Nota: {nota.get_nota()}"
                rezultat.append(linie)
        return rezultat



    #Statistica

    def lista_ordoanta_dupa_note(self, id_disciplina):
        rezultat = []
        for note in self.__repo_note.get_all_note():
            if note.get.disciplina().get_id == id_disciplina:
                rezultat.append((note.get_student(), note.get_valoare()))
        return rezultat

    def studenti_ordonati_dupa_nume(self):
        pass

