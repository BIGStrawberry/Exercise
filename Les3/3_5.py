'''
    Author: Wouter Dijkstra
'''
import math
#Practice Exercise 3_5 (functie met list-parameter en for-loop)
def kwadraten_som(grondgetallen):
    totaal = 0
    for i in grondgetallen:
        if (i > 0):
            powah = math.pow(i,2)
            totaal = totaal + powah
    return totaal

grondgetallen = [2, 4, 5, -5]
print(kwadraten_som(grondgetallen))
