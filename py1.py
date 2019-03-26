#Name: Karle Oliva
#Date: March 19, 2019
# This program displays a name organizer

nombres= input("")
allnombres = nombres.split(';')

for c in allnombres:
    temp = c.split(',')
    print(temp[1],temp[0])
