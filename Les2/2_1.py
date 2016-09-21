'''
    Author: Wouter Dijkstra
'''
#Practice Exercise 2_1
hourlyRate = input('2_1: Wat verdien je per uur?:')
workedHours = input('2_1: Hoeveel uur heb je gewerkt?:')

reward = int(hourlyRate) * int(workedHours)

print('2_1',workedHours + " uur werken levert " +str(reward)+ " euro op.")
