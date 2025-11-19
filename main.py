from service.srv_student import service_student
from service.srv_discipline import service_iscipline
from service.srv_note import ServiceNote

from repository.repository_studenti import RepoStudent
from repository.repository_discipline import RepoDiscipline
from repository.repo_note import RepoNote

from validation.validator_studenti import StudentValidator
from validation.disciplina_validator import DisciplinaValidator
from validation.nota_validator import NotaValidator

repo_s = RepoStudent()
repo_d = RepoDiscipline()
repo_n = RepoNote()

val_s = StudentValidator()
val_d = DisciplinaValidator()
val_n = NotaValidator()

srv_studenti = ServiceStudenti(repo_s, val_s)
srv_discipline = ServiceDiscipline(repo_d, val_d)
srv_note = ServiceNote(repo_n, repo_s, repo_d, val_n)

# UI
run_main = Console(srv_studenti, srv_discipline, srv_note)
run_main.run()
