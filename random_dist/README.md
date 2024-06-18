# RandomGen #

RandomGen is a Python class that generates random numbers based on predefined probabilities. 
## RandomGen Class ##
### init ###
When init, user can pass on a list of random_numbers and the matching probabilities. within \_\_init\_\_, we check 1. length of the random_nums and probabilites must be equal. 2. all elements in probabilities have to be within \[0,1\], and 3. sum of probabilities must be equal to 1 (here I added difference must be less than 1e-6, almost sums to 1). Otherwise, assertion exceptions will be raised accordingly.\
I also created a self._cumulative_probs, which will be used in next_num(), also to avoid repeated calculation of this.
### next_num ###
Most importantly, the RandomGen class contains a function next_num(), which returns one of the randomNums. When this method is called multiple times over a long period, it should return the numbers roughly with the initialized probabilities. \
First, based on requirements, it is most suitable to use generator. \
random.random() can only generate uniform distributed numbers in \[0,1\), according to the requirments, the simplest way is to use cumulatative probabilities, then find where does rand fit into cumulative_probs, (i.e. first element that's > rand), then return the matching random_number. 

## Tests ##
As for the unit tests, there are 3 main tests: 1 for init, 1 simple test for distribution of next_num(), and one more that mocks random number \[0,1\), and test if the function maps it to the right number in the given list. \