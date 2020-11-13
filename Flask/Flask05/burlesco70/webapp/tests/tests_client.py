import re
import unittest
from project import create_app, db
from project.serate.models import Serata
from project.corsi.models import Corso
from project.tags.models import Tag

class FlaskClientTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        Tag.insert_default_tags()
        '''
        self.client instance variable is the Flask test client object. 
        This object exposes methods that issue requests into the application
        
        When the test client is created with the use_cookies option enabled, 
        it will accept and send cookies in the same way browsers do, so functionality
        that relies on cookies to recall context between requests can be used
        '''
        self.client = self.app.test_client(use_cookies=True)

    def test_check_tag(self):
        t = Tag.query.filter_by(name="Python").first()
        #print(t)
        self.assertTrue(t.name == "Python")

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

# TODO Capire perchè non funziona
'''
    def test_home_page(self):
        response = self.client.get('/')
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Python Group Biella' in response.get_data(as_text=True))
'''
