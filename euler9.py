""" Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

ANSWER: 31875000
"""

import math

def get_hypotenuse(target):
    a = 1
    b = 2
    for b in range(1, target):
        for a in range(1, b):
            c = math.sqrt(a**2 + b**2)
            # print(f'c={c}, b={b}, a={a}')
            if(a + b + c) == target:
                return int(a * b * c)

print(get_hypotenuse(1000))