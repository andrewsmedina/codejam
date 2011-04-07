import unittest
from reverse_words import reverse_words

class ReverseWordsTestCase(unittest.TestCase):

    def test_reverse_words_in_a_line(self):
        self.assertEqual('test a is this', reverse_words('this is a test'))

    def test_reverse_words_with_one_word_dont_change_de_line(self):
        self.assertEqual('foobar', reverse_words('foobar'))

unittest.main()
