
def naive_way(nums):
    max_sum,n=0,len(nums)
    for i in range(n):
        current_sum=0
        for j in range(i,n):
            current_sum+=nums[j]
            max_sum=max(max_sum,current_sum)
    return max_sum


L=[-2,1,-3,4,-1,2,1] 
print("Naive way : ",naive_way(L),"\n")


# if the current sum<0 , we should ignore it  to start another : 


maxSub=float('-inf')
maxelme=float('inf')
print("the minimum elment :",maxSub<-100000,"\n") # this - infinity
print("the maximum element :",maxelme>100000,"\n") # this + infinity 

def Max_subarray(nums):
    maxSub=float('-inf')
    current_sum=0
    for i  in range(len(nums)):
        current_sum+=nums[i]
        if maxSub<current_sum:
            maxSub=current_sum
        if current_sum<0:
            current_sum=0
    return maxSub
        
L=[-1,-6,-7,-9,-10,-11,-139] 
print("Implmentation of Kandane's algorithm : ",Max_subarray(L),"\n")


def Max_subarray_v2(nums):
    maxSub=nums[0]
    current_sum=nums[0]
    for i in range(1,len(nums)):
        current_sum+=nums[i]
        if maxSub<current_sum:
            maxSub=current_sum
        if current_sum<0:
            current_sum=0
    return maxSub

L=[-1,-6,-7,-9,-10,-11,-139] 
print("  Implmentation of Kandane's algorithm 2 : ",Max_subarray_v2(L),"\n")



def Max_subarray_v4(nums):
    current_sum=maxSub=nums[0]
    for num in nums[1:]:   #Using slicing 
        current_sum=max(current_sum,current_sum+num)
        maxSub=max(maxSub,current_sum)
    return maxSub

L=[-1,-6,-7,-9,-10,-11,139] 
print(" another Implmentation of Kandane's algorithm 3 : ",Max_subarray_v4(L),"\n")





        























