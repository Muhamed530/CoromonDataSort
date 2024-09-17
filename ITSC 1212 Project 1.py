openFile = open("CoromonDataset.csv", "r")
lines = openFile.readlines()
header = lines[0].strip().split(",")
#print(header)

statsDictionary = {}
for row in lines[1:]:
    stats = row.strip().split(",")
    statsDictionary[stats[0]] = stats
#print(statsDictionary)

"""
-How many Coromons exists.
1. length function
"""
coromonAmount = len(statsDictionary)  
numOfcoromonsinput =  input("do you wanna see the number of coromons?  y or n: ")
if numOfcoromonsinput == "y":
    print("The amount of coromon that exist is:", coromonAmount)
    print()

"""
Select a Coromon randomly and display its information.
"""
userCoromon = input("what Coromons stats would you like to see(I recommend Bearealis he's my favorite): ")
if userCoromon in statsDictionary and userCoromon != "Bearealis":
    print("The coromon you wanted to see:", statsDictionary[userCoromon])
    print()
    print("I'm going to show you Bearealis anyway:)", statsDictionary['Bearealis'])
elif userCoromon not in statsDictionary:
    print("you spelt that wrong.(maybe check capitilization)")
    print()
    print("Also I'm going to show you Bearealis anyway:)", statsDictionary['Bearealis'])
elif userCoromon == "Bearealis":
    print("Great Choice!")
    print("The coromon you wanted to see:", statsDictionary['Bearealis'])
print()
print()

"""
The different types of Coromons.
1. create a list for each type of coromon
2. iterate through the statsDictionary and add each coromon to their specific type
"""
typesOfCoromon = []  
for stats in statsDictionary.values():
    if stats[1] not in typesOfCoromon:
        typesOfCoromon.append(stats[1])
#print(typesOfCoromon)

Normal = []  
Electric = []  
Ghost = []  
Sand = []  
Fire = []  
Ice = []  
Water = []  
darkMagic = []  

for coromon in statsDictionary.values():
    if coromon[1] == "Normal":
        Normal.append(coromon[0])
    elif coromon[1] == "Electric":
        Electric.append(coromon[0])
    elif coromon[1] == "Ghost":
        Ghost.append(coromon[0])
    elif coromon[1] == "Sand":
        Sand.append(coromon[0])
    elif coromon[1] == "Fire":
        Fire.append(coromon[0])
    elif coromon[1] == "Ice":
        Ice.append(coromon[0])
    elif coromon[1] == "Water":
        Water.append(coromon[0]) 
    elif coromon[1] == "Dark Magic":
        darkMagic.append(coromon[0]) 

"""
For each Coromon type display the average value for each of its properties across all of the Coromon that belong to that type.
Take every type of coromon and find the average property of all of the stats
ex. Take the list of normal types and iterate through the list
take the health value of the coromon that is currently being iterated if it belongs to the type in question 
add it to the value of a counter
divide that counter by the number of coromon in the type(length of the list)
display that number as the average for that property
"""
avgNormal = []  
statPosition = 1

for stat in header[2:]:
    statCounter = 0
    statPosition += 1
    for coromon in Normal:
        statCounter += int(statsDictionary[coromon][statPosition])
    avgNormal.append(statCounter / len(Normal))
# print("The averages of the normal coromon:")

avgElectric = []  
statPosition = 1

for stat in header[2:]:
    statCounter = 0
    statPosition += 1
    for coromon in Electric:
        statCounter += int(statsDictionary[coromon][statPosition])
    avgElectric.append(statCounter / len(Electric))
# print("The averages of the electric coromon:",  avgElectric)

avgGhost = []  
statPosition = 1

for stat in header[2:]:
    statCounter = 0
    statPosition += 1
    for coromon in Ghost:
        statCounter += int(statsDictionary[coromon][statPosition])
    avgGhost.append(statCounter / len(Ghost))
# print("The averages of the ghost coromon:",  avgGhost)

avgSand = []  
statPosition = 1

for stat in header[2:]:
    statCounter = 0
    statPosition += 1
    for coromon in Sand:
        statCounter += int(statsDictionary[coromon][statPosition])
    avgSand.append(statCounter / len(Sand))
# print("The averages of the sand coromon:",  avgSand)

avgFire = []  
statPosition = 1

for stat in header[2:]:
    statCounter = 0
    statPosition += 1
    for coromon in Fire:
        statCounter += int(statsDictionary[coromon][statPosition])
    avgFire.append(statCounter / len(Fire))
# print("The averages of the fire coromon:",  avgFire)

avgIce = []  
statPosition = 1

for stat in header[2:]:
    statCounter = 0
    statPosition += 1
    for coromon in Ice:
        statCounter += int(statsDictionary[coromon][statPosition])
    avgIce.append(statCounter / len(Ice))
# print("The averages of the ice coromon:",  avgIce)

avgWater = []  
statPosition = 1

for stat in header[2:]:
    statCounter = 0
    statPosition += 1
    for coromon in Water:
        statCounter += int(statsDictionary[coromon][statPosition])
    avgWater.append(statCounter / len(Water))
# print("The averages of the water coromon:",  avgWater)

avgDarkMagic = []  
statPosition = 1

for stat in header[2:]:
    statCounter = 0
    statPosition += 1
    for coromon in darkMagic:
        statCounter += int(statsDictionary[coromon][statPosition])
    avgDarkMagic.append(statCounter / len(darkMagic))
# print("The averages of the dark magic coromon:",  avgDarkMagic)

elementsAvg = input("Which elements averages would you like to see: ")
print()

if elementsAvg == "Normal" or elementsAvg == "normal":
    counter = 2
    namelistcounter = 0
    print("Here are the average stats for normal:")
    print()
    for avgs in avgNormal:
        print(header[counter], ":", avgs)
        counter+= 1

elif elementsAvg == "Electric" or elementsAvg == "electric":
    counter = 2
    namelistcounter = 0
    print("Here are the average stats for electric:")
    print()
    for avgs in avgElectric:
        print(header[counter], ":", avgs)
        counter+= 1

elif elementsAvg == "Ghost" or elementsAvg == "ghost":
    counter = 2
    namelistcounter = 0
    print("Here are the average stats for ghost:")
    print()
    for avgs in avgGhost:
        print(header[counter], ":", avgs)
        counter+= 1

elif elementsAvg == "Sand" or elementsAvg == "sand":
    counter = 2
    namelistcounter = 0
    print("Here are the average stats for sand:")
    print()
    for avgs in avgSand:
        print(header[counter], ":", avgs)
        counter+= 1

elif elementsAvg == "Fire" or elementsAvg == "fire":
    counter = 2
    namelistcounter = 0
    print("Here are the average stats for fire:")
    print()
    for avgs in avgFire:
        print(header[counter], ":", avgs)
        counter+= 1

elif elementsAvg == "Ice" or elementsAvg == "ice":
    counter = 2
    namelistcounter = 0
    print("Here are the average stats for ice:")
    print()
    for avgs in avgIce:
        print(header[counter], ":", avgs)
        counter+= 1

elif elementsAvg == "Water" or elementsAvg == "water":
    counter = 2
    namelistcounter = 0
    print("Here are the average stats for water:")
    print()
    for avgs in avgWater:
        print(header[counter], ":", avgs)
        counter+= 1

elif elementsAvg == "Dark Magic" or elementsAvg == "dark magic":
    counter = 2
    namelistcounter = 0
    print("Here are the average stats for dark magic:")
    print()
    for avgs in avgDarkMagic:
        print(header[counter], ":", avgs)
        counter+= 1

else:
    print("you spelled that wrong")
print()
print()
print()

avgTypeStatsDict = {}
avgTypeStatsDict['avgNormal'] = avgNormal
avgTypeStatsDict['avgElectric'] = avgElectric
avgTypeStatsDict['avgGhost'] = avgGhost
avgTypeStatsDict['avgSand'] = avgSand
avgTypeStatsDict['avgFire'] = avgFire
avgTypeStatsDict['avgIce'] = avgIce
avgTypeStatsDict['avgWater'] = avgWater
avgTypeStatsDict['avgDarkMagic'] = avgDarkMagic

# print(avgTypeStatsDict)

"""
The Coromon type(s) with the highest average Health Points points.
The Coromon type(s) with the lowest average Health Points points.
The Coromon type(s) with the highest average Attack points.
The Coromon type(s) with the lowest average Attack points.
The Coromon type(s) with the highest average Special Attack points.
The Coromon type(s) with the lowest average Special Attack points.
The Coromon type(s) with the highest average Defense points.
The Coromon type(s) with the lowest average Defense points.
The Coromon type(s) with the highest average Special Defense points.
The Coromon type(s) with the lowest average Special Defense points.
The Coromon type(s) with the highest average Speed points.
The Coromon type(s) with the lowest average Speed points.
"""

maxavglist = []  
maxavgnamelist = []  
minavglist = []  
minavgnamelist = []  
for i in range(len(avgTypeStatsDict.values())-1):  
    maxavg = [0]  
    minavg = [float('inf')]  
    maxavgname = []  
    minavgname = []  
    for coromon, avgs in avgTypeStatsDict.items():  
        if avgs[i] > maxavg[0]:  
            maxavg = [avgs[i]]  
            maxavgname = [coromon]  
        elif avgs[i] == maxavg[0]:  
            maxavg.append(avgs[i])  
            maxavgname.append(coromon)  
    maxavglist.append(maxavg)  
    maxavgnamelist.append(maxavgname)  

    for coromon, avgs in avgTypeStatsDict.items():  
        if avgs[i] < minavg[0]:  
            minavg = [avgs[i]]  
            minavgname = [coromon]  
        elif minavg[0] == avgs[i]:  
            minavg.append(avgs[i])  
            minavgname.append(coromon)  
    minavglist.append(minavg)  
    minavgnamelist.append(minavgname)  
# print("minavglist: ", minavglist)
# print("maxavglist: ", maxavglist)
# print("minavgnamelist: ", minavgnamelist)
# print("maxavgnamelist: ", maxavgnamelist)

userlowestavg = input("do you want to see the list of lowest average stat points that can be found in the elements? y or n: ")  

if userlowestavg == "y":  
    headercounter = 2  
    namelistcounter = 0  
    for minimums in minavglist:  
        print("Lowest average", header[headercounter], "can be found in the" ,(minavgnamelist[namelistcounter]),"element(s) at", minimums,  header[headercounter], "points")  
        headercounter+= 1  
        namelistcounter+= 1  

    print()
    print()

userhighestavg = input("do you want to see the list of highest average stat points that can be found in the elements? y or n:")  

if userhighestavg == "y":  
    headercounter = 2  
    namelistcounter = 0  
    for maximums in maxavglist:  
        print("Highest average", header[headercounter], "can be found in the" ,(maxavgnamelist[namelistcounter]),"element(s) at", maximums,  header[headercounter], ".")  
        headercounter+= 1  
        namelistcounter+= 1  