from repository.repository_studenti import RepoStudent
from validation.validator_studenti import StudentValidator
from service.srv_student import service_student

cale = r"E:\Coding\Python\LC\LAB_7-9\student.txt"
repo = RepoStudent(cale)
validator = StudentValidator()
service = service_student(repo, validator)

service.generare(1212)

while True:
    ceva = input(">>> ")
    if ceva == "exit":
        break

    if ceva == "1":
        for s in service.get_all_student():
            print(s)

    if ceva == "2":
        id_student = int(input("ID student: "))
        service.sterge_student(id_student)

disciplina = ["Limba si literatura romana", "Matematica", "Limba engleza", "Limba franceza", "Biologie", "Fizica",
              "Chimie", "Istorie", "Geografie", "Educatie civica", "Educatie plastica", "Educatie muzicala",
              "Educatie fizica si sport", "Informatica", "TIC", "Educatie tehnologica", "Consiliere si orientare"]

print(len(disciplina))