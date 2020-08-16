""" 10001st prime 
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

ANSWER: 104743
"""
import math

def is_prime(number):
    if number == 1:
        return False
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            # Any Factors other than 1 and `number` make it not prime
            return False
    return True


def get_prime(number):
    primes = []
    value = 2
    while len(primes) < number:   
        if is_prime(value):
            primes.append(value)
        value += 1
    return primes[-1]

print(get_prime(10001))

# Testing printing formatted text
# print(f'{get_prime(10001):,}')