# JR Chen
# 111993420
# Jiarochen
# CSE 101
# Lab 3

import string

# IN THIS PART OF THE FILE, IT IS VERY IMPORTANT THAT YOU *ONLY* WRITE CODE
# INSIDE THE FUNCTION DEFINITIONS BELOW! IF YOU WRITE CODE BETWEEN (AND OUTSIDE)
# THE FUNCTION DEFINITIONSS, THE GRADING SYSTEM WILL NOT BE ABLE TO READ YOUR
# CODE AND YOU WILL RECEIVE A GRADE OF ZERO FOR THIS ASSIGNMENT!

def updateVersion(numbers, index):
    numbers[index] = (numbers[index] + 1)
    for i in range((index+1),len(numbers)):
        numbers[i] = 0
    return numbers 


def rightShift(bits, places):
    if places > len(bits):
        bits = bits
    else:
        for i in range(0,places):
            bits.pop()
            bits.insert(0,bits[0])
    return bits


def swapEnds(text, index1, index2):
    if index1 > len(text) or index2 > len(text):
        newtext = text
    elif index1 > index2:
        index1,index2 = index2,index1
        a = text[(index2+1):]
        b = text[index1:(index2+1)]
        c = text[:index1]
        newtext = a + b + c
    else:
        a = text[(index2+1):]
        b = text[index1:(index2+1)]
        c = text[:index1]
        newtext = a + b + c
    
    return newtext


def rpn(sequence):
    numbers = []
    for i in range(0,len(sequence)):
        a = sequence[i].isdigit()
        if a == True:
            numbers.append(sequence[i])
        else:
            op2 = int(numbers[-1])
            numbers.pop()
            op1 = int(numbers[-1])
            numbers.pop()
            if sequence[i] == "+":
                newvalue = op1 + op2
                numbers.append(newvalue)
            elif sequence[i] == "-" :
                newvalue = op1 - op2
                numbers.append(newvalue)
            elif sequence[i] == "*" :
                newvalue = op1 * op2
                numbers.append(newvalue)
            elif sequence[i] == "/" :
                newvalue = op1 / op2
                numbers.append(newvalue)
    if len(numbers) == 1:
        result = int(numbers[0])
    else:
        result = "Error"
    return result


# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE OR REMOVE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    ############### Part 1 Tests ###############
    ver_num = [5,7,2]
    print('Testing updateVersion() for [5, 7, 2] with change index 1...')
    updateVersion(ver_num, 1)
    print("Updated version number is:", ver_num, "\n")

    ver_num = [11, 4, 10, 1, 7, 4]
    print('Testing updateVersion() for [11, 4, 10, 1, 7, 4] with change index 2...')
    updateVersion(ver_num, 2)
    print("Updated version number is:", ver_num, "\n")

    ver_num = [1, 5, 11, 12, 8]
    print('Testing updateVersion() for [1, 5, 11, 12, 8] with change index 4...')
    updateVersion(ver_num, 4)
    print("Updated version number is:", ver_num, "\n")

    # Write your own tests for Part 1 here!
    print()  # prints a blank line

    ############### Part 2 Tests ###############
    digits = [0, 1, 1, 1, 0, 0, 0, 1]
    print('Testing rightShift() for [0, 1, 1, 1, 0, 0, 0, 1] with shift amount 3...')
    rightShift(digits, 3)
    print("Updated list of bits is:", digits, "\n")

    digits = [1, 1, 0, 1, 1]
    print('Testing rightShift() for [1, 1, 0, 1, 1] with shift amount 1...')
    rightShift(digits, 1)
    print("Updated list of bits is:", digits, "\n")

    digits = [0, 0, 1, 0, 1, 1]
    print('Testing rightShift() for [0, 0, 1, 0, 1, 1] with shift amount 10...')
    rightShift(digits, 10)
    print("Updated list of bits is:", digits, "\n")

    # Write your own tests for Part 2 here!
    print()  # prints a blank line

    ############### Part 3 Tests ###############
    print('Testing swapEnds("space: the final frontier", 5, 14): \"', swapEnds("space: the final frontier", 5, 14), "\"", sep='')
    print('Testing swapEnds("these are the voyages", 12, 7): \"', swapEnds("these are the voyages", 12, 7), "\"", sep='')
    print('Testing swapEnds("where no one has gone before", 8, 42): \"', swapEnds("where no one has gone before", 8, 42), "\"", sep='')
    # Write your own tests for Part 3 here!
    print()  # prints a blank line

    ############### Part 4 Tests ###############
    print('Testing rpn() with input sequence "532*+":', rpn("532*+"))
    print('Testing rpn() with input sequence "273-":', rpn("273-"))
    print('Testing rpn() with input sequence "94/12+-":', rpn("94/12+-"))
    # Write your own tests for Part 4 here!
    print() # prints a blank line

