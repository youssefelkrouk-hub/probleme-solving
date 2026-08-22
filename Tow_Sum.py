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


# The tow_sum problem || , now the arrays is sorted : 
from typing import List

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
    return []


nums = [2, 7, 11, 15]
target = 9
print("Using tow Pointers to solve the tow sum for an array that is sorted ",print(tow_sum_2(nums,target)),"\n")