

class Console:
    def __init__(self,service_studenti,service_materii,service_note):
        self.__service_studenti = service_studenti
        self.__service_materii = service_materii
        self.__service_note = service_note
        self.__comenzi = {
            "adauga_studenti":self.__ui_adauga_student(),
            "sterge_studenti":self.__ui.sterge_student(),
            "modifica_studenti":self.__ui.modifica_student(),
            "lista_studenti":self.__ui.lista_student(),
            "lista_discipline":self.__ui.lista_discipline(),
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
        print("0 -> iesire: <exit> sau  <0>")
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
            nume_coxmanda = parti_comanda[0]
            parametri_comanda = parti_comanda[1:]
            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda](parametri_comanda)
                except UiError as eroare_ui:
                    print(f"Eroare ui: {eroare_ui}")
            else:
                print(f"Comanda {text_comanda} nu exista!")
