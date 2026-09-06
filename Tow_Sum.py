# Brute  force search : 
def brute_force(nums,target):
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                return [i,j]
    return []

nums = [3,2,4]
target = 6
print("Tow Sum Problem using a brute force way:",brute_force(nums,target),"\n")



def tow_sum(nums,target):
    map={}
    for index,number in enumerate(nums):
        compliment=target-number # the compliment to add to the number , and check if it's exist in the map 
        if compliment in map: #real check if it's exist in the map 
            return [map[compliment],index] 
        map[number]=index # if no, add or insert the (key,value)=(number,index)
  
nums = [2, 7, 11, 15]
target = 9
print("The optimized way using Hashmap , where time complexity O(n),adn space complexity O(n) : ",tow_sum(nums,target),"\n")


# The tow_sum problem || , now the arrays is sorted : usiin tow pointers technique 

def tow_sum_2(numbers,target):
    n,m=0,len(numbers)-1
    while n<m:
        current_sum=numbers[n]+numbers[m]
        if current_sum==target:
            return [n+1,m+1]
        elif current_sum<target:
            n+=1
        else:
            m-=1
    return [-1,-1]


nums = [2, 7, 11, 15]
target = 9
print("Using tow Pointers to solve the tow sum for an array that is sorted ",print(tow_sum_2(nums,target)),"\n")


# Tow SUM || : Sorted Array 
# ------> Intuition  <----------: 
# Aproach 2: using a  binary search : 
# Fix one element and search for its complement. 
# For each numbers[i], 
# the value we need is complement = target - numbers[i]. 
# Since the array is sorted, 
# a binary search on the portion after index i finds that complement in O(log n) 
# instead of the O(n) linear scan.  with a simple for loop  ! 


def tow_sum_binary_search(nums,target):
    n=len(nums)
    for i in range(n-1):
        complement=target-nums[i]
        left,right=i+1,n-1
        while left<=right:
            mid = (left + right) // 2
            if nums[mid]==complement:
                return [i+1,mid+1]
            elif nums[mid]<complement:
                left=mid+1
            else:
                right=mid-1 
    return [-1,-1]
                
nums=[-3,-1,0,2,4,6]
target=3
print("Using Binary search to catch the complement that w'ill add up with val = Target :  ",tow_sum_binary_search(nums,target),"\n")







def tow_sum(nums,target):
    map={}
    for num in nums:
        compliment=target-num 
        if compliment in map: 
            return [num,compliment]
        map[num]=compliment

nums=[4,7,1,9,3]
target=10
print("returnig the element not  only the index  using a  hashmap: ",tow_sum(nums,target) ,"\n")


def tow_sum(nums,target):
    map=set()
    for num in nums:
        compliment=target-num 
        if compliment in map: 
            return [num,compliment]
        map.add(num)

nums=[4,7,1,9,3]
target=10
print("returnig the element not  only the index  using a hash set : ",tow_sum(nums,target) ,"\n")