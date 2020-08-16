""" Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

ANSWER: 232792560
"""

def is_divisible_by_all(value, max=20):
    # Start at 2, everything is divisible by 1
    for i in range(2, max + 1):
        if value % i != 0:
            return False
    return True

def get_smallest_multiple(max=20):
    # No value below the top of our range is a multiple of the max value
    value = max
    while True:
        if is_divisible_by_all(value, max):
            return value
        # The multiple must be a multiple of the largest number in our range so
        # we increment by that much each step.
        value += max

print(get_smallest_multiple(100))