from repository.repository_studenti import RepoStudent
from validation.validator_studenti import StudentValidator
from service.srv_student import service_student

repo = RepoStudent()
validator = StudentValidator()
service = service_student(repo, validator)

service.generare(123)

for s in service.get_all_studenti():
    print(s)
