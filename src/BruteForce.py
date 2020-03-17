import math
import time

start_time = time.time()

def swap(arr,r1,r2):
    temp=arr[r1]
    arr[r1]=arr[r2]
    arr[r2]=temp

def brute_force(arr, i, n,min_width,arr_order):
    if i == n:
        width = arr[0]
        for k in range(0, len(arr)-1):
            width += math.pow(math.pow(arr[k] + arr[k + 1], 2) - math.pow(math.fabs(arr[k] - arr[k + 1]), 2), 0.5)
            k += 1
        width += arr[k]
        min_width.append(width)
        arr_order.append(arr.copy())
    else:
        j=i
        while j<=n:
            swap(arr, i, j)
            brute_force(arr, i + 1, n,min_width,arr_order)
            swap(arr, i, j);
            j+=1

def circle_packing(arr):
    min_width=[]
    arr_order=[]
    brute_force(arr, 0, len(arr) - 1,min_width,arr_order)
    index= min_width.index(min(min_width))
    return min_width[index],arr_order[index]



#TEst 1
#width,order=circle_packing([50, 2, 4, 10, 30,80,40,15,90])


#Test 2
#width,order=circle_packing([100,35,40,50,40,70,80,90,85,120])

#Test 3
#width,order=circle_packing([15,25,40,98,54,36,21,49,100,140,7])

#Test 4
#width,order=circle_packing([10,20,30,40,50,60,70,80])

#print("width: ", width,"\norder: ",order)
#print("--- %s seconds ---" % (time.time() - start_time))

