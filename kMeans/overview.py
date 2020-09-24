import numpy as np
import copy
import random

def genDataSet(filename: str)
    """
    Functie die een dataset maakt uit een KNMI CSV file zoals aangegeven in de opdrachtbeschrijving op Canvas
    """    

def genLabels(filename: str, year)
    """
    Genereert een lijst met de bijbehorende seizoenen voor de dataset van het KNMI
    """

def scale(datalist)
    """
    Schaal de parameters van 0 tot 100
    """

def scale2(datalist, scales)
    """
    Schaal de parameters van 0 tot 100 waar je een gewicht aan kan toevoegen
    """

def findminmax(datalist)
    """
    Bepaal per parameter van de 7 het minimum en het maximum
    """

def distance(a, b)
    """ 
    Bereken de afstand tussen twee 7 dimensionale coordinaten
    """

def labelcounter(cluster, datalist, labels)
    """
    Pakt per cluster het meest voorkomende seizoen uit een lijst met seizoenen
    """

def kMeans(datalist, K, labels)
    """
    Run het kMeans algoritme met de gekozen K aantal clusters, geeft de clusters en de centroids terug in lijsten
    """

def calculateNewCentroids(clusters, oldCentroids)
    """
    Bereken nieuwe centroids op basis van de coordinaten van de metingen in de clusters
    """

def findNearestCentroids(datalist, centroids, clusters)
    """
    Bereken per meting de afstanden tot alle centroids en voeg de meting toe aan het cluster van de dichtsbijzijnde centroid
    """

import kMeans as km

#Genereer de dataset
dataset = km.genDataSet("dataset1.csv")

#Genereer de labels
labels = km.genLabels("dataset1.csv", 2000)

#Vind de scalers
scalers = km.findminmax(dataset)

#Scale de data
scaleddata = km.scale(dataset, scalers)


results = []
tmp = 0
for k in range(2, 50):
    results = []
    for _ in range(10):     #Doe 10 keer kMeans om de randomness van het kiezen van de centroids eruit te halen.
        clusters, _, _ = km.kMeans(scaleddata, k, labels)  
        total = 0
        for l in clusters:
            for m in l:
                total += m[0]
        results.append(total)
    tmp = min(results)  #Kies het resultaat met de laagste aggregate intra-clustur distance
    print(k, tmp / k)


