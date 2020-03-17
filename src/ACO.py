import copy
import math
import random
import sys
import time
from collections import OrderedDict
from operator import itemgetter



def fitness(arr):
    width = arr[0]
    for k in range(len(arr) - 1):
        width += math.pow(math.pow(arr[k] + arr[k+1], 2) - math.pow(
            math.fabs(arr[k] - arr[k+1]), 2), 0.5)
        k += 1
    width += arr[k]
    return width


def distance(x,y):
    return  math.pow(math.pow(x+ y, 2) - math.pow( math.fabs(x- y), 2), 0.5)


class ACO:
    def __init__(self,ant_size, tmax=400,alpha=4,beta=0.25,rho=0.6,Q=1):
        self.pheromone_delta = []
        self.pheromone = dict()
        self.ant_size = ant_size
        self.t_max = tmax
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.Q=Q

    def heuristic_value(self,x,y):
        return 1/distance(x,y)
    def initialize_pheromone(self,circle_list):
        size=len(circle_list)
        for i in range(len(circle_list) - 1):
            j = i + 1
            while j < len(circle_list):
                self.pheromone[(circle_list[i], circle_list[j])] = 1/(size*size)
                self.pheromone[(circle_list[j],circle_list[i])] = 1/(size*size)
                j += 1

    def evaporate(self):
        for ph in self.pheromone:
            self.pheromone[ph] *= (1-self.rho)
        for ph_delta in self.pheromone_delta:
            for ph in ph_delta:
                self.pheromone[ph] += ph_delta[ph]


    def construct_solution(self,start_circle,circle_list):
        solution=[start_circle]
        arr=copy.deepcopy(circle_list)
        arr.remove(start_circle)
        i=0
        while i < len(arr):
            pij=[]
            for circle in arr:
                p_ij=(self.pheromone[(start_circle,circle)]**self.alpha) * ((self.heuristic_value(start_circle,circle))**self.beta)
                pij.append((start_circle,circle,p_ij))
            min_value=sorted(pij,key=lambda x: x[2])[0]#en büyük proba sahip olanı ekle
            start_circle=min_value[1]
            solution.append(start_circle)
            arr.remove(start_circle)
        return solution


    def delta_update(self,solution):
        pheromone_delta = dict()
        for i in range(len(solution) - 1):
            Lx=fitness(solution)
            pheromone_delta[(solution[i], solution[i+1])] = self.Q / Lx
        return pheromone_delta

    def run(self, circle_list):
        self.initialize_pheromone(circle_list)
        global_solution = None
        global_width=sys.maxsize
        for t in range(self.t_max):
            self.pheromone_delta = []
            for ant in range(self.ant_size):
                start_index = random.randint(0, len(circle_list) - 1)
                solution=self.construct_solution(circle_list[start_index], circle_list)
                self.pheromone_delta.append(self.delta_update(solution))
                width = fitness(solution)
                if  width < global_width:
                    global_solution = copy.deepcopy(solution)
                    global_width = width
            self.evaporate()
        return global_solution, global_width



st=time.time()
x=[10,20,30,40,50,60,70,80]
a=ACO(len(x))
b=a.run(x)
print(b," time",time.time()-st)

st=time.time()
x=[50, 2, 4, 10, 30,80,40,15,90]
a=ACO(len(x))
b=a.run(x)
print(b," time",time.time()-st)

st=time.time()
x=[100,35,40,50,45,70,80,90,85,120]
a=ACO(len(x))
b=a.run(x)
print(b," time",time.time()-st)

st=time.time()
x=[15,25,40,98,54,36,21,49,100,140,7]
a=ACO(len(x))
b=a.run(x)
print(b," time",time.time()-st)



