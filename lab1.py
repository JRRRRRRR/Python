# Jiarong Chen
# 111993420
# Jiarochen
# CSE 101
# Lab 1

# In this part of the file it is very important that you write code inside
# the functions only! If you write code in between the functions, then the
# grading system will not be able to read your code and grade your work!

def net_pay(hours, pay_rate, fed_rate, state_rate):
    return (hours*pay_rate*(1-fed_rate-state_rate)) # Replace or modify this line!

def displacement(velocity, acceleration, time_init, time_final):
    return (velocity*(time_final-time_init)+(1/2)*acceleration*(time_final-time_init)**2)  # Replace or modify this line!

def stardate(month, day, year):
    if month==1:
        m=0;
    elif month==2:
        m=31;
    elif month==3:
        m=59;
    elif month==4:
        m=90;
    elif month==5:
        m=120;
    elif month==6:
        m=151;
    elif month==7:
        m=181;
    elif month==8:
        m=212;
    elif month==9:
        m=243;
    elif month==10:
        m=273;
    elif month==11:
        m=304;
    elif month==12:
        m=334;
    return (1000*(year-2323)+((1000/365)*(m+day-1)))# Replace or modify this line!

# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    ############### Part I Tests ###############
    print('net_pay(25, 10, .15, .10) returns', net_pay(25, 10, .15, .10))
    print('net_pay(40, 8, .25, .25) returns', net_pay(40, 8, .25, .25))
    print('net_pay(35, 20, .2, .09) returns', net_pay(35, 20, .2, .09))
    # Write your own tests for this function here!
    print() # prints a blank line

    ############### Part II Tests ###############
    print('displacement(5,2,1,7) returns', displacement(5,2,1,7))
    print('displacement(3,1,4,20) returns', displacement(3,1,4,20))
    print('displacement(18,-3,2,6) returns', displacement(18,-3,2,6))
    # Write your own tests for this function here!
    print() # prints a blank line

    ############### Part III Tests ###############
    print('stardate(2,21,2365) returns', stardate(2,21,2365))
    print('stardate(11,29,2401) returns', stardate(11,29,2401))
    print('stardate(5,4,2390) returns', stardate(5,4,2390))
    # Write your own tests for this function here!
    print() # prints a blank line

