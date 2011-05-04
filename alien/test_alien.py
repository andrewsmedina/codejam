import unittest

class MatchInAlienLanguageTestCase(unittest.TestCase):

    def test_raw_word_should_be_match_with_itself(self):
        self.assertTrue(match_in_alien_language(word='abc', pattern='abc'))

unittest.main()
