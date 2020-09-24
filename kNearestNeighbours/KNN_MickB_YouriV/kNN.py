import numpy as np
import copy

#Genereer een dataset uit de gegeven KNMI CSV
def genDataSet(filename: str):
    return np.genfromtxt(filename, delimiter=";", usecols=[1,2,3,4,5,6,7], converters={5: lambda s: 0 if s == b"-1" else float(s), 7: lambda s: 0 if s == b"-1" else float(s)})

#Genereer de seizoenslabels uit de CSV
    dates = np.genfromtxt(filename, delimiter=";", usecols=[0])
    labels = []
    for label in dates:
      if label < (year*10000)+301:
        labels.append("winter")
      elif label < (year*10000)+601:
        labels.append("lente")
      elif label < (year*10000)+901:
        labels.append("zomer")
      elif label < (year*10000)+1201:
        labels.append("herfst")
      else: # from 01-12 to end of year
        labels.append("winter")
    return labels

#Normaliseer de parameters naar een range van 0 tot 100
def scale(datalist, scalers):
    scaleddata = copy.copy(datalist)
    for l in range(len(scaleddata)):
        for s in range(7):
            scaleddata[l][s] -= scalers[s][0] # - minimum
            scaleddata[l][s] /= (scalers[s][1]-scalers[s][0]) # / (max - min)
            scaleddata[l][s] *= 100
    return scaleddata

#Normaliseer de parameters naar een range van 0 tot 100
#Mogelijkheid om 7 gewichten toe te kennen
def scale2(datalist, scalers, combi):
    scaleddata = copy.copy(datalist)
    for l in range(len(scaleddata)):
        for s in range(7):
            scaleddata[l][s] -= scalers[s][0] # - minimum
            scaleddata[l][s] /= (scalers[s][1]-scalers[s][0]) # / (max - min)
            scaleddata[l][s] *= 100
            scaleddata[l][s] *= combi[s]
    return scaleddata

#Vind het minimum en het maximum voor alle 7 parameters en maak er een tupel van
def findminmax(datalist):
    tmp = []
    scalers = []
    for p in range(7):
        tmp = []
        for i in range(len(datalist)):
            tmp.append(datalist[i][p])
        scalers.append((min(tmp), max(tmp)))
    return scalers

#Bereken de afstand tussen twee 7 dimensionale punten
def distance(a, b):
    d = 0
    for i in range(0, 7):
        d += (abs(a[i] - b[i]))**2
    return np.sqrt(d)

#Pakt het meest voorkomende seizoen uit een lijst seizoenen. Recursed als het gelijk spel is.
def labelcounter(labellist):
    wc, hc, lc, zc = 0, 0, 0, 0
    for l in labellist:
        if l[1] == "winter": wc += 1
        elif l[1] == "herfst": hc += 1
        elif l[1] == "zomer": zc += 1
        else: lc += 1
    result = [("winter", wc), ("zomer", zc), ("herfst", hc), ("lente", lc)]
    result.sort(key=lambda tup: tup[1], reverse=True)
    if result[0][1] == result[1][1]:
        return labelcounter(labellist[:-1])
    return result[0][0]

#Vind de optimale K door alle mogelijke K's te proberen en te valideren.
def findK(dataset, validationset, datalabels, validationlabels):
    kresults = []
    validlabeldistances = []
    for v in validationset:
        distances = []
        for i in range(len(dataset)):
            distances.append( (distance((dataset[i]), v), datalabels[i]) )
        distances.sort(key=lambda tup: tup[0])
        validlabeldistances.append(distances)
    for k in range(1, len(dataset)):
        correctcounter = 0
        classifiedlabels = []
        for vld in validlabeldistances:
            classifiedlabels.append(labelcounter(vld[:k]))

        for g in range(len(validationlabels)):
            if validationlabels[g] == classifiedlabels[g]:
                correctcounter += 1
        kresults.append((correctcounter / len(validationlabels) * 100.0, k))

    kresults.sort(key=lambda tup: tup[0], reverse=True)
    for i in range(len(kresults)):
        print(kresults[i][0], kresults[i][1])
    return kresults[0]

#Gebruik een gegeven K om een dataset in KNMI format te classificeren op het seizoen
def findLabel(dataset, validationset, datalabels, k):
    validlabeldistances = []
    classifiedlabels = []
    for v in validationset:
        distances = []
        for i in range(len(dataset)):
            distances.append( (distance((dataset[i]), v), datalabels[i]) )
        distances.sort(key=lambda tup: tup[0])
        validlabeldistances.append(distances)
    for vld in validlabeldistances:
        classifiedlabels.append(labelcounter(vld[:k]))
    return classifiedlabels