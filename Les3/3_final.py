'''
    Author: Wouter Dijkstra
'''
#Final Assignment 3
def standaardprijs(afstandKM):
    if (afstandKM < 0):
        afstandKM = 0

    if (afstandKM < 50):
        price = 0.80 * afstandKM
        return price
    else:
        price = 15 + (0.60 * afstandKM)
        return price

def getDiscount(prijs, korting):
    newPrice = prijs - (prijs * (korting/100))
    return str(round(newPrice,2))

def ritprijs(leeftijd, weekendrit, afstandKM):
    if(leeftijd < 0):
        leeftijd = 0

    basePrice = standaardprijs(afstandKM)

    if (leeftijd > 11 and leeftijd < 65):
        if (weekendrit == False):
            return getDiscount(basePrice, 0) + str(" (0% korting)")
        else:
            return getDiscount(basePrice, 40) + str(" (40% korting)")
    else:
        if(weekendrit == False):
            return getDiscount(basePrice, 30) + str(" (30% korting)")
        else:
            return getDiscount(basePrice, 35) + str(" (35% korting)")


print("#")
print("11 en niet weekend", ritprijs(11, False, 55))
print("12 en niet weekend", ritprijs(12, False, 55))
print("64 en niet weekend", ritprijs(64, False, 55))
print("65 en niet weekend", ritprijs(65, False, 55))
print("#")
print("11 en wel weekend", ritprijs(11, True, 55))
print("12 en wel weekend", ritprijs(12, True, 55))
print("64 en wel weekend", ritprijs(64, True, 55))
print("65 en wel weekend", ritprijs(65, True, 55))
print("#")
print("11 en wel weekend", ritprijs(11, True, -10))
print("12 en wel weekend", ritprijs(12, True, 40))
print("64 en wel weekend", ritprijs(-10, True, 55))
print("65 en wel weekend", ritprijs(65, True, 55))
