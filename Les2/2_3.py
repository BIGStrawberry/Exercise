'''
    Author: Wouter Dijkstra
'''
#Practice Exercise 2_3 (if met 2 booleaanse operators)
age = input('2_3: Geef je leeftijd:')
dutchPassport = input('2_3: Nederlands paspoort?:')

if (int(age) and dutchPassport == 'ja'):
    print('2_3:','Gefeliciteerd, je mag stemmen!')
else:
    print('2_3:','Balen, je mag NIET stemmen!')
