import unittest
from project.utenti.models import Utente

class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = Utente(password = 'cat')
        self.assertTrue(u.password_hash is not None)
    
    def test_no_password_getter(self):
        u = Utente(password = 'cat')
        with self.assertRaises(AttributeError):
            u.password
    
    def test_password_verification(self):
        u = Utente(password = 'cat')
        self.assertTrue(u.verify_password('cat'))
        self.assertFalse(u.verify_password('dog'))