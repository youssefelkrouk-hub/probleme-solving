# maximum subarray : 

def kandan_algo_naive(arrays):
    maxSum=0
    for i in range(len(arrays)):
        currentSum=0
        for j in range(i,len(arrays)):
            currentSum+=arrays[j]
            maxSum=max(maxSum,currentSum)
    return maxSum



L=[-2,1,-3,4,-1,2,1,-5,-4] 
print("Using kandane's algorithme: ",kandan_algo_naive(L),"\n") 

