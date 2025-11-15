from Error.UiError import *
from domain.studenti import Studenti
from service import srv_discipline


class Console:
    def __init__(self,srv_studenti, srv_discipline, srv_note):
        self.__service_studenti = srv_studenti
        self.__service_materii = srv_discipline
        self.__service_note = srv_note
        self.__comenzi = {
            "adauga_studenti":self.__ui_adauga_student(),
            "sterge_studenti":self.__ui.sterge_student(),
            "modifica_studenti":self.__ui.modifica_student(),
            "lista_studenti":self.__ui.lista_student(),
            "lista_discipline":self.__ui.lista_discipline(),
            "afisare":self.__ui.afisare(),
            }


    def ui_meniu_principal(self):
        print("----------------------- MENIU PRINCIPAL ------------------------")
        print("1 -> adauga studenti: add_stud <id_student> <nume_student>")
        print("2 -> sterge studenti: del_stud <id_student> <nume_student>")
        print("3 -> modifica_studenti: mod_stud <id_student> <nume_student>")
        print("4 -> lista_studenti: list_stud")
        print("5 -> lista_discipline: list_dis")
        print("6 -> cautare_student: cautare <id_student> sau <nume_student>")
        print("7 -> cautare_disciplina: cautare <disciplina>")
        print("8 -> adaugare_note: add_note <id_student> <disciplina> <nota>")
        print("9 -> afisare: afisare")
        print("0 -> iesire: <exit>")
        print("-----------------------------------------------------------------")

    def run(self):
        self.ui_meniu_principal()
        while(True):
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

    def ui_adauga_student(self, parametri_comanda):
        if len(parametri_comanda) != 3:
            raise EroareUI("Ai introdus prea un numar invalid de paramteri. Trebuie 2!")
        try:
            id_student = int(parametri_comanda[0])
        except ValueError:
            raise EroareUI("id numeric invalid!")
        nume_student = parametri_comanda[1]
        self.__service_studenti.adauga_studenti = Studenti(id_student, nume_student)
        print("Student adaugat cu succes!")

    def ui_afisare(self):
        return self.__service_studenti.get_all_studenti()
    
#
# ui = Console(srv_studenti, srv_discipline, srv_note)
# ui.run()
# ui.run()