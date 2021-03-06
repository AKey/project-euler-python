""" Even Fibonacci numbers
Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

Result should be : 4613732
"""

# Get all of the fibinachi numbers below 4Million
fib = [1, 2]
while fib[-1] < 4_000_000:
    fib.append(fib[-1] + fib[-2])
del fib[-1]

# Determine if a number is even and add it to the running total
total = 0
for i in fib:
    if i % 2 == 0:
        total += i

print(total)
