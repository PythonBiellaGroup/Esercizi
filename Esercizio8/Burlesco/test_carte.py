import unittest
from carte import Carta
from carte import Mazzo


class TestCarte(unittest.TestCase):
    def setUp(self):
        # Un po' di carte utili per i test
        self.tre_di_fiori = Carta(0, 3)
        self.fante_di_quadri = Carta(1, 11)
        self.altro_fante_di_quadri = Carta(1, 11)
        self.asso_di_cuori = Carta(2, 1)
        self.asso_di_fiori = Carta(0, 1)
        self.re_di_cuori = Carta(2, 13)
        self.sette_di_cuori = Carta(2, 7)

    def test_str(self):
        self.assertTrue(str(self.tre_di_fiori) == "3 di Fiori")
        self.assertTrue(str(self.fante_di_quadri) == "Fante di Quadri")

    def test_minor(self):
        self.assertTrue(self.tre_di_fiori < self.fante_di_quadri)
        # Equivalente
        self.assertLess(self.tre_di_fiori, self.fante_di_quadri)

    def test_equal(self):
        self.assertTrue(self.fante_di_quadri == self.altro_fante_di_quadri)
        # Equivalente
        self.assertEqual(self.fante_di_quadri, self.altro_fante_di_quadri)
        self.assertNotEqual(self.fante_di_quadri, self.tre_di_fiori)

    def test_esercizio_8(self):
        # Prima dell'esercizio
        # self.assertLess(self.asso_di_cuori, self.re_di_cuori)
        # Dopo l'esercizio
        self.assertGreater(self.asso_di_cuori, self.re_di_cuori)
        self.assertGreater(self.asso_di_cuori, self.asso_di_fiori)
        self.assertLess(self.sette_di_cuori, self.asso_di_cuori)


class TestMazzo(unittest.TestCase):
    def setUp(self):
        self.mazzo_rosso = Mazzo()
        self.mazzo_blu = Mazzo()
        self.re_di_cuori = Carta(2, 13)

    def test_rimuovi(self):
        self.mazzo_blu.rimuovi(self.re_di_cuori)
        self.assertFalse(self.re_di_cuori in self.mazzo_blu.carte)


if __name__ == '__main__':
    unittest.main()
