""" Summation of primes
Show HTML problem content  
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

ANSWER: 142913828922
"""

# Using the Sieve of Eratosthenes
"""
    For all numbers n from 2 to sqrt(max)
    if n is True:
        n is prime
        for all multiples of n where n < max
            mark multiples as False
"""

def prime_sieve(max=10):
    """Returns a list of prime numbers upto [max]"""
    # Make list of all numbers set to true
    primes = [True] * (max + 1)
    primes[0] = False
    primes[1] = False

    # Starting at 2 and going to the sqrt(max)
    n = 2
    while (n * n <= max):

        # If prime[n] is still True it is a prime
        if (primes[n] == True):
            # Mark all mutliples as false starting at n^2
            for i in range(n * n, max + 1, n):
                primes[i] = False
        n += 1
    
    # Converting our list of bools to a list of prime numbers
    found_primes = []
    for value in range(max + 1):
        if primes[value]:
            found_primes.append(value)
    return found_primes

all_primes = prime_sieve(2_000_000)
print(sum(all_primes))