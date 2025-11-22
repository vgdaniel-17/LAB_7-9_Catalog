class NotaValidator:
    def valideaza_nota(self, nota):
        if not 0 < nota.get_nota() < 11:
            raise Exception("Nota invalida!")
