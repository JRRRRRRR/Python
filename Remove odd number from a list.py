# Remove odd values from a list

def getEvens(numbers):
    save = [ ]
    for i in numbers:
        if i % 2 == 0: # i is even
            save.append(i)
        return save # send back new list

# This version actually change the source list
def removeOdds(numbers):
    #Remove odd numbers as we find
    index = 0
    while index < len(numbers):
        if numbers[index] % 2 == 0:
            index += 1
        else:
           del numbers[index] # numbers[index:index+1] = [ ]
# Password creation
def create_password(a,b,words):
    pwd = ""
    pwd = pwd + str(a)

    # Insert first letters here

    pwd = pwd + str(b)
    return pwd

