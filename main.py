from domain.dis import Discipline
from repository.repository_discipline import RepoDiscipline

repo = RepoDiscipline()

repo.addDiscipline(Discipline(3123, "mate", "mihii"))

for discipline in repo.getAllDiscipline():
    print(discipline)