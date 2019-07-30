'''
In HIRE-ASSISTANT, assuming that the candidates are presented in a random order, what is the probability that you hire
exactly one time? What is the probability you hire exactly n times?
'''


import random
import math


def generate_random(a, b):
    random_range_size = b - a + 1
    while True:
        random_number = 0
        for i in range(math.ceil(math.log(random_range_size, 2))):
            random_number << random.randint(0, 1)
        if random_number < random_range_size:
            break
    return random_number + a


test_size = 1000
for i in range(test_size):
    if generate_random(0, 3) not in [0, 1, 2, 3]:
        print("Incorrect value")
for i in range(test_size):
    if generate_random(0, 4) not in [0, 1, 2, 3, 4]:
        print("Incorrect value")
for i in range(test_size):
    if generate_random(1, 5) not in [1, 2, 3, 4, 5]:
        print("Incorrect value")
print("tests finished")
