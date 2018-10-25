# Jiarong Chen 
# 111993420
# Jiarochen
# CSE 101
# Lab 5

# IN THIS PART OF THE FILE, IT IS VERY IMPORTANT THAT YOU *ONLY* WRITE CODE
# INSIDE THE FUNCTION DEFINITIONS BELOW! IF YOU WRITE CODE BETWEEN (AND OUTSIDE)
# THE FUNCTION DEFINITIONSS, THE GRADING SYSTEM WILL NOT BE ABLE TO READ YOUR
# CODE AND YOU WILL RECEIVE A GRADE OF ZERO FOR THIS ASSIGNMENT!

def removeLast(first, second):
    new = first
    n = 1
    for i in range(len(second)):
        for n in range((len(new)-1),-1,-1):
            if second[i] == new[n]:
                new = new[:n] + new[(n+1):]
                break;
    return new
# optional helper function for removeLast() (above)

def excise(text, index):
    return 


def statement(init_balance, transactions):
    for n in range(len(transactions)):
        if transactions[n][0] == "credit":
            init_balance -= transactions[n][1]
        elif transactions[n][0] == "debit":
            init_balance +=  transactions[n][1]
        elif  transactions[n][0] == "interest":
            init_balance = init_balance * (1 + transactions[n][1])
    return init_balance 


def limboScore(scores, contestant):
    total_score = 0
    for n in range(len(scores)):
        if scores[n][0] != contestant:
            total_score += (scores[n][1]*2)
        else:
            total_score += (scores[n][1]+5)
    total_score /= 14
    return total_score


def getHost(url):
    url = url[(url.find("://")+3):]
    if url.find(".com") != -1:
        url = url[:url.find(".com")]
    elif url.find(".edu") != -1:
        url = url[:url.find(".edu")]
    elif url.find(".net") != -1:
        url = url[:url.find(".net")]
    url = url[(url.rfind(".")+1):]
    return url


# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE OR REMOVE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    ############### Part 1 Tests ###############
    print('Testing removeLast("starlord", "thor"):', removeLast("starlord", "thor")) # only some characters appear in first string

    print('Testing removeLast("graymalkin", "rag"):', removeLast("graymalkin", "rag")) # all characters appear in first string

    print('Testing removeLast("Booster Gold", "Aquaman"):', removeLast("Booster Gold", "Aquaman")) # no characters appear in first string

    print('Testing removeLast("Booster", "tber"):', removeLast("Booster Gold", "tber")) 
    # Write your own tests for Part 1 here!
    print()  # prints a blank line

    ############### Part 2 Tests ###############
    print('Testing statement(219.73, [["credit", 102.88], ["credit", 468.64], ["interest", 0.23], ["debit", 128.48]]):')
    print("Final balance:", statement(219.73, [["credit", 102.88], ["credit", 468.64], ["interest", 0.23], ["debit", 128.48]]))
    print()

    print('Testing statement(40.22, [["debit", 474.23], ["interest", 0.32], ["debit", 452.68], ["debit", 158.95], ["interest", 0.34], ["credit", 34.47]]):')
    print("Final balance:", statement(40.22, [["debit", 474.23], ["interest", 0.32], ["debit", 452.68], ["debit", 158.95], ["interest", 0.34], ["credit", 34.47]]))
    print()

    print('Testing statement(1220.61, [["credit", 393.09], ["credit", 62.42], ["credit", 284.84], ["payment", 88.19], ["debit", 153.12], ["payment", 122.98], ["credit", 69.1], ["interest", 0.06]]):')
    print("Final balance:", statement(1220.61, [["credit", 393.09], ["credit", 62.42], ["credit", 284.84], ["payment", 88.19], ["debit", 153.12], ["payment", 122.98], ["credit", 69.1], ["interest", 0.06]]))

    # Write your own tests for Part 2 here!
    print() # prints a blank line

    ############### Part 3 Tests ###############
    print('Testing limboScore([["Kenya", 1.8], ["France", 7.8], ["Ethiopia", 1.4], ["India", 5.7], ["South Korea", 8.9], ["Norway", 3.4], ["Morocco", 4.1]], "Thailand"):')
    print("Final score:", limboScore([["Kenya", 1.8], ["France", 7.8], ["Ethiopia", 1.4], ["India", 5.7], ["South Korea", 8.9], ["Norway", 3.4], ["Morocco", 4.1]], "Thailand"))
    print()

    print('Testing limboScore([["USA", 8.4], ["Finland", 2.5], ["Germany", 7.5], ["Jamaica", 1.5], ["Russia", 3.6], ["Poland", 7.9], ["South Africa", 3.7]], "Egypt"):')
    print("Final score:", limboScore([["USA", 8.4], ["Finland", 2.5], ["Germany", 7.5], ["Jamaica", 1.5], ["Russia", 3.6], ["Poland", 7.9], ["South Africa", 3.7]], "Egypt"))
    print()

    print('Testing limboScore([["Norway", 1.4], ["Aruba", 1.3], ["Russia", 8.4], ["Jamaica", 5.5], ["Spain", 2.6], ["USA", 3.3], ["Morocco", 3.0]], "Spain"):')
    print("Final score:", limboScore([["Norway", 1.4], ["Aruba", 1.3], ["Russia", 8.4], ["Jamaica", 5.5], ["Spain", 2.6], ["USA", 3.3], ["Morocco", 3.0]], "Spain"))
    print()

    # Write your own tests for Part 3 here!
    print()  # prints a blank line

    ############### Part 4 Tests ###############
    print('getHost("irc://foo.com/") returns:', getHost("irc://foo.com/"))
    print('getHost("http://i.am.a.hostname.edu/blah/blah/") returns:', getHost("http://i.am.a.hostname.edu/blah/blah/"))
    print('getHost("ftp://some-like.it-hot.net/something/filename.pdf") returns:', getHost("ftp://some-like.it-hot.net/something/filename.pdf"))

    # Write your own tests for Part 4 here!
    print()  # prints a blank line


