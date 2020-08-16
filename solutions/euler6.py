""" Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,

1^2+2^2+...+10^2=385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)^2=55^2=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

ANSWER: 25164150
"""

# Sum of square
def sum_of_squares(max):
    total = 0
    for i in range(1, max + 1):
        total += i**2
    return total

# Square of sums
def square_of_sums(max):
    return sum(range(1, max + 1))**2

print(square_of_sums(100) - sum_of_squares(100))