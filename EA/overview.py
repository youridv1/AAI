def individual(length, min, max):
    """
    return random individual of given length and range 
    """

def population(count, length, min, max):
    """
    Return random population of given count with individuals made by individual()
    """

def fitness(individual, target = (36, 360)):
    """
    determine fitness based on absolute difference between target and answer of individual
    """

def grade(population, target = (36, 360)):  
    """
    determine average fitness of population
    Calls fitness for every individual
    """

def bitmutation(individual, chance): 
    """
    mutate the values of the genotype a given fraction of the time
    """

def mutationloop(population, chance):
    """
    mutate the population using bitmutation
    Calls bitmutation for every individual in a loop
    """

def crossover(p1, p2):
    """
    Crossover 2 individuals choosing which bit to adapt based on a 50/50 chance
    """

def parentselection(population, poolsize, target = (36, 360)):
    """
    Select parents out of population according to tournament selection
    Every parent that made it out his pool, gets returned
    """

def newpopulation(parents, populationsize): 
    """
    Newpopulation calls crossover on randomly selected parents until the populationsize is met
    """

def answer(population):
    """
    Call answer on every individual and append to a list. Then sort the list on fitness
    """

# main.py

import population as pn
import statistics as s
import numpy as np

def main(generations, populationsize, chance):
    population = pn.population(populationsize, 10, 0, 1)
    for _ in range(generations):
        parents = pn.parentselection(population, 4)
        population = pn.newpopulation(parents, populationsize)
        population = pn.mutationloop(population, chance)
    return pn.answer(population)


if __name__ == "__main__":
    results = []
    for _ in range(100):
        result = main(400, 2048, 0.0001)
        print(result)
        results.append(result[0])
    print("average:", s.mean(results))
    print("min:", min(results))
    print("max:", max(results))
    print("median:", s.median(results))
    print("mode:", s.mode(results))
    print("st deviation:", s.stdev(results))
    print("variance:", np.var(results))
