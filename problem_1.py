""" Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Result should be : 233168
"""

# Determine if a number is a multiple of 3 or 5
def is_multiple(number):
    return number % 3 == 0 or number % 5 == 0

def list_multiples(max_value):
    multiples = []
    for i in range(1, max_value):
        if is_multiple(i):
            multiples.append(i)
    return multiples

print(sum(list_multiples(1000)))

""" Alternativly... """
print(sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0)))