from repository.repository_studenti import RepoStudent
from validation.validator_studenti import StudentValidator
from service.srv_student import service_student

repo = RepoStudent()
validator = StudentValidator()
service = service_student(repo, validator)

service.generare(10)

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
