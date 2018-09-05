def average(a, b, c):
    sum = a + b + c
    return sum/3
first = float(input("Enter a: "))
second = float(input("Enter b: "))
third = float(input("Enter c: "))
print("The average of these values is ",
      average(first, second, third))
print("The average of these values is ",
      average(second, first, third))
print("The average of these values is ",
      average(third, first, second))
