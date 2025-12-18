from domain.note import Note
import random
from Error.Srv_note import ErrorSN


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

    # GEN --------------------------------------------------------------------------------------------------------------

    def generare(self, nr):
        """
        Genereaza note
        :param nr:
        :return:
        """
        studenti = self.__repo_studenti.get_all()
        if not studenti:
            raise ErrorSN("Nu sunt studenti pentru a generea")
        disciplina = self.__repo_discipline.get_all()
        if not disciplina:
            raise ErrorSN("Nu sunt discipline pentru a generea")

        for _ in range(nr):
            student_rand = random.choice(studenti)
            disciplina_rand = random.choice(disciplina)

            id_student = student_rand.get_id_student()
            id_diciplina = disciplina_rand.get_id_disciplina()
            val_nota = random.randint(1, 10)

            nota = Note(id_student, id_diciplina, val_nota)

            self.__validator.valideaza_nota(nota)
            self.__repo_note.adauga_note(nota)

    # DEL-LIST ---------------------------------------------------------------------------------------------------------

    def golire_lista_note(self):
        self.__repo_note.sterge_tot()

    # STATISTICS -------------------------------------------------------------------------------------------------------

    def sortare_stud_dis(self, id_disciplina):
        rezultat = []

        _ = self.__repo_discipline.cauta(id_disciplina)

        for note in self.__repo_note.get_all_note():
            if note.get_disciplina() == id_disciplina:
                student = self.__repo_studenti.cauta_student(note.get_student())
                nume = student.get_nume_student()
                valoare = note.get_nota()
                rezultat.append((nume, valoare))

        rezultat.sort(key = lambda x : (x[0].lower(), -x[1]))

        return [f"{nume} | Nota: {nota}" for nume, nota in rezultat]

    def statistica_top20(self):
        """
        Returneaza top 20% studenti dupa media notelor lor.
        Format:
            Nume Student | Media: X.Y
        """


        note_student = {}

        for nota in self.__repo_note.get_all_note():
            id_stud = nota.get_student()
            valoare = nota.get_nota()

            if id_stud not in note_student:
                note_student[id_stud] = []

            note_student[id_stud].append(valoare)


        if not note_student:
            return []


        medii = []
        for id_stud, lista_note in note_student.items():
            student = self.__repo_studenti.cauta_student(id_stud)
            nume = student.get_nume_student()

            media = sum(lista_note) / len(lista_note)

            medii.append((nume, media))

        medii.sort(key=lambda x: -x[1])


        nr_total = len(medii)
        nr_top = max(1, nr_total * 20 // 100)

        top = medii[:nr_top]

        return [f"{nume} | Media: {round(media, 2)}" for nume, media in top]


    def lista_stud_med_mai_mare_5(self):
        def statistica_top20(self):

            note_student = {}

            for nota in self.__repo_note.get_all_note():
                id_stud = nota.get_student()
                valoare = nota.get_nota()

                if id_stud not in note_student:
                    note_student[id_stud] = []

                note_student[id_stud].append(valoare)

            if not note_student:
                return []

            medii = []
            for id_stud, lista_note in note_student.items():
                student = self.__repo_studenti.cauta_student(id_stud)
                nume = student.get_nume_student()

                media = sum(lista_note) / len(lista_note)

                if media > 5:
                    medii.append((nume, media))

            return [f"{nume} | Media: {round(media, 2)}" for nume, media in medii]


    def sortare(self):
        rez = []
        for note in self.__repo_note.get_all_note():


            id_stud = note.get_student()
            dis = note.get_disciplina()
            valoare = note.get_nota()

            rez.append((id_stud, dis, valoare))

        rez.sort(key = lambda x : (x[0].lower(), x[1].lower()))

        return rez