'''
    Author: Wouter Dijkstra
'''
#Practice Exercise 3_2 (functie met list-parameter)
def som(list):
    totaal = 0
    for i in list:
        totaal = totaal + i
    return totaal

list = [5, 10, 15]
print(som(list))
