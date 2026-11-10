import unittest
import main
class TestPersianTextAnalyzer(unittest.TestCase):
    def test_count_words(self):
        text = "سلام دنیا"
        self.assertEqual(main.count_words(text), 2)
    def test_count_words_empty(self):
        self.assertEqual(main.count_words(""), 0)
    def test_count_words_punctuation(self):
        text = "سلام، دنیا!"
        self.assertEqual(main.count_words(text), 2)
    def test_count_characters(self):
        text = "abc"
        self.assertEqual(main.count_characters(text), 3)
    def test_count_letters(self):
        text = "abc 123"
        self.assertEqual(main.count_letters(text), 3)
    def test_count_sentences(self):
        text = "این یک جمله است. دیگری هم هست!"
        self.assertEqual(main.count_sentences(text), 2)
    def test_character_frequency(self):
        text = "aabb"
        freq = main.character_frequency(text)
        self.assertEqual(freq['a'], 2)
        self.assertEqual(freq['b'], 2)
    def test_word_frequency(self):
        text = "سگ سگ حیوان"
        freq = main.word_frequency(text)
        self.assertEqual(freq['سگ'], 2)
        self.assertEqual(freq['حیوان'], 1)
    def test_most_common_words(self):
        text = "سگ سگ حیوان سگ"
        common = main.most_common_words(text, 2)
        self.assertEqual(common[0][0], 'سگ')
        self.assertEqual(common[0][1], 3)
    def test_analyze(self):
        text = "سلام دنیا. امیدوارم خوب باشی."
        stats = main.analyze(text)
        self.assertIn('word_count', stats)
        self.assertIn('character_count', stats)
        self.assertIn('letter_count', stats)
        self.assertIn('sentence_count', stats)
        self.assertIn('character_frequency', stats)
        self.assertIn('word_frequency', stats)
        self.assertIn('most_common_words', stats)
        self.assertEqual(stats['word_count'], 5)
        self.assertEqual(stats['sentence_count'], 2)
if __name__ == '__main__':
    unittest.main()
