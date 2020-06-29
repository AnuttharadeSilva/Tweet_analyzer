import unittest
from analyzer import *
from tweepy_streamer import *
from datetime import date
 
class TestAnalyzer(unittest.TestCase):

    def test_null(self):
        self.assertIsNotNone(predict(None))
        self.assertIsNotNone(predict([]))

    def test_Output(self):
        self.assertIsInstance(predict(None),list)
        self.assertIsInstance(predict([]),list)

    def test_type(self):
        self.assertIsInstance(predict(['happy','sad']),list)

    def test_positive(self):
        self.assertEqual(predict(['I am happy that corona is finaly over']),[1])

    def test_negative(self):
        self.assertEqual(predict(['We are suffering a lot']),[0])

class TestTweepy(unittest.TestCase):

    def test_type(self):
        self.assertIsInstance(get_tweets('corona AND Colombo',date(*map(int,'2020-6-1'.split('-'))), date(*map(int, '2020-6-14'.split('-'))), 10), list)
        self.assertIsInstance(get_tweets(' AND ',date(*map(int,'2020-6-1'.split('-'))), date(*map(int, '2020-6-14'.split('-'))), 10), list)
        self.assertIsInstance(get_tweets('corona',date(*map(int,'2020-6-1'.split('-'))), date(*map(int, '2020-6-14'.split('-'))), 0), list)

 
if __name__ == "__main__":
    unittest.main()