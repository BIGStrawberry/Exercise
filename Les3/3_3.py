'''
    Author: Wouter Dijkstra
'''
#Practice Exercise 3_3 (functie met if)
def langGenoeg(length):
    if(length>120):
        return ("Je bent lang genoeg voor de attractie!")
    else:
        return ("Sorry, je bent te klein!")

lengte = 118
print(langGenoeg(lengte))
