# CSE 101, Fall 2018
# Assignment 1 starter code
#
# Your name: JR Chen
# Your SBU ID:111993420

# Complete the function that follows for this assignment

import string

def alfg(sequence, rounds):
    round = 0
    x = sequence
    y = sequence[1:]
    for n, m in zip(x,y):
        a = (n + m) % 10
        round += 1
        x.append(a)
        y.append(a)
        if round == rounds:
            break;
    return sequence[-5:] # CHANGE OR REPLACE THIS STATEMENT


# DO NOT modify or remove the code below! We will use it for testing.

if __name__ == "__main__":
    # Problem 1: Lagged Fibonacci Digits
    init_sequence = []
    next_value = 10 # we need a multi-digit value other than -1 to force the loop to begin
    while next_value != -1 and next_value > 9:
        next_value = int(input("Enter the next digit in the initial sequence, or -1 to end: "))
        if next_value != -1 and next_value < 10:
            init_sequence.append(next_value)
            next_value = 10 # force the loop to continue after a single digit is entered
    rds = int(input("Enter the number of rounds to perform: "))

    print("Calling alfg() with the starting sequence", init_sequence, "and", rds, "rounds, for a final result of", alfg(init_sequence,rds))
    print()

