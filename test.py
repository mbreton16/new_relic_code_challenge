import unittest
from main import get_words, phrases, run_sequence


class MainTest(unittest.TestCase):


    def test_get_words(self):
        # Basic sanity test
        test_basic_string = 'testing'
        self.assertEqual('testing', next(get_words(test_basic_string)))

        # Test if the sanitizer can handle all kinds of weird punctuation - should be removed entirely
        test_string_punctuation = 'te!@#$%^&*./\;\'(--sting'
        self.assertEqual('testing', next(get_words(test_string_punctuation)))

        # Test upper case conversion
        test_string_case = 'TESTING'
        self.assertEqual('testing', next(get_words(test_string_case)))

    def test_phrases(self):
        simple_phrase = ['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']
        for idx, i in enumerate(phrases(simple_phrase)):
            if idx == 0:
                self.assertEqual(('the', 'quick', 'brown'), i) # First combination
            if idx == 1:
                self.assertEqual(('quick', 'brown', 'fox'), i) # Second combination, and so on
        self.assertEqual(7, sum(1 for _ in phrases(simple_phrase))) # Should be a total of 7 combinations

    # More of a functional test but helpful in determining if the output is correct.
    def test_run_sequence(self):
        try:
            with open('pg2009.txt', 'r', encoding='utf-8') as file:
                data = file.read()
        except Exception as e:
            print(e)
        results = run_sequence(data) # Results is a dictionary of tupled phrases as the index, with the count as value
        self.assertEqual(320, results[('of', 'the', 'same')])  # The most common phrase in the sample text reoccurs 320x
        self.assertEqual(116, results[('in', 'the', 'same')]) # Test another popular phrase to be sure.


if __name__ == '__main__':
    unittest.main()



