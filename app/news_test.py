import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    """
    Test class to test the behavior of the News class
    """
    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.new_news = News(3456,'Lorenz Meyer','Articles that will blow your mind','What makes Lorenzo happy','https://urlToImage/','2022-05-02T06:54:51Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__':
    unittest.main()