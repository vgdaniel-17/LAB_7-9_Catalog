import unittest
from domain.disciplina import *
from repository.repository_discipline import *


class TestDis(unittest.TestCase):
    def setUp(self):
        self.discipline = RepoDiscipline()

    def test_addDiscipline(self):
        new_dis = Discipline(4124, "mate", "gabi")
        self.discipline.addDiscipline(new_dis)

        all_dis = self.discipline.getAllDiscipline()

        self.assertEqual(len(all_dis), 1)
        self.assertEqual(all_dis[-1].get_id_disciplina(), 4124)
        self.assertEqual(all_dis[-1].get_nume_disciplina(), "mate")
        self.assertEqual(all_dis[-1].get_profesor(), "gabi")

if __name__ == '__main__':
    unittest.main()
