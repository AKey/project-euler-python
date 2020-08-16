""" Power digit sum
Problem 16
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

ANSWER : 1366
"""

def power_sum(base, power):
    number = base ** power
    return sum(int(digit) for digit in str(number))

print(power_sum(2, 1000))