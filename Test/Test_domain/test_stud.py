from domain.studenti import Student
import unittest

class StudentTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Incep testele pentru domain.studenti")

    @classmethod
    def tearDownClass(cls):
        print("Teste: OK!")

    def test_create_stud(self):
        stud = Student(123, "Pop Mihai")
        self.assertEqual(stud.get_id_student(), 123)
        self.assertEqual(stud.get_nume_student(), "Pop Mihai")
        self.assertEqual(len(stud.get_nume_student()), 9)
    def test_is_active(self):
        stud = Student(123, "Pop Mihai")
        self.assertTrue(stud.is_active())
    def test_set_nume_student(self):
        stud = Student(123, "Pop Mihai")
        stud.set_nume_student("Gavrila Boss")
        self.assertEqual(stud.get_nume_student(), "Gavrila Boss")
    def test_deactivate(self):
        stud = Student(123, "Pop Mihai")
        stud.deactivate()
        self.assertFalse(stud.is_active())
    def test_str_active(self):
        stud = Student(123, "Pop Mihai")
        self.assertEqual(str(stud), "123 | Pop Mihai")
    def test_str_inactive(self):
        stud = Student(123, "Pop Mihai")
        stud.deactivate()
        self.assertEqual(str(stud), "123 | Pop Mihai (sters)")






