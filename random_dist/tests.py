import unittest
from unittest.mock import patch
from randomgen import RandomGen


class TestRandomGen(unittest.TestCase):
    def test_initialization(self):
        """Test initialization of RandomGen class"""
        with self.assertRaises(AssertionError):
            RandomGen([-1, 0, 1], [0.1, 0.2])  # Different lengths

        with self.assertRaises(AssertionError):
            RandomGen([-1, 0, 1], [-0.1, 0.6, 0.5])  # Negative probabilities

        with self.assertRaises(AssertionError):
            RandomGen([-1, 0, 1], [0.3, 0.3, 0.3])  # Probabilities don't sum to 1

        # Should pass
        RandomGen([-1, 0, 1], [0.1, 0.2, 0.7])

    def test_distribution(self):
        """Test if next_num produces numbers according to specified probabilities"""
        numbers = [-1, 0, 1, 2]
        probabilities = [0.1, 0.2, 0.1, 0.6]
        random_gen = RandomGen(numbers, probabilities)

        generated_numbers = [random_gen.next_num() for _ in range(10000)]
        frequency = {
            number: generated_numbers.count(number) / 10000 for number in numbers
        }

        for number, prob in zip(numbers, probabilities):
            self.assertAlmostEqual(frequency[number], prob, delta=0.05)
    
    @patch('random.random')
    def test_next_num(self, mock_random):
        """Test if next_num function maps rand to the right number in the list"""

        # mock random.random()
        mock_random.return_value = 0.35
        
        numbers = [-1, 0, 1, 2]
        probabilities = [0.1, 0.2, 0.1, 0.6]
        random_gen = RandomGen(numbers, probabilities)
        result = random_gen.next_num()
        
        # Check that the function returns the mocked value
        self.assertEqual(result, 1)

        # Ensure that random.random() was called exactly once
        mock_random.assert_called_once()
        


if __name__ == "__main__":
    unittest.main()
