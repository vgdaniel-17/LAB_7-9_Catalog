from domain.studenti import Studenti
from Error.Srv_stud_error import ErrorSS

class StudentValidator:
    def validare_student(self, id_student, nume):
        erros = []
        if 0 > id_student:
            erros.append("Id nu este valid")
        if not nume:
            erros.append("Numele nu este valid")

        raise ErrorSS(erros)

