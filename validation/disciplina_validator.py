from Error.Srv_dis import ErrorSD

class DisciplinaValidator:
    def validare_disciplina(self, id_disciplina, nume, profesor):
        errors = []
        if id_disciplina < 0:
            errors.append("Id nu este valid")
        if not nume or nume.strip() == "":
            errors.append("Numele nu este valid")
        if not  profesor or profesor.strip() == "":
            errors.append("Profesorul nu este valid")

        if errors:
            raise ErrorSD(errors)

    def id(self, id_disciplina):
        if id_disciplina < 0:
            raise ErrorSD("Id nu este valid")

    def profesor(self, profesor):
        if not profesor or profesor.strip() == "":
            raise ErrorSD("Profesorul nu este valid")

    def disciplina(self, disciplina):
        if not disciplina or disciplina.strip() == "":
            raise ErrorSD("Disciplina nu este valid")

