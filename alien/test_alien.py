import unittest
from alien import is_alien_word


class MatchInAlienLanguageTestCase(unittest.TestCase):

    def test_raw_word_should_be_match_with_itself(self):
        self.assertTrue(is_alien_word(word='abc', pattern='abc'))

unittest.main()
