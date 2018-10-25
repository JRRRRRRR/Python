# JR Chen
# 111993420
# Jiarochen
# CSE 101
# Lab 4

# IN THIS PART OF THE FILE, IT IS VERY IMPORTANT THAT YOU *ONLY* WRITE CODE
# INSIDE THE FUNCTION DEFINITIONS BELOW! IF YOU WRITE CODE BETWEEN (AND OUTSIDE)
# THE FUNCTION DEFINITIONSS, THE GRADING SYSTEM WILL NOT BE ABLE TO READ YOUR
# CODE AND YOU WILL RECEIVE A GRADE OF ZERO FOR THIS ASSIGNMENT!

def expand(text):
    string = ""
    for i in range(len(text)//2):
        string = string + text[2*i] * int(text[2*i+1])
    return string 


def braid(level):
    result = [1,1,1]
    for i in range(1,level+1):
        if i % 2 == 1:
            result[0] = result[0] + result[1]
            result[0],result[1] = result[1],result[0]
        else:
            result[2] = result[1] + result[2]
            result[1],result[2] = result[2],result[1] 
    return result


def shuffle(deck, rounds):
    newdeck = deck
    for i in range(rounds):
        first = newdeck[0:len(deck)//2]
        second = newdeck[len(deck)//2:]
        result = []
        for n in range(len(deck)//2):
            result.append(first[n])
            result.append(second[n])
        newdeck = result
    return newdeck


def backspace(text):
    while text.find("^H") > -1:
        text = text[0:(text.find("^H")-1)] + text[(text.find("^H")+2):]
    return text

# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE OR REMOVE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    ############### Part 1 Tests ###############
    print('Testing expand() with the string "d3o5z2y1": \"', expand("d3o5z2y1"), "\"", sep='')

    print('Testing expand() with the string "y2e1Z314p6o1C5": \"', expand("y2e1Z314p6o1C5"), "\"", sep='')

    print('Testing expand() with the string "E2r8A5*9e6F4": \"', expand("E2r8A5*9e6F4"), "\"", sep='')
    # Write your own tests for Part 1 here!
    print()  # prints a blank line

    ############### Part 2 Tests ###############
    print('Testing braid(0):', braid(0))
    print('Testing braid(2):', braid(2))
    print('Testing braid(5):', braid(5))
    print('Testing braid(1):', braid(1))

    # Write your own tests for Part 2 here!
    print() # prints a blank line

    ############### Part 3 Tests ###############
    initial_deck = [5, 2, 1, 7, 2, 3]
    rounds = 1
    print('Shuffling', initial_deck, rounds, 'time(s)......')
    d = shuffle(initial_deck, rounds)
    print("Final deck ordering is:", d, "\n")

    initial_deck = [14, 3, 2, -8, 11, 5, 9, 12]
    rounds = 2
    print('Shuffling', initial_deck, rounds, 'time(s)......')
    d = shuffle(initial_deck, rounds)
    print("Final deck ordering is:", d, "\n")

    initial_deck = [14, 3, 2, -8, 11, 5, 9, 12]
    rounds = 3
    print('Shuffling', initial_deck, rounds, 'time(s)......')
    d = shuffle(initial_deck, rounds)
    print("Final deck ordering is:", d, "\n")
    # Write your own tests for Part 3 here!
    print()  # prints a blank line

    ############### Part 4 Tests ###############
    print('Testing backspace("Hello, w^horld!"): \"', backspace("Hello, w^horld!"), "\"", sep='')
    print('Testing backspace("A Horse is a Horse, of k^Hcourse"): \"', backspace("A Horse is a Horse, of k^Hcourse"), "\"", sep='')
    print('Testing backspace("I wish^H^H^Hant some ice cream^H^H^H^H^Hmilk"): \"', backspace("I wish^H^H^Hant some ice cream^H^H^H^H^Hmilk"), "\"", sep='')
    # Write your own tests for Part 4 here!
    print()  # prints a blank line


