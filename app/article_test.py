import unittest
from models import article
Article=article.Article

class ArticleTest(unittest.TestCase):
     '''
    Test class to test the behaviour of the Article class
    '''
    def setUp(self):
        '''
        set up method that will run before every Test
        '''
        self.new_article=Article("one",Nicole","WSJ Wealth Adviser Briefing","Brief price gaps in equity trades cost investors about $2 billion a year","http://m.wsj.net/video/20190214/021419seibjoebiden/021419seibjoebiden_1280x720.jpg","https://www.wsj.com/video/waiting-for-biden-why-the-2020-field-is-incomplete-until-he-decides/688A19B5-161D-4FA6-8315-9C025298B3D5.html")

    def test_article(self):
        self.assertTrue(isinstance(self.new_article,Article))

if __name__ == '__main__':
    unittest.main()