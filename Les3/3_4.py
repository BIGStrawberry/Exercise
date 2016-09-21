'''
    Author: Wouter Dijkstra
'''
#Practice Exercise 3_4 (functie met if)
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def new_password(old_password, new_pass):
    if (old_password == new_pass):
        return False
    elif (len(new_pass) < 6):
        return False
    elif (hasNumbers(new_pass) == False):
        return False
    else:
        return True

old_password = "oudpasswoord"
new_pass = "nieu3wee"
print(new_password(old_password, new_pass))
