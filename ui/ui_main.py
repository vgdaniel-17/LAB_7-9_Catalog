from os import times_result

from Error.UiError import *



class Console:
    def __init__(self, srv_studenti, srv_discipline, srv_note):
        self.__service_student = srv_studenti
        self.__service_discipline = srv_discipline
        self.__service_note = srv_note
        self.__comenzi = {
            #studenti
            "add_stud": self.ui_add_stud,
            "del_stud": self.ui_del_stud,
            "mod_stud": self.ui_mod_stud,
            "list_stud": self.ui_list_stud,
            "caut_stud": self.ui_caut_stud,
            "gen_stud": self.ui_gen_stud,
            "gol_list_stud": self.ui_gol_lista_stud,

            #discipline
            "add_dis": self.ui_add_dis,
            "del_dis": self.ui_del_dis,
            "mod_dis": self.ui_mod_dis,
            "list_dis": self.ui_list_dis,
            "caut_dis": self.ui_caut_dis,
            "gen_dis" : self.ui_gen_dis,
            "gol_list_dis": self.ui_gol_lista_dis,

            #note
            "add_note": self.ui_add_note,
            "list_note": self.ui_list_note,
            "gen_note": self.ui_gen_note,
            "gol_list_note": self.ui_gol_lista_note,

            #statistici
            "stat1": self.ui_stat1,
            "stat2": self.ui_stat2,
            "stat3": self.ui_stat3,



            "help":self.ui_help,
        }

    def ui_help(self, params=None):
        print("""
        =========================== AJUTOR COMENZI ===========================
         Comenzi pentru gestionarea STUDENTILOR:
           add_stud <id> <nume>            - Adauga un student nou
           del_stud <id>                   - Sterge logic un student
           mod_stud <id> <nume_nou>        - Modifica numele unui student
           list_stud                       - Afiseaza toti studentii activi
           caut_stud <id>                  - Cauta un student dupa ID
           gen_stud <nr>                   - Genereaza automat studenti
           gol_list_stud                   - Goleste lista de studenti

         Comenzi pentru gestionarea DISCIPLINELOR:
           add_dis <id> <nume> <prof>      - Adauga o disciplina
           del_dis <id>                    - Sterge o disciplina
           mod_dis <id> <nume> <prof>      - Modifica o disciplina
           list_dis                        - Afiseaza toate disciplinele
           caut_dis <id>                   - Cauta o disciplina dupa ID
           gen_dis <nr>                    - Genereaza automat discipline
           gol_list_dis                    - Goleste lista de discipline

         Comenzi pentru NOTE:
           add_note <id_student> <id_disciplina> <nota>   - Adauga o nota
           list_note <id_student>          - Afiseaza toate notele unui student
           gen_note <nr>                   - Genereaza automat notele 
           gol_list_note                   - Goleste lista de note

         STATISTICI:
           stat1 <id_disciplina>           - Lista studenti + note la disciplina data
           stat2                           - Primii 20% studenti dupa media generala
           stat3                           - Studenti cu media mai mare decat 5

         ALTE COMENZI:
           help                            - Afiseaza acest meniu
           exit                            - Inchide aplicatia
        ======================================================================
        """)

    def run(self):
        print("Pentru a accesa comenzile <help>")
        while (True):
            text_comanda = input(">>>").strip()
            if text_comanda == "":
                continue
            if text_comanda == "exit" or text_comanda == "0":
                break

            parti_comanda = text_comanda.split()
            nume_comanda = parti_comanda[0]
            parametri_comanda = parti_comanda[1:]
            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda](parametri_comanda)
                except EroareUI as eroare_ui:
                    print(f"Eroare ui: {eroare_ui}")
            else:
                print(f"Comanda {text_comanda} nu exista!")

    # STUDENTI ---------------------------------------------------------------------------------------------------------

    def ui_add_stud(self, parametri_comanda):
        # if len(parametri_comanda) != 2:
        #     raise EroareUI("Ai introdus prea un numar invalid de paramteri. Trebuie 2!")
        try:
            id_student = int(parametri_comanda[0])
        except ValueError:
            raise EroareUI("id numeric invalid!")
        nume_student = " ".join(parametri_comanda[1:])
        self.__service_student.adauga_student(id_student, nume_student)
        print("Student adaugat cu succes!")

    def ui_del_stud(self, parametri_comanda):
        if len(parametri_comanda) != 1:
            raise EroareUI("Trebuie doar id-ul!")
        try:
            id_student = int(parametri_comanda[0])
        except ValueError:
            raise EroareUI("id numeric invalid!")

        self.__service_student.sterge_student(id_student)
        print("Student sters cu succes!")

    def ui_mod_stud(self, parametri_comanda):
        if len (parametri_comanda) != 2:
            raise EroareUI("Trebuie doar id-ul si numele nou!")
        try:
            id_student = int(parametri_comanda[0])
        except ValueError:
            raise EroareUI("id numeric invalid!")
        nume_student = parametri_comanda[1]
        self.__service_student.modifica_student(id_student, nume_student)
        print("Student modificat cu succes!")

    def ui_list_stud(self, parametri_comanda=None):
        list_stud = self.__service_student.get_all_student_active()
        if not list_stud:
            raise EroareUI("Nu exista studenti!")

        for s in list_stud:
            print(s)

    def ui_caut_stud(self, parametri_comanda):
        if len(parametri_comanda) != 1:
            print("Trebuie doar id-ul!")
        try:
            id_student = int(parametri_comanda[0])
        except ValueError:
            raise EroareUI("id numeric invalid!")

        print(self.__service_student.cauta_student(id_student))


    def ui_gen_stud(self, parametri_comanda):
        if len(parametri_comanda) != 1:
            print("Trebuie doar un numar!")
        try:
            numar = int(parametri_comanda[0])
        except ValueError:
            raise EroareUI("Nr studenti trebuie sa fie numar pozitiv!")

        self.__service_student.generare(numar)
        print("Studenti generati cu succes!")

    def ui_gol_lista_stud(self, parametri_comanda):
        self.__service_student.golire_lista_student()
        print("Lista de studenti a fost stearsa cu succes!")

    # DISCIPLINE -------------------------------------------------------------------------------------------------------

    def ui_add_dis(self, parametri_comanda):
        if len(parametri_comanda) != 3:
            print("Trebuie doar <id_disciplina> <nota> <prof>!")
        try:
            id_disciplina = int(parametri_comanda[0])
        except ValueError:
            raise EroareUI("id numeric invalid!")

        nume = parametri_comanda[1]
        profesor = " ".join(parametri_comanda[2:])

        self.__service_discipline.adauga_disciplina(id_disciplina, nume, profesor)
        print("Disciplina adaugata cu succes!")

    def ui_del_dis(self, parametri_comanda):
        if len(parametri_comanda) != 1:
            print("Trebuie doar id-ul!")
        try:
            id_disciplina = int(parametri_comanda[0])
        except ValueError:
            raise EroareUI("id numeric invalid!")
        self.__service_discipline.sterge_disciplina(id_disciplina)

    def ui_mod_dis(self, parametri_comanda):
        if len(parametri_comanda) != 3:
            print("Trebuie doar <id_disciplina> <nota> <prof>!")
        try:
            id_disciplina = int(parametri_comanda[0])
        except ValueError:
            raise EroareUI("id numeric invalid!")
        nume = parametri_comanda[1]
        profesor = " ".join(parametri_comanda[2:])
        self.__service_discipline.modifica_disciplina(id_disciplina, nume, profesor)
        print("Disciplina modificata!")

    def ui_list_dis(self, parametri_comanda=None):
        list_dis = self.__service_discipline.get_all_dis()
        if not list_dis:
            raise EroareUI("Nu exista discipline!")
        for d in list_dis:
            print(d)

    def ui_caut_dis(self, parametri_comanda):
        if len(parametri_comanda) != 1:
            print("Trebuie doar id-ul!")
        try:
            id_disciplina = int(parametri_comanda[0])
        except ValueError:
            raise EroareUI("id numeric invalid!")
        print(self.__service_discipline.cauta_disciplina(id_disciplina))

    def ui_gen_dis(self, parametri_comanda):
        if len(parametri_comanda) != 1:
            print("Trebuie doar un numar!")
        try:
            numar = int(parametri_comanda[0])
        except ValueError:
            raise EroareUI("Nr de discipline trebuie sa fie numar pozitiv!")

        self.__service_discipline.generare(numar)
        print("Discipline generate cu succes!")

    def ui_gol_lista_dis(self, parametri_comanda):
        self.__service_discipline.golire_lista_dis()
        print("Lista de discipline a fost stearsa cu succes!")

    # NOTE -------------------------------------------------------------------------------------------------------------

    def ui_add_note(self, parametri_comanda):
        if len(parametri_comanda) != 3:
            print("Trebuie doar <id_student> <id_disciplina> <nota>!")
        try:
            id_student = int(parametri_comanda[0])
        except ValueError:
            raise EroareUI("id numeric invalid!")
        try:
            id_disciplina = int(parametri_comanda[1])
        except ValueError:
            raise EroareUI("id numeric invalid!")
        try:
            nota = int(parametri_comanda[2])
        except ValueError:
            raise EroareUI("nota invalid!")
        self.__service_note.adauga_note(id_student, id_disciplina, nota)
        print("Nota adaugata cu succes!")

    def ui_list_note(self, parametri_comanda):
        if len(parametri_comanda) != 2:
            print("Trebuie doar <id_student>!")
        try:
            id_student = int(parametri_comanda[0])
        except ValueError:
            raise EroareUI("id numeric invalid!")
        afisare = self.__service_note.list_note(id_student)

        if not afisare:
            print("Nu sunt note!")

        for s in afisare:
            print(s)

    def ui_gen_note(self, parametri_comanda):
        if len(parametri_comanda) != 1:
            print("Trebuie doar <nr>!")

        try:
            numar = int(parametri_comanda[0])
        except ValueError:
            raise EroareUI("trebuie numar valid!")

        self.__service_note.generare(numar)
        print("Nota generata cu succes!")

    def ui_gol_lista_note(self, parametri_comanda):
        self.__service_note.golire_lista_note()
        print("Lista de note a fost stearsa cu succes!")


    # STATISTICI -------------------------------------------------------------------------------------------------------

    def ui_stat1(self, parametri_comanda):
        if len(parametri_comanda) != 1:
            print("Trebuie doar id-ul disciplinei!")
        try:
            id_disciplina = int(parametri_comanda[0])
        except ValueError:
            raise EroareUI("id numeric invalid!")

        rez = self.__service_note.sortare_stud_dis(id_disciplina)
        for s in rez:
            print(s)

    def ui_stat2(self, params):
        if len(params) != 0:
            raise EroareUI("Comanda corecta: stat2")

        rezultat = self.__service_note.statistica_top20()

        if not rezultat:
            print("Nu exista note in sistem!")
            return

        print("Top 20% studenti dupa media generala:")
        for linie in rezultat:
            print(linie)

    def ui_stat3(self, parametri_comanda):
        if len(parametri_comanda) != 0:
            raise EroareUI("Comanda corecta: stat2")

        rezultat = self.__service_note.statistica_top20()

        if not rezultat:
            print("Nu exista note in sistem!")
            return

        print("Studenti cu media mai mare decact 5:")
        for linie in rezultat:
            print(linie)







#
# ui = Console(srv_studenti, srv_discipline, srv_note)
# ui.run()
# ui.run()