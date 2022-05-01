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
        self.new_news = News(3456,'Python Is Awsome','Articles that will blow your mind','https://image.newsapi.org/t/p/v2/kls25hgfd',6.4,345676)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__':
    unittest.main()