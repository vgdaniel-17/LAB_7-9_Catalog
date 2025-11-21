from Error.Srv_stud import ErrorSS

class StudentValidator:
    def validare_student(self, id_student, nume):
        errors = []

        if id_student < 0:
            errors.append("Id nu este valid")
        if not nume or nume.strip() == "":
            errors.append("Numele nu este valid")

        if errors:
            raise ErrorSS(errors)

    def validare_id(self, id_student):
        errors = []
        if id_student < 0:
            errors.append("Id nu este valid")

        if errors:
            raise ErrorSS(errors)
