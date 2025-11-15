class Note:
    def __init__(self):
        self.__note = []

    def add_note(self, nota):
        self.__note.append(nota)

    def get_all_note(self):
        return self.__note[:]
