'''
    Author: Wouter Dijkstra
'''
#Practice Exercise 3_6 (functie met (im)mutable parameter)
def wijzig(list):
    list.clear()
    list.extend(['d', 'e', 'f'])

list = ['a', 'b', 'c']
print(list)
wijzig(list)
print(list)
