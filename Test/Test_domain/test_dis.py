import unittest
from domain.disciplina import Discipline

class TestDiscipline(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Incep testele pentru domain.disciplina")

    @classmethod
    def tearDownClass(cls):
        print("Teste: OK!")

    def test_create_dis(self):
        dis = Discipline(123, "Info", "Polinomic Munteanu")
        self.assertEqual(dis.get_id_disciplina(), 123)
        self.assertEqual(dis.get_nume_disciplina(), "Info")
        self.assertEqual(dis.get_profesor(), "Polinomic Munteanu")
    def test_set_nume_disciplina(self):
        dis = Discipline(123, "Info", "Polinomic Munteanu")
        dis.set_nume_disciplina("Mate")
        self.assertEqual(dis.get_nume_disciplina(), "Mate")
        self.assertEqual(dis.get_profesor(), "Polinomic Munteanu")
    def test_set_profesor(self):
        dis = Discipline(123, "Info", "Polinomic Munteanu")
        dis.set_profesor("Integralia Matei")
        self.assertEqual(dis.get_profesor(), "Integralia Matei")
        self.assertEqual(dis.get_nume_disciplina(), "Info")
    def test_is_active(self):
        dis = Discipline(123, "Info", "Polinomic Munteanu")
        self.assertTrue(dis.is_active())
    def test_is_deactivate(self):
        dis = Discipline(123, "Info", "Polinomic Munteanu")
        dis.deactivate()
        self.assertFalse(dis.is_active())
    def test_str_active(self):
        dis = Discipline(123, "Info", "Polinomic Munteanu")
        self.assertEqual(str(dis), "123 | Info | Polinomic Munteanu")
    def test_str_deactivate(self):
        dis = Discipline(123, "Info", "Polinomic Munteanu")
        dis.deactivate()
        self.assertEqual(str(dis), "123 | Info | Polinomic Munteanu (sters)")
