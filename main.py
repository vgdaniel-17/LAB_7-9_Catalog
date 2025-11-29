from repository.repository_studenti import RepoStudent
from repository.repository_discipline import RepoDiscipline
from repository.repository_note import RepoNote

from validation.validator_studenti import StudentValidator
from validation.disciplina_validator import DisciplinaValidator
from validation.validator_note import NotaValidator

from service.srv_student import service_student
from service.srv_discipline import Service_Discipline
from service.srv_note import Service_Note

from ui.ui_main import Console


def main():
    # FILE ADDRESS
    cale_student = r"E:\Coding\Python\LC\LAB_7-9\student.txt"
    cale_disciplina = r"E:\Coding\Python\LC\LAB_7-9\disciplina.txt"
    cale_note = r"E:\Coding\Python\LC\LAB_7-9\note.txt"
    # REPOSITORIES
    repo_studenti = RepoStudent(cale_student)
    repo_discipline = RepoDiscipline(cale_disciplina)
    repo_note = RepoNote(cale_note)

    # VALIDATORS
    val_studenti = StudentValidator()
    val_discipline = DisciplinaValidator()
    val_note = NotaValidator()

    # SERVICES
    srv_studenti = service_student(repo_studenti, val_studenti)
    srv_discipline = Service_Discipline(repo_discipline, val_discipline)
    srv_note = Service_Note(repo_note, repo_studenti, repo_discipline, val_note)

    # UI
    consola = Console(srv_studenti, srv_discipline, srv_note)
    consola.run()


if __name__ == "__main__":
    main()
