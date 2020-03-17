import math
import random
import copy
import time


def fitness(arr):
    width = arr[0]
    for k in range(len(arr) - 1):
        width += math.pow(math.pow(arr[k] + arr[k+1], 2) - math.pow(
            math.fabs(arr[k] - arr[k+1]), 2), 0.5)
        k += 1
    width += arr[k]
    return width



def random_permutation(radius_list):
    if len(radius_list) == 1:
        return radius_list
    perm = copy.deepcopy(radius_list)

    for i in range(len(radius_list)):
        r = i
        while i == r:
            r = random.randint(0, len(radius_list) - 1)
        perm[i], perm[r] = perm[r], perm[i]
    return perm


def rand_two_point(length):
    i = random.randint(0, length)
    j = i
    while i == j:
        j = random.randint(0, length)
    y = i if i < j else j
    z = i if i > j else j

    return y, z

def survivor_selection(population,parents):
    sorted_population = sorted(population, key=lambda tup: tup[1],reverse=True)
    for i in range(len(parents)):
        population[population.index(sorted_population[i])]=(parents[i])


def scramble_mutation(parents):
    for i in range(len(parents)):
        y, z = rand_two_point(len(parents[i][0]) - 1)
        parents[i][0][y:z] = random_permutation(parents[i][0][y:z])
        parents[i] = (parents[i][0], fitness(parents[i][0]))

def crossover(parent1,parent2):
    child=[-1]*len(parent1)
    y,z=rand_two_point(len(parent1)-1)
    child[y:z]=parent1[y:z]
    k=z
    while child[z]==-1:
        if parent2[k] not in child:
            child[z]=parent2[k]
            z+=1
        k+=1
        if z>len(parent1)-1:
           z=0
        if k>len(parent1)-1:
            k=0
    return (child,fitness(child))


def order1_crossover(parents):
    return [crossover(parents[0][0], parents[1][0]), crossover(parents[1][0], parents[0][0])]



def selection(population):
    parents = []
    sumFitness = 0
    for i in population:
        sumFitness += i[1]
    i = 0
    while len(parents) < 2 and i <= 40:
        r = random.uniform(0, sumFitness)
        partialSum = 0
        for ch in population:
            partialSum += ch[1]
            if partialSum >= r:
                parents.append(ch)
                break
        i += 1
    return parents


def create_population(circle_list,size):
    population=[]
    for i in range(size):
        chromosome=random_permutation(circle_list)
        population.append((chromosome,fitness(chromosome)))
    return population

def genetic_algorithm(circle_list,iter,pop_size):
    population=create_population(circle_list,pop_size)
    i = 0;
    while i < iter:
        parents=selection(population)
        if len(parents)<2:
            break
        parents = order1_crossover(parents)
        scramble_mutation(parents)
        survivor_selection(population,parents)
        i += 1
    population = sorted(population, key=lambda tup: tup[1])
    print(population[0])


iter=400
pop_size=10


st=time.time()
genetic_algorithm([10,20,30,40,50,60,70,80],iter,pop_size)
print("---",time.time()-st," seconds---")


st=time.time()
genetic_algorithm([50, 2, 4, 10, 30,80,40,15,90],iter,pop_size)
print("---",time.time()-st," seconds---\n\n")


st=time.time()
genetic_algorithm([100,35,40,50,45,70,80,90,85,120],iter,pop_size)
print("---",time.time()-st," seconds---\n\n")


st=time.time()
genetic_algorithm([15,25,40,98,54,36,21,49,100,140,7],iter,pop_size)
print("---",time.time()-st," seconds---\n\n")

