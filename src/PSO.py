import copy
import math
import random
import sys
import time

def convert(original,pos):
    arr = [-1] * len(original)
    for i, index in enumerate(pos):
        arr[index] = original[i]
    return arr


def fitness(original,pos):
    arr=[-1]*len(original)
    for i,index in enumerate(pos):
        arr[index]=original[i]
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

def create_population(circle_list, size):
    index_list=[]
    for i in range(len(circle_list)):
        index_list.append(i)
    population = []
    for i in range(size):
        chromosome = random_permutation(index_list)
        population.append(chromosome)
    return population


class Particle:
    def __init__(self,pos,original):
        self.pos=pos
        self.velocity=[1]*len(pos)
        self.fitness=fitness(original,self.pos)
        self.p_best=pos
        self.original=original

    def update_velocity(self,velocity):
        self.velocity=copy.deepcopy(velocity)

    def update_pos(self,pos):
        usage=[None]*len(pos)
        sort_pos=sorted(pos)
        for i in range(len(sort_pos)):
            indices = [t for t, x in enumerate(pos) if x == sort_pos[i]]
            for index in indices:
                if usage[index]==None:
                    usage[index]=i
                    break;
        self.pos=usage

    def update_pbest(self):
        temp=fitness(self.original,self.pos)
        if temp < self.fitness:
            self.p_best = copy.deepcopy(self.pos)
            self.fitness = temp


class PSO:
    def __init__(self,circle_list):
        self.w, self.c1, self.r1, self.c2, self.r2 = 0.8, 0.9, random.uniform(0, 1), 0.9, random.uniform(0, 1)
        population=create_population(circle_list,60)
        self.particles=[]
        for p in population:
            self.particles.append(Particle(p,circle_list))
        self.circle_list=circle_list

    def min_particle(self):
        for p in self.particles:
            p.fitness=fitness(self.circle_list,p.pos)
        best_p=[]
        min=sys.maxsize
        for p in self.particles:
            if min>p.fitness:
                best_p=copy.deepcopy(p.pos)
        return best_p


    def calculate_velocity(self,particle):
        temp_divers = [self.w * vi for vi in particle.velocity]
        temp_inten1 = [self.c1 * self.r1 * (pi - xi) for pi, xi in zip(particle.p_best , particle.pos)]
        temp_inten2 = [self.c2 * self.r2 * (gi - xi) for gi, xi in zip(self.g_best , particle.pos)]
        velocity = [x+y+z for x,y,z in zip(temp_divers,temp_inten1,temp_inten2)]
        return velocity

    def calculate_pos(self,particle):
        temp=[x + y for x,y in zip(particle.pos,particle.velocity)]
        return temp

    def run(self,MAX_ITER):
        iter=0
        self.g_best=self.min_particle()
        while iter<MAX_ITER:
            for particle in self.particles:
                particle.update_velocity(self.calculate_velocity(particle))
                particle.update_pos(self.calculate_pos(particle))
                particle.update_pbest()
                #update global
                if fitness(self.circle_list,self.g_best)>fitness(self.circle_list,particle.pos):
                    self.g_best=copy.deepcopy(particle.pos)
            iter+=1
        return fitness(self.circle_list,self.g_best),"   sol:",convert(self.circle_list,self.g_best)


st=time.time()
pso=PSO([10,20,30,40,50,60,70,80])
print("weight: ",pso.run(200) ,"  time:",time.time()-st)
st=time.time()


pso=PSO([50, 2, 4, 10, 30,80,40,15,90])
print("weight: ",pso.run(200) ,"  time:",time.time()-st)


st=time.time()
pso=PSO([100,35,40,50,45,70,80,90,85,120])
print("weight: ",pso.run(200) ,"  time:",time.time()-st)


st=time.time()
pso=PSO([15,25,40,98,54,36,21,49,100,140,7])
print("weight: ",pso.run(200) ,"  time:",time.time()-st)


