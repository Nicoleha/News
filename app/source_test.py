import unittest
from models import source
Source = source.Source

class SourceTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Source class
    '''
    def setUp(self):
        '''
        set up method that will run before every Test
        '''
        self.new_source=Source('the-wall-street-journal','the expansionist technology','Find live scores, player and team news, videos, rumors')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

if __name__ == '__main__':
    unittest.main()