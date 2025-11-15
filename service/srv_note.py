from domain.note import Note


class Service_Note:
    def __init__(self, repo_note, validator_note, repo_studenti, repo_discipline):
        self.__repo_note = repo_note
        self.__validator = validator_note
        self.__repo_studenti = repo_studenti
        self.__repo_discipline = repo_discipline

    def adauga_note(self, id_student, id_diciplina, nota):
        student = self.__repo_studenti.cauta(id_student)
        disciplina = self.__repo_discipline.cauta(id_diciplina)

        nota = Note(student, disciplina, nota)
        self.__validator.valideaza(nota)
        self.__repo_note.adauga_note(nota)

    def get_all_note(self):
        return self.__repo_note.get_all_note()

    #Statistica

    def lista_ordoanta_dupa_note(self, id_disciplina):
        rezultat = []
        for note in self.__repo_note.get_all_note():
            if note.get.disciplina().get_id == id_disciplina:
                rezultat.append((note.get_student(), note.get_valoare()))
        return rezultat

    def studenti_ordonati_dupa_nume(self):
        pass

