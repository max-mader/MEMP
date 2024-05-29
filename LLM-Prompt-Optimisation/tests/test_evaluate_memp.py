import unittest

from evaluate_memp import rate_verb_tense_consistency, rate_streamlining_sentence_structure, rate_removing_execution_details

class EvaluateMEMPTestCase(unittest.TestCase):
    def test_rate_verb_tense_consistency(self):
        rating = rate_verb_tense_consistency("Creating", "Create")
        self.assertEqual(rating, 10)

    def test_rate_streamlining_sentence_structure(self):
        rating = rate_streamlining_sentence_structure("Creating a Universal Response Template involves designing a format that's adaptable across a wide range of tasks and queries, providing a structured yet flexible framework for responses.", "Creating a Universal Response Template, designing a format that's adaptable across a wide range of tasks and queries.")
        self.assertEqual(rating, 8)

    def test_rate_removing_execution_details(self):
        rating = rate_removing_execution_details("Creating a Universal Response Template involves designing a format that's adaptable across a wide range of tasks and queries, providing a structured yet flexible framework for responses.", "Creating a Universal Response Template")
        self.assertEqual(rating, 9)

if __name__ == '__main__':
    unittest.main()