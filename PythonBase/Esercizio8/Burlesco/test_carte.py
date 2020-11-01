import unittest
from carte import Carta
from carte import Mazzo
from carte import Mano


class TestCarte(unittest.TestCase):
    def setUp(self):
        # Un po' di carte utili per i test
        self.tre_di_fiori = Carta(0, 3)
        self.fante_di_quadri = Carta(1, 11)
        self.altro_fante_di_quadri = Carta(1, 11)
        self.asso_di_cuori = Carta(2, 1)
        self.asso_di_fiori = Carta(0, 1)
        self.altro_asso_di_fiori = Carta(0, 1)
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
        self.assertEqual(self.asso_di_fiori, self.altro_asso_di_fiori)
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
        self.mazzo_verde = Mazzo()
        self.re_di_cuori = Carta(2, 13)
        self.mano_mario = Mano("Mario")
        self.mano_davide = Mano("Davide")

    def test_rimuovi(self):
        self.mazzo_blu.rimuovi(self.re_di_cuori)
        self.assertFalse(self.re_di_cuori in self.mazzo_blu.carte)

    def test_pesca(self):
        numero_carte = len(self.mazzo_rosso.carte)
        carta = self.mazzo_rosso.carte[numero_carte-1]
        self.mazzo_rosso.pesca()
        # Controllo che il mazzo abbia una carta in meno
        self.assertTrue(len(self.mazzo_rosso.carte) == numero_carte-1)
        # Controllo che la carta pescata non ci sia più
        self.assertFalse(carta in self.mazzo_rosso.carte)

    def test_mazzo_vuoto(self):
        self.assertFalse(self.mazzo_blu.mazzo_vuoto())
        for i in range(len(self.mazzo_blu.carte)):
            self.mazzo_blu.pesca()
        self.assertTrue(self.mazzo_blu.mazzo_vuoto())

    def test_distribuisci_tutte_le_carte(self):
        numero_carte_mazzo = len(self.mazzo_verde.carte)
        self.mazzo_verde.distribuisci_carte((self.mano_mario,
                                             self.mano_davide))
        self.assertEqual(len(self.mano_mario.carte),
                         len(self.mano_davide.carte),
                         numero_carte_mazzo // 2)

    def test_distribuisci_dieci_carte(self):
        '''
        Distribuisce in tutto 10 carte, le mani sono due, quindi cinque a testa
        '''
        print(len(self.mazzo_rosso.carte))
        self.mazzo_rosso.distribuisci_carte((self.mano_mario,
                                             self.mano_davide), 10)
        self.assertEqual(len(self.mano_mario.carte),
                         len(self.mano_davide.carte),
                         5)


if __name__ == '__main__':
    unittest.main()
