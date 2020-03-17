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


def find_neigborhood(arr):
    neigborhood= dict()
    for i in range(len(arr) - 1):
        j = i + 1
        while j < len(arr):
            x = copy.deepcopy(arr)
            temp = x[i]
            x[i] = x[j]
            x[j] = temp
            neigborhood[(arr[i],arr[j])]=(fitness(x),x)
            j += 1
    neigborhood = dict(OrderedDict(sorted(neigborhood.items(), key=itemgetter(1))))
    return neigborhood

def randomPermutation(radius_list):
    perm = copy.deepcopy(radius_list)
    for i in range(len(radius_list)):
        r=i
        while i==r:
            r = random.randint(0,len(radius_list)-1)
        perm[i], perm[r] = perm[r], perm[i]
    return perm

def create_recency_mem(input_circles):
    input_circles.sort()
    tabuList = {}
    for i in range(len(input_circles)-1):
        for j in range(i+1,len(input_circles)):
            if input_circles[i] not  in tabuList:
                tabuList[input_circles[i]] = {}
            tabuList[input_circles[i]][input_circles[j]]=0
    return tabuList



def update_recency_mem(recency_mem,change,local_best,fitness_value,tenure):
    #tabuysa tenureì ata
    for i in recency_mem:
        for j in recency_mem[i]:
            if recency_mem[i][j]>0:
                recency_mem[i][j] -= 1
    #improvement yapıyorsa
    if fitness(local_best) > fitness_value:
        recency_mem[change[0]][change[1]] = tenure

def choose_best(current,recency_mem):

    current_fitnes=fitness(current)
    current_best=copy.deepcopy(current)
    neighbors=find_neigborhood(current_best)

    best=()
    best_fitness=sys.maxsize
    path=[]

    for i in neighbors:
        #if there is an improvement assign negihbors[i] to the best and return
        if neighbors[i][0] < current_fitnes:
            y = i[0] if i[0] < i[1] else i[1]
            z = i[0] if i[0] > i[1] else i[1]
            best = (y, z)
            best_fitness=neighbors[i][0]
            path=neighbors[i][1]
            break;
        else:
            y=i[0] if i[0]<i[1] else i[1]
            z=i[0] if i[0]>i[1] else i[1]
            #tabu değilse ve improvemnt yoksa da ekle.
            if recency_mem[y][z]==0:
                best=(y,z)
                best_fitness=neighbors[i][0]
                path = neighbors[i][1]
                break;
    return  best,best_fitness,path



def tabu_search(input_circles,max_iters,iters,tenure):
    #begin
    tries=0
    recency_mem=create_recency_mem(input_circles)

    global_path=randomPermutation(input_circles)
    #repat until tries==max_iters
    while tries < max_iters:
        local_best=copy.deepcopy(global_path)
        count=0
        #repat until count==iters
        while count < iters:
            change,fitness_value,temp_path=choose_best(local_best,recency_mem)

            update_recency_mem(recency_mem,change,local_best,fitness_value,tenure)

            if fitness_value < fitness(local_best):
                local_best=copy.deepcopy(temp_path)
            count += 1

        tries += 1
        if fitness(local_best) < fitness(global_path):
            global_path=local_best
    print("path: ", global_path," width:",fitness(global_path))




max_iter=7
iter=100
tenure=7

st=time.time()

st=time.time()
tabu_search([10,20,30,40,50,60,70,80],max_iter,iter,tenure)
print("---",time.time()-st," seconds---")


tabu_search([50, 2, 4, 10, 30,80,40,15,90],max_iter,iter,tenure)
print("---",time.time()-st," seconds---\n\n")

st=time.time()
tabu_search([100,35,40,50,45,70,80,90,85,120],max_iter,iter,tenure)
print("---",time.time()-st," seconds---\n\n")

st=time.time()
tabu_search([5, 72, 1, 12, 65, 2, 99, 45],max_iter,iter,tenure)
print("---",time.time()-st," seconds---\n\n")

print(fitness([30, 70, 10, 80, 20, 50, 40, 60]))