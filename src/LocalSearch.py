import copy
import math
import time

from src.Greedy import greedy

start_time = time.time()
def fitness(arr):
    width = arr[0]
    for k in range(len(arr) - 1):
        width += math.pow(math.pow(arr[k] + arr[k+1], 2) - math.pow(
            math.fabs(arr[k] - arr[k+1]), 2), 0.5)
        k += 1
    width += arr[k]
    return width


def find_neigborhood(arr):
    neigborhood = []
    for i in range(len(arr) - 1):
        j = i + 1
        while j < len(arr):
            x = copy.deepcopy(arr)
            temp = x[i]
            x[i] = x[j]
            x[j] = temp
            neigborhood.append(x)
            j += 1
    return neigborhood

def local_search(initial_solution):
    x=initial_solution
    i=0
    while i < 150:
        N = find_neigborhood(x)
        best_neighborhood=x
        for n in N:
            if fitness(n)<fitness(best_neighborhood):
                best_neighborhood=n
        if fitness(best_neighborhood)==fitness(x):
            break
        x=best_neighborhood
        i+=1
    return fitness(x),x


#TEST 1
#initial_solution=greedy([50, 2, 4, 10, 30,80,40,15,90])

#TEST 2
#initial_solution=greedy([100,35,40,50,40,70,80,90,85,120])

#TEST 3
#initial_solution=greedy([15,25,40,98,54,36,21,49,100,140,7])

#TEST 4
#initial_solution=greedy([10,20,30,40,50,60,40,80])

#print(local_search(initial_solution[1]),"local")
#print("--- %s seconds ---" % (time.time() - start_time))

