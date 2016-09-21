'''
    Author: Wouter Dijkstra
'''

# Practice Exercise 1_1 (expressions)
print(
'''Practice Exercise 1_1 (expressions)
| Expression    | Uitkomst      | Type          |
| 5             |   5           | Integer       |
| 5.0           |   5.0         | Float         |
| 5%2           |   1           | Integer       |
| 5>1           |   True        | Boolean       |
| '5'           |   '5'         | String        |
| 5*2           |   10          | Integer       |
| '5' * 2       |   '55'        | String        |
| '5' + '2'     |   '52'        | String        |
|  5/2          |    2.5        | Float         |
|  5//2         |    2          | Integer       |
|  [5, 2, 1]    |  [5, 2, 1]    | List          |
|5 in [1, 4, 6] |   False       | Boolean       |
''')

#Practice Exercise 1_2 (strings)
myName = "Wouter Dijkstra"
myAddress = "Elzenlaan 4"

result = "Mijn naam is " + myName + " en mijn adres is " + myAddress + "."
print('1_2:', result)

#Practice Exercise 1_3 (strings)

#1_3_a
a = "Supercalifragilisticexpialidocious"
print('1_3_b:', "Het aantal letters in het woord zijn: " + str(len(a)))

#1_3_b
b = "ice"
print('1_3_b: ', b in a)

#1_3_c
wordOne = "Antidisestablishmentarianism"
wordTwo = "Honorificabilitudinitatibus"

if (len(wordOne) > len(wordTwo)):
    print('1_3_c: ',"Antidisestablishmentarianism is groter")
else:
    print('1_3_c: ',"Honorificabilitudinitatibus is groter")

#1_3_d
componisten = ['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']
componisten.sort()
print('1_3_d: ', componisten[0])

# Practice Exercise 1_4 (getallen)

cijferICOR = 7.5
cijferPROG = 9.31111
cijferCSN = 8.5

average = (cijferICOR+cijferPROG+cijferCSN) / 3
reward = (average * 30)*3
print('1_4: ' , "Mijn cijfers (gemiddeld een " +str(round(average, 1))+ ") leveren een beloning van EUR"+str(round(reward, 2))+" op!")

#Practice Exercise 1_5 (lists)
#1_5_1
favorieten = ['Jan Smit']

#1_5_2
favorieten.append('Nick Bout')

#1_5_3
favorieten[1] = 'Bob Thomas'
print('1_5: ', favorieten)
