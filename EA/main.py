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
        result = main(100, 4096, 0.0001)
        print(result)
        results.append(result[0])
    print("average:", s.mean(results))
    print("min:", min(results))
    print("max:", max(results))
    print("median:", s.median(results))
    print("mode:", s.mode(results))
    print("st deviation:", s.stdev(results))
    print("variance:", np.var(results))
