import unittest
from repository.repository_studenti import studenti, RepoStudent
from domain.studenti import Studenti


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.repo_student = RepoStudent()

    def test_add_student(self):

        new_student = Studenti(2131, "Vasile")
        self.repo_student.addStudent(new_student)

        all_students = self.repo_student.getAll()

        self.assertEqual(len(all_students), 1)
        self.assertEqual(all_students[-1].get_id_student(), 2131)
        self.assertEqual(all_students[-1].get_nume_student(), "Vasile")





if __name__ == '__main__':
    unittest.main()
