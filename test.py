from unittest import TestCase, main
import utilities


class GetAmountOfSentencesTest(TestCase):
    def test_default(self):
        text = "weqwe. weqwe! weqwe? weqwe..."
        self.assertEqual(utilities.get_amount_of_sentences(text), 4)

    def test_with_abbreviations(self):
        text = "weqwe with Mr. Brown. weqwe with Dr. Who. weqwe with p.s. something."
        self.assertEqual(utilities.get_amount_of_sentences(text), 3)


class GetAmountOfNonDeclarativeSentences(TestCase):
    def test_only_declarative(self):
        text = "weqwe. weqwe. weqwe."
        self.assertEqual(utilities.get_amount_of_non_declarative_sentences(text), 0)

    def test_only_non_declarative(self):
        text = "weqwe? weqwe! weqwe!?"
        self.assertEqual(utilities.get_amount_of_non_declarative_sentences(text), 3)

    def test_mixin(self):
        text = "weqwe? weqwe... weqwe. weqwe. weqwe!?"
        self.assertEqual(utilities.get_amount_of_non_declarative_sentences(text), 2)


class GetAverageAmountOfCharactersInSentence(TestCase):
    def test_default_text(self):
        text = "weqwe? weqwe! weqwe!?"
        self.assertEqual(utilities.get_average_amount_of_characters_in_sentence(text), 12)

    def test_text_with_numbers(self):
        text = "weqwe 1234 123weqwe? weqwe 31343! 21423532 weqwe!?"
        self.assertEqual(utilities.get_average_amount_of_characters_in_sentence(text), 12)

    def test_empty(self):
        text = ""
        self.assertEqual(utilities.get_average_amount_of_characters_in_sentence(text), 0)


class GetAverageAmountOfCharactersInWord(TestCase):
    def test_default_text(self):
        text = "weqwe? weqwe! weqwe!?"
        self.assertEqual(utilities.get_average_amount_of_characters_in_word(text), 6)

    def test_text_with_numbers(self):
        text = "weqwe 1234 123weqwe? weqwe 31343! 21423532 weqwe!?"
        self.assertEqual(utilities.get_average_amount_of_characters_in_word(text), 6)

    def test_empty(self):
        text = ""
        self.assertEqual(utilities.get_average_amount_of_characters_in_word(text), 0)


class GetTopGrams(TestCase):
    def test_text_with_no_repeat(self):
        text = "qwery asfg zxcvb rtyu cvbnmm"
        expected = [("qwery asfg zxcvb", 1), ("asfg zxcvb rtyu", 1), ("zxcvb rtyu cvbnmm", 1)]
        self.assertEqual(utilities.get_top_grams(text, 3, 3), expected)

    def test_text_with_repeat(self):
        text = "text with repeat word repeat word repeat word"
        expected = [("repeat word", 3), ("word repeat", 2)]
        self.assertEqual(utilities.get_top_grams(text, n=2, k=2), expected)


if __name__ == "__main__":
    main()