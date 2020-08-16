""" Largest palindrome product
Show HTML problem content  
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

ANSWER: 906609
"""

# Get all 3 digit numbers
def get_values():
    arr = []
    for i in range(100, 1000):
        arr.append(i)
    return arr

# Determine if a number is a palindrome
def is_palindrome(value):
    return str(value) == str(value)[::-1]


# Get the product of all pairs in a list
def get_all_products(input_numbers):
    products = []
    while len(input_numbers) > 1:
        for number in input_numbers:
            products.append(input_numbers[0] * number)
        del input_numbers[0]
    return products


# Get the largest palindrome
def get_largest_palindrome(products):
    # Reverse sort the products list so we start with the largest number
    # We can return the first palindrome because it will be the largest too
    products.sort(reverse = True)
    for i in products:
        if is_palindrome(i):
            return i

""" EXTRA BONUS::
    Get all of the palindromes!
"""
def get_all_palindromes(numbers):
    palindromes = []
    numbers.sort()
    for value in numbers:
        if is_palindrome(value):
            palindromes.append(value)
    return palindromes


#print(get_all_palindromes(get_all_products(get_values())))
print(get_largest_palindrome(get_all_products(get_values())))