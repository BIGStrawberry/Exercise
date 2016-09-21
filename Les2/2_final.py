'''
    Author: Wouter Dijkstra
'''
# Final Assignment 2

stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk',
            'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch',
            'Eindhoven', 'Weert',
            'Roermond', 'Sittard', 'Maastricht']


#Input station naam
user_start_station = input('Vul a.u.b. een beginstation in: ')
if (user_start_station in stations):
    print('Dit station komt voor in ons bestand.')
    start_station_index = stations.index(user_start_station)
else:
    user_start_station = stations[0]
    print('Dit station komt NIET voor in ons bestand, ', user_start_station, ' geselecteerd.')
    start_station_index = 0

user_end_station = input('Vul a.u.b. uw eindstation in: ')

if (user_end_station in stations):
    end_station_index = stations.index(user_end_station)

    if (start_station_index >= end_station_index):
        print('Dit station komt voor in ons bestand - lengte.')
        end_station_index = len(stations) - 1
        user_end_station = stations[-1]
else:
    user_end_station = stations[-1]
    print('Dit station komt NIET voor in ons bestand, ', user_end_station, ' geselecteerd.')
    end_station_index = len(stations) - 1


# print(stations)
print("")
print("##################################")
print("#######    T I C K E T     #######")
print("##################################")
print("")
print("Het beginstation is ", user_start_station, "en is station nummer",stations.index(user_start_station)+1,"in het traject.")
print("Het eindstation is ", user_end_station, "en is station nummer",stations.index(user_end_station)+1,"in het traject.")
amount_stations = end_station_index - start_station_index
price = 5
print("De afstand bedraagt", amount_stations,"station(s).")
print("De prijs van het kaartje is:", price*amount_stations)
print("Jij stapt in de trein op het station:",user_start_station)
for i in range(start_station_index + 1, end_station_index):
    print('  -', stations[i])
print("Jij stapt uit de trein op het station:",user_end_station)
