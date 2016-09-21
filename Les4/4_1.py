'''
    Author: Wouter Dijkstra
'''
#Practice Exercise 4_1 (formatting)
def convert(tempCelcius):
    return (tempCelcius * 1.8) + 32

def table(steps):
    temp = -30
    print(" C", "   F")
    while(temp < 40):
        print("%d, %d" % (temp,int(convert(temp))))
        temp += steps

table(10)



