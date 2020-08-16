""" Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

ANSWER : 6857
"""

# I wanted to do this more functionally,no variables are passed and mutated

import math

# Get factors of a number
""" We use the square root to find one factor then divide the target number
    by the result to find the second half of that factor. Every factor of a 
    number will be either lower than the square root as sqrt * sqrt = number
    or it will be the complement of that lower factor.
    The raw result is a list like [1, 24, 2, 12, 3, 8, 4, 6] so we sort
    to make the output nicer if we want to see it
"""
def get_factors(number):
    factors = []
    for i in range(1, int(math.sqrt(number) + 1)):
        if number % i == 0:
            factors.append(i)
            factors.append(number // i)
    # This is just so the list looks nice
    factors.sort()
    return factors



# Determine if a number is prime
def is_prime(number):
    return len(get_factors(number)) == 2


# Find the highest prime number
def largest_prime(number):
    factors = get_factors(number)
    primes = []
    for factor in factors:
        if is_prime(factor):
            primes.append(factor)
    return max(primes)


print((largest_prime(600851475143)))
print(get_factors(24))