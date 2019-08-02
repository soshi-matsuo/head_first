import unittest
import poker

class TestPoker(unittest.TestCase):

    def setUp(self):
        self.hands_patterns = [
            ['4H', '3H', '2H', '5H', '6H'],
            ['2H', "3H", '4H', '5H', '6D'],
            ['2H', "3H", '5H', '6H', '7H'],
            ['2H', "3H", '6S', '5H', '7D'],
            ['2H', "2D", '2S', '2C', '7D']
        ]
    @unittest.SkipTest
    def test_is_high_card(self):
        hands = ['2H', '4H', '5C', '9S', 'AS']
        self.assertEqual(True, True)

    def test_is_straight_flush(self):
        label_patterns = [
            True, False, False, False, False
        ]
        for hands, label in zip(self.hands_patterns, label_patterns):
            with self.subTest(hands=hands, label=label):
                self.assertEqual(poker.is_straight_flush(hands), label)

    def test_is_flush(self):
        label_patterns = [
            True, False, True, False, False
        ]
        for hands, label in zip(self.hands_patterns, label_patterns):
            with self.subTest(hands=hands, label=label):
                self.assertEqual(poker.is_flush(hands), label)


    def test_is_straight(self):
        label_patterns = [
            True, True, False, False, False
        ]
        for hands, label in zip(self.hands_patterns, label_patterns):
            with self.subTest(hands=hands, label=label):
                self.assertEqual(poker.is_straight(hands), label)

    def test_is_four_card(self):
        label_patterns = [
            False, False, False, False, True
        ]
        for hands, label in zip(self.hands_patterns, label_patterns):
            with self.subTest(hands=hands, label=label):
                self.assertEqual(poker.is_four_card(hands), label)

if __name__ == '__main__':
    unittest.main()