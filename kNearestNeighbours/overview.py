from kNN import findK, scale, genDataSet, genLabels, findLabel, scale2
import numpy as np
import copy

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

def labelcounter(labellist)
    """
    Pakt het meest voorkomende seizoen uit een lijst met seizoenen
    """

def findK(dataset, validationset, datalabels, validationlabels)
    """
    Test K van 1 tot en met de lengte van de dataset en return een tuple van de beste K en zijn accuraatheid tijdens validatie
    """
    
def findLabel(dataset, validationset, datalabels, k)
    """
    Klassificeert de gegeven metingen van de dataset met de gekozen K in seizoenen
    """

#Gewichten gevonden door brute force met experiment.py
weights = [1, 1, 2, 4, 2, 1, 3]

#generate dataset, validationset and testset
data = genDataSet("dataset1.csv")

scalers = findminmax(data)

scaleddata = scale2(data, scalers, weights)
scaledvaliddata = scale2(genDataSet("validation1.csv"), scalers, weights)
scaledtestdata = scale2(genDataSet("days.csv"), scalers, weights)

#generate labels for aformentioned sets
labels = genLabels("dataset1.csv", 2000)
validlabels = genLabels("validation1.csv", 2001)

#Vind de optimale K en de accuraatheid en sla deze beide op
accuracy, optimalK = findK(scaleddata, scaledvaliddata, labels, validlabels)

#Klassificeer de days.csv dataset en print deze uit samen met de gebruikte k en accuraatheid tijdens validatie van de k
print(findLabel(scaleddata, scaledtestdata, labels, optimalK))
print("Used K: ", optimalK)
print("Accuracy validationset: ", accuracy)