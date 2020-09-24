import numpy as np
import copy
import random

random.seed(0)
#Genereer een dataset uit de gegeven KNMI CSV
def genDataSet(filename: str):
    return np.genfromtxt(filename, delimiter=";", usecols=[1,2,3,4,5,6,7], converters={5: lambda s: 0 if s == b"-1" else float(s), 7: lambda s: 0 if s == b"-1" else float(s)})

#Genereer de seizoenslabels uit de CSV
def genLabels(filename: str, year):
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
    for i in range(0, len(a)):
        d += (abs(a[i] - b[i]))**2
    return np.sqrt(d)

def findNearestCentroids(datalist, centroids, clusters):
    for cl in range(len(clusters)):
        clusters[cl] = []
    shortestDistance = float('inf')
    for j in range(len(datalist)):
        for i in range(len(centroids)):
            currentDistance = distance(datalist[j], centroids[i])
            if currentDistance < shortestDistance:
                shortestDistance = currentDistance
                currentCentroid = i
        clusters[currentCentroid].append((currentDistance, datalist[j], j))
        shortestDistance = float('inf')
        currentCentroid = i

def calculateNewCentroids(clusters, oldCentroids):
    tmp = []
    centroids = []
    for j in range(len(clusters)):
        tmp = []
        for i in range(len(clusters[j])):
            tmp.append(clusters[j][i][1])
        if tmp:
            centroids.append(np.mean(tmp, axis = 0))
        else:
            centroids.append(oldCentroids[j])
    return centroids

def labelcounter(cluster, datalist, labels):
    wc, hc, lc, zc = 0, 0, 0, 0
    for l in cluster:
        if labels[l[2]] == "winter": wc += 1
        elif labels[l[2]] == "herfst": hc += 1
        elif labels[l[2]] == "zomer": zc += 1
        else: lc += 1
    result = [("winter", wc), ("zomer", zc), ("herfst", hc), ("lente", lc)]
    result.sort(key=lambda tup: tup[1], reverse=True)
    return result[0][0]
    
def kMeans(datalist, K, labels):
    centroids = []
    clusters = []
    for _ in range(K):
        centroids.append(datalist[random.randrange(len(datalist))])
        clusters.append([])
    while True:
        oldCentroids = copy.copy(centroids)
        findNearestCentroids(datalist, centroids, clusters)
        centroids = calculateNewCentroids(clusters, oldCentroids)
        if np.array_equal(oldCentroids,centroids):
            break
    cl_labels = []
    for cl in clusters:
        cl_labels.append(labelcounter(cl, datalist, labels))
    return clusters, centroids, clusters




