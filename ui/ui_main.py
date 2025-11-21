from Error.UiError import *
from domain.studenti import Student
from service import srv_discipline


class Console:
    def __init__(self, srv_studenti, srv_discipline, srv_note):
        self.__service_student = srv_studenti
        self.__service_materi = srv_discipline
        self.__service_note = srv_note
        self.__comenzi = {
            #studenti
            "add_stud": self.ui_add_stud(), #
            "del_stud": self.ui_del_stud(), #
            "mod_stud": self.ui_mod_stud(), #
            "list_stud": self.ui_list_stud(),#
            "caut_stud": self.ui_caut_stud(),#
            "gen": self.ui_gen_stud(), #

            #discipline

            "add_dis": self.ui_add_dis(),

        }

    def ui_help(self):
        print("""
        =========================== AJUTOR COMENZI ===========================
         Comenzi pentru gestionarea STUDENTILOR:
           add_stud <id> <nume>            - Adauga un student nou
           del_stud <id>                   - Sterge logic un student
           mod_stud <id> <nume_nou>        - Modifica numele unui student
           list_stud                       - Afiseaza toti studentii activi
           caut_stud <id>                  - Cauta un student dupa ID
           gen <nr>                        - Genereaza automat studenti
    
         Comenzi pentru gestionarea DISCIPLINELOR:
           add_dis <id> <nume> <prof>      - Adauga o disciplina
           del_dis <id>                    - Sterge o disciplina
           mod_dis <id> <nume> <prof>      - Modifica o disciplina
           list_dis                        - Afiseaza toate disciplinele
           caut_dis <id>                   - Cauta o disciplina dupa ID
    
         Comenzi pentru NOTE:
           add_note <id_student> <id_disciplina> <nota>   - Adauga o nota
           list_note                       - Afiseaza toate notele
    
         STATISTICI:
           stat1 <id_disciplina>           - Lista studenti + note la disciplina data
           stat2                           - Primii 20% studenti dupa media generala
    
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
        if len(parametri_comanda) != 3:
            raise EroareUI("Ai introdus prea un numar invalid de paramteri. Trebuie 2!")
        try:
            id_student = int(parametri_comanda[0])
        except ValueError:
            raise EroareUI("id numeric invalid!")
        nume_student = parametri_comanda[1]
        self.__service_student.adauga_student = Student(id_student, nume_student)
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

    def ui_list_stud(self):
        list_stud = self.__service_student.get_all()
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
            raise EroareUI("Nr studenti trebuie sa fie numar!")

        self.__service_student.gen_student(numar)
        print("Studenti generati cu succes!")


    # DISCIPLINE -------------------------------------------------------------------------------------------------------

    def ui_add_dis(self, parametri_comanda):
        if len(parametri_comanda) != 3:
            print("Trebuie doar <id_disciplina> <nota> <prof>!")
        try:
            id_disciplina = int(parametri_comanda[0])
        except ValueError:
            raise EroareUI("id numeric invalid!")
        try:
            nota = int(parametri_comanda[1])
        except ValueError:
            raise EroareUI("nota invalida!")












#
# ui = Console(srv_studenti, srv_discipline, srv_note)
# ui.run()
# ui.run()