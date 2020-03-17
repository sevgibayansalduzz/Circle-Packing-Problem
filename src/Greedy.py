import math
import sys
import copy
import time

start_time = time.time()

def objective_func(arr,i, j):
    return math.pow(math.pow(arr[i] + arr[j], 2) - math.pow(math.fabs(arr[i] - arr[j]), 2), 0.5)

def generate_matrix(arr):
    matrix = []
    for i in range(len(arr)):
        m_i = []
        for j in range(len(arr)):
            if i == j:
                m_i.append(sys.maxsize)
            else:
                m_i.append(objective_func(arr,i, j))
        matrix.append(m_i)
    return matrix

def make_infinite(matrix,i):
    for k in range(len(matrix[i])):
        matrix[i][k]=sys.maxsize
        matrix[k][i]=sys.maxsize

def greedy(arr):
    matrix=generate_matrix(arr)
    min_width=sys.maxsize
    min_path=[]
    for j in range(len(arr)):
        width=arr[j]
        path=[]
        copy_matrix=copy.deepcopy(matrix)
        start_v=j
        path.append(start_v)
        for k in range(len(arr)-1):
            index=copy_matrix[start_v].index(min(copy_matrix[start_v]))
            width+=min(copy_matrix[start_v])
            make_infinite(copy_matrix,start_v)
            start_v=index
            path.append(start_v)
        width+=arr[start_v]
        if width<min_width:
            min_width=width
            min_path=copy.deepcopy(path.copy())
        final_path=[]
        for i in min_path:
            final_path.append(arr[i])
    return min_width,final_path
#Test1
#print(greedy([50, 2, 4, 10, 30,80,40,15,90]),"greedy")

#Test2
#print(greedy([100,35,40,50,40,70,80,90,85,120]),"greedy")


#TEST 3
#print(greedy([15,25,40,98,54,36,21,49,100,140,7]),"greedy")
# TEST 3
#print(greedy([10,20,30,40,50,60,40,80]),"greedy")


#Open below comment row for displaying running time
#print("--- %s seconds ---" % (time.time() - start_time))

