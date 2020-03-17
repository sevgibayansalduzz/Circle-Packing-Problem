import copy
import random
import time

from src.Greedy import greedy
from src.LocalSearch import local_search, fitness




start_time = time.time()
# Nk of x
def kth_neighborhood(x,k):
    neigborhood = []
    for i in range(len(x)):
        temp_sol = copy.deepcopy(x)
        temp = temp_sol[i]
        temp_sol[i] = temp_sol[(i+k)%(len(x))]
        temp_sol[(i+k)%(len(x))] = temp
        neigborhood.append(temp_sol)
    return neigborhood

def shake(s,k):
    Nk=kth_neighborhood(s,k)
    return Nk[random.randint(0,len(Nk)-1)]

def vns(arr):
    s=greedy(arr)[1]#initial solution
    i=0
    kmax=len(arr)/2 #Ni(α) = Nn−i(α), for i = 1, 2, ..., n, so that maximum value of k is kmax = [n/2].
    while i < 150:
        k=0
        while k <= kmax:
            s1 = shake(s,k) #Generate a point x1  at random from the kth neighborhood of x (x1 ∈ Nk(x))).
            s2 = local_search(s1)[1]
            if fitness(s2) < fitness(s):
                s = copy.deepcopy(s2)
                k = 1
            else:
                k += 1
        i += 1
    return fitness(s),s

#TEST 1
#arr=[50, 2, 4, 10, 30,80,40,15,90]

#TEST 2
#arr=[100,35,40,50,40,70,80,90,85,120]

# TEST 3
arr=[15,25,40,98,54,36,21,49,100,140,7]


#TEST 4
#arr=[10,20,30,40,50,60,40,80]

print(vns(arr),"vns")
print("--- %s seconds ---" % (time.time() - start_time))




