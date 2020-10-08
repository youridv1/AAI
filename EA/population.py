import random
import copy
import numpy
import time

random.seed(time.time())

def individual(length, min, max):
    return [ random.randint(min, max) for x in range(length) ] # return random individual of given length and range

def population(count, length, min, max):
    return [ individual(length, min, max) for x in range(count) ] # return random population of given count with individuals made by individual()

def fitness(individual, target = (36, 360)): # determine fitness based on absolute difference between target and answer of individual
    piles = [0, 1]                           #TO DO: make length of target variable instead of always 2 (which is convenient for the cards problem)
    for i in range(len(individual)):
        if individual[i]:
            piles[1]*=(i+1)
        else:
            piles[0] += (i+1)
    # print("piles:", piles)
    return (abs(piles[0]-target[0])) + (abs(piles[1]-target[1]))

def grade(population, target = (36, 360)):  # determine average fitness of population for some reason
    grade = [fitness(x, target) for x in population]
    return sum(grade)/len(population)

def bitmutation(individual, chance): # mutate the values of the genotype a given fraction of the time
    for i in range(len(individual)):
        if random.random() < chance:
            individual[i] = individual[i] != 1
    return individual

def mutationloop(population, chance):   # mutate the population using bitmutation
    for i in range(len(population)):
        population[i] = bitmutation(population[i], chance)
    return population

def crossover(p1, p2): # make babies
    child = []
    if len(p1) != len(p2):
        print("downsyndroom")
    for i in range(len(p1)):
        if random.random() < 50:
            child.append(p1[i])
        else:
            child.append(p2[i])
    if len(child) != len(p1) or len(child) != len(p2):
        print("downkind")
    return child

def parentselection(population, poolsize, target = (36, 360)): # select parents out of population according to tournament selection
    temp = []
    tournament = []
    popcop = copy.copy(population)
    while popcop:
        for _ in range(min([poolsize, len(popcop)])):
            index = random.randint(0, len(popcop)-1)
            # print(index, len(popcop))
            temp.append(popcop.pop(index))
        tournament.append(temp)
        temp = []
        
    #tournament
    parents = []
    temp2 = []
    for pool in tournament:
        for contender in pool:
            temp2.append(fitness(contender, target)) # bereken de fitness van de peeps in de pool
        parents.append(pool[temp2.index(min(temp2))]) # vind de index van de guy met de beste fitness en gebruik deze om hem aan de parents te appenden
        temp2 = []
    return parents

def newpopulation(parents, populationsize):
    parcop = copy.copy(parents)
    newpop = []
    while len(newpop) < populationsize - len(parents):
        p1 = random.randint(0, len(parcop)-1)
        p2 = random.randint(0, len(parcop)-1)
        if p1 == p2:
            continue
        newpop.append(crossover(parcop[p1], parcop[p2]))
    return parents + newpop # lelijk maar het doet wat het moet doen

def answer(population):
    results = []
    for individual in population:
        results.append((fitness(individual), individual))
    results.sort(key=lambda x:x[0])
    return results[0]
    
        
