# Dit is geen deel van de opdracht
# Ik probeer hier te kijken of wegingen per parameter nog iets helpt
# Heb maar multithreading gebruikt zodat ik binnen een uur een nuttig aantal combinaties kon testen.

from kNN import findK, scale, genDataSet, genLabels, findLabel, scale2, findminmax
import _thread as trd
import time

#Maak labels aan
labels = genLabels("dataset1.csv", 2000)
validlabels = genLabels("validation1.csv", 2001)

#Maak dataset aan
data = genDataSet("dataset1.csv")
scalers = findminmax(data)

#Functie om voor een bepaalde K een lijst met 7 gewichten voor de 7 parameters te returnen die de hoogste accuraatheid geven
def findKVariableWeighted(combis, labels, validlabels):
    wresults = []
    for combi in combis:
        scaleddata = scale2(genDataSet("dataset1.csv"), scalers, combi)
        scaledvaliddata = scale2(genDataSet("validation1.csv"), scalers, combi)
        classifiedlabels = findLabel(scaleddata, scaledvaliddata, labels, 52) # << Hier voer je bepaalde K in
        correctcounter = 0
        for h in range(len(validlabels)):
            if validlabels[h] == classifiedlabels[h]:
                correctcounter += 1
            wresults.append((correctcounter / len(validlabels) * 100.0, combi))
    wresults.sort(key=lambda tup: tup[0], reverse=True)
    print(wresults[0])
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)

#Combinaties maken
combinations = []
limit = 5
for a in range(1, limit):
        for b in range(1, limit):
            for c in range(1, limit):
                for d in range(1, limit):
                    for e in range(1, limit):
                        for f in range(1, limit):
                            for g in range(1, limit):
                                combinations.append([a, b, c, d, e, f, g])

#Starttijd printen
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)

#8 Threads starten die ieder een deel van de combinaties nalopen en hun beste resultaat printen
#Meer Threads kunnen vanzelfsprekend ook, maar mijn laptop heeft 8 logische kernen dus 8 leek me wel mooi gebalanceerd.
print("starting")
trd.start_new_thread( findKVariableWeighted, (combinations[0:2048], labels, validlabels) )
print("started 1")
time.sleep(5)
trd.start_new_thread( findKVariableWeighted, (combinations[2048:4096], labels, validlabels) )
print("started 2")
time.sleep(5)
trd.start_new_thread( findKVariableWeighted, (combinations[4096:6144], labels, validlabels) )
print("started 3")
time.sleep(5)
trd.start_new_thread( findKVariableWeighted, (combinations[6144:8192], labels, validlabels) )
print("started 4")
time.sleep(5)
trd.start_new_thread( findKVariableWeighted, (combinations[8192:10240], labels, validlabels) )
print("started 5")
time.sleep(5)
trd.start_new_thread( findKVariableWeighted, (combinations[10240:12288], labels, validlabels) )
print("started 6")
time.sleep(5)
trd.start_new_thread( findKVariableWeighted, (combinations[12288:14336], labels, validlabels) )
print("started 7")
time.sleep(5)
trd.start_new_thread( findKVariableWeighted, (combinations[14336:], labels, validlabels) )
print("started 8")

#Houdt parent process van het script aan de gang zodat de child processes van de threads ergens naartoe kunnen printen en geen weeskindjes worden.
while 1:
    pass