# JR Chen
# 111993420
# Jiarochen
# CSE 101
# Lab 2

# IN THIS PART OF THE FILE, IT IS VERY IMPORTANT THAT YOU *ONLY* WRITE CODE
# INSIDE THE FUNCTION DEFINITIONS BELOW! IF YOU WRITE CODE BETWEEN (AND OUTSIDE)
# THE FUNCTION DEFINITIONSS, THE GRADING SYSTEM WILL NOT BE ABLE TO READ YOUR
# CODE AND YOU WILL RECEIVE A GRADE OF ZERO FOR THIS ASSIGNMENT!

def score(hand):
    score = 0
    for n in hand:
        if n == 2:
            score = 0
            break;
        elif n == 5:
            score = 0
        else:
            score = score + n
    return score 

def factors(n):
    factors=[]
    for i in range(n+1,0,-1):
        if n % i == 0:
            factors.append(i)
    return factors 

def ladder(steps, commands):
    count = 0
    position = 1
    for i in commands:
        if count == 10:
            break;
        elif count < 10:
            count += 1
        if i == "C":
            position += 1
            if position > steps:
                break;
        elif i == "D":
            position -= 1
            if position == 0:
                position += 1
        elif i == "R":
            position = 1;
    return count 

def babylonian(symbols):
    series = []
    value2 = 0
    for i in symbols:
        value = 0
        for n in i:
            if n == "<":
                value += 10
            elif n == "T":
                value += 1
            elif n == "\\":
                value = 0
        series.append(value)
    for a in series:
        value2 = value2 + 60 ** (len(symbols) - series.index(a) - 1 ) * a
    return series, value2


# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE OR REMOVE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    ############### Part 1 Tests ###############
    print('Testing score() for [6,3,3,1,5]:', score([6,3,3,1,5]))
    print('Testing score() for [6,1,3,1,4]:', score([6,1,3,1,4]))
    print('Testing score() for [4,1,2,4,4]:', score([4,1,2,4,4]))
    # Write your own tests for Part 1 here!
    print()  # prints a blank line

    ############### Part 2 Tests ###############
    print('Testing factors() for value = 38:', factors(38))
    print('Testing factors() for value = 128:', factors(128))
    print('Testing factors() for value = 17:', factors(17))
    # Write your own tests for Part 2 here!
    print()  # prints a blank line

    ############### Part 3 Tests ###############
    print('Testing ladder() for steps = 1 and commands = "C":', ladder(1, "C"))
    print('Testing ladder() for steps = 1 and commands = "DDRCDCC":', ladder(1, "DDRCDCC"))
    print('Testing ladder() for steps = 4 and commands = "CDDCCCCCRCCCCDDDD":', ladder(4, "CDDCCCCCRCCCCDDDD"))
    # Write your own tests for Part 3 here!
    print() # prints a blank line

    ############### Part 4 Tests ###############
    print('Testing babylonian() for the symbol sequence ["TTT", "<"]:', babylonian(["TTT","<"]))
    print('Testing babylonian() for the symbol sequence ["<T", "\\", "TTTTTT"]:', babylonian(["<T", "\\", "TTTTTT"]))
    print('Testing babylonian() for the symbol sequence ["<<<TTTTTTT", "<", "\\", "TTTT", "<<<<<"]:', babylonian(["<<<TTTTTTT", "<", "\\", "TTTT", "<<<<<"]))
    # Write your own tests for Part 4 here!
    print() # prints a blank line

