#Test if a number is even or odd
number = int (input("Enter input: "))

if number % 2 == 0: # == means "is equal to"
    print(number, "is even")
else:
    print(number, "is odd")

if number > 5:
    print("Greater than 5")
elif number < 0:
    print("Number is negative")
else:
    print("Number is relatively small")
    
