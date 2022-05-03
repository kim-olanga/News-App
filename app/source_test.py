import unittest
from app.models import source
Source = source.Source

class SourceTest(unittest.TestCase):
    """
    Test class to test the behavior of the Source class
    """
    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.new_source = Source(3456,'Lorenz Meyer','Articles that will blow your mind','What makes Lorenzo happy','2022-05-02T06:54:51Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

if __name__ == '__main__':
    unittest.main()