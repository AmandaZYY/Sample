import random
from typing import List
import bisect
from memory_profiler import profile

class RandomGen:
    def __init__(self, random_nums: List[float], probabilities: List[float]):
        assert len(random_nums) == len(
            probabilities
        ), "Length of numbers and probabilities must be equal"
        assert all(
            prob > 0 for prob in probabilities
        ), "All probabilities must be positive"
        assert (
            abs(sum(probabilities) - 1) < 1e-6
        ), "Sum of probabilities must be approximately 1"

        self._random_nums = random_nums
        self._probabilities = probabilities
        # Create cumulative probabilities
        self._cumulative_probs = [
            sum(probabilities[: i + 1]) for i in range(len(probabilities))
        ]
    
    def next_num(self) -> float:
        """
        Returns one of the randomNums. When this method is called multiple
        times over a long period, it should return the numbers roughly with
        the initialized probabilities.
        """
        # Generate a uniform random number
        rand = random.random()
        # Find where rand fits into cumulative_probs
        index = bisect.bisect_left(self._cumulative_probs, rand)
        return self._random_nums[index]
       
@profile
def my_func():
    # Testing the RandomGen class
    random_gen = RandomGen([i for i in range(10000)], [0.0001]*10000 )

    # Generating numbers 100 times
    # generator = random_gen.next_num()
    generated_numbers = [ random_gen.next_num() for _ in range(10000)]

    # Counting the frequency of each number
    frequency = {number: generated_numbers.count(number) for number in random_gen._random_nums}
    #print(frequency)

if __name__ == '__main__':
    my_func()
