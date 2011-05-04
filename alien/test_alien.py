import unittest
from alien import is_alien_word, letter_pattern_groups

class LetterPatternGroupsTestcase(unittest.TestCase):

    def test_simple_pattern_should_return_same_amout_of_letters_how_patters(self):
        self.assertEqual(3, len(letter_pattern_groups('abc')))

    def test_pattern_with_one_complex_pattern(self):
        self.assertEqual(3, len(letter_pattern_groups('(ab)bc')))

    def test_pattern_with_full_complex_pattern(self):
        self.assertEqual(3, len(letter_pattern_groups('(ab)(bc)(cd)')))


class IsAlienWordTestCase(unittest.TestCase):

    def test_raw_word_should_be_match_with_itself(self):
        self.assertTrue(is_alien_word(word='abc', pattern='abc', length=3))

    def test_other_word_shold_not_be_an_alien_word_if_words_are_different(self):
        self.assertFalse(is_alien_word(word='abc', pattern='xkc', length=3))

    def test_word_with_pattern_more_complex(self):
        self.assertTrue(is_alien_word(word='abc', pattern='(ab)bc', length=3))

    def test_word_with_pattern_full_complex(self):
        self.assertTrue(is_alien_word(word='abc', pattern='(ab)(bx)(cy)', length=3))


unittest.main()
