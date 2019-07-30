'''
Suppose that you want to output 0 with probability 1/2 and 1 with probability 1/2. At your disposal is a procedure
BIASED-RANDOM that outputs either 0 or 1. It outputs 1 with some probability p and 0 with probability 1−p, where 0<p<1,
but you don't now what p is. Give an algorithm that uses BIASED-RANDOM as a subroutine, and returns an unbiased answer,
returning 0 with probability 1/2 and 1 with probability 1/2. What is the expected running time of your algorithm as a
function of p?
'''


import random


def biased_random(p):
    if random.uniform(0, 1) > p:
        return 1
    else:
        return 0


def unbiased_random_using_biased_random(p):
    while True:
        rand1 = biased_random(p)
        rand2 = 1 if biased_random(p) == 0 else 0
        if rand1 == rand2:
            return rand1


number_of_zeroes = 0
number_of_ones = 0
for i in range(10000):
    if biased_random(0.6) == 0:
        number_of_zeroes += 1
    else:
        number_of_ones += 1
print("after running biased_random with target_p = 0.6 we received actual_p = {}"
      .format(number_of_zeroes / (number_of_ones + number_of_zeroes)))

number_of_zeroes = 0
number_of_ones = 0
for i in range(10000):
    if biased_random(0.1) == 0:
        number_of_zeroes += 1
    else:
        number_of_ones += 1
print("after running biased_random with target_p = 0.1 we received actual_p = {}"
      .format(number_of_zeroes / (number_of_ones + number_of_zeroes)))


number_of_zeroes = 0
number_of_ones = 0
for i in range(10000):
    if unbiased_random_using_biased_random(0.6) == 0:
        number_of_zeroes += 1
    else:
        number_of_ones += 1
print("after running unbiased_random_using_biased_random with target_p = 0.6 we received actual_p = {}"
      .format(number_of_zeroes / (number_of_ones + number_of_zeroes)))

number_of_zeroes = 0
number_of_ones = 0
for i in range(10000):
    if unbiased_random_using_biased_random(0.1) == 0:
        number_of_zeroes += 1
    else:
        number_of_ones += 1
print("after running unbiased_random_using_biased_random with target_p = 0.1 we received actual_p = {}"
      .format(number_of_zeroes / (number_of_ones + number_of_zeroes)))
