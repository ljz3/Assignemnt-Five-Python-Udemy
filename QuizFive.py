# 1) Import the random function and generate both a random number between 0 and 1 as well as a random number between 1 and 10.

import random
import datetime

zero_to_one = random.randrange(0,2)
one_to_ten = random.randrange(1,11)
print(zero_to_one)
print(one_to_ten)

# 2) Use the datetime library together with the random number to generate a random, unique value.

random_unique = str(datetime.datetime.now()) + str(one_to_ten)
print(random_unique)