import unittest
from ibmtranslator import englishToFrench, frenchToEnglish



class TestIbmApi(unittest.TestCase):
    def test_englishToFrench(self):
        # self.assertEqual(englishToFrench(""), "")
        self.assertEqual(englishToFrench("Hello"), "Bonjour")



    def test_frenchToEnglish(self):
        # self.assertEqual(frenchToEnglish(""), "")
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")


if __name__ == '__main__':
    unittest.main()
