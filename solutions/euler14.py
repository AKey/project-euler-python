""" Longest Collatz sequence
Show HTML problem content  
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

ANSWER: 837799
"""
# Figure out Memoization

import time

def get_collatz_sequence(start_number):
    sequence = []
    sequence.append(start_number)
    while sequence[-1] > 1:
        if sequence[-1] % 2 == 0:
            sequence.append(int(sequence[-1] / 2))
        else:
            sequence.append(int(3 * sequence[-1] + 1))
    return sequence

def get_longest_collatz(max_number):
    largest_start_num = -1
    longest_count = -1
    for i in range(1, max_number):
        collatz = get_collatz_sequence(i)
        if len(collatz) > longest_count:
            longest_count = len(collatz)
            largest_start_num = i
    return largest_start_num


start = time.process_time()
longest_collatz = get_longest_collatz(1000000)
stop = time.process_time()
print(f'{longest_collatz} calculated in {stop - start}')