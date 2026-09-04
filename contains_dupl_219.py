# Given an integer array nums and an integer k, 
# return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

#Input: nums = [1,2,3,1], k = 3
# outuput : true 

def contain_dupli_219(nums,k):
    hash_map={}
    for index,num in enumerate(nums):
        if num in hash_map and abs(hash_map[num]-index)<=k:
            return True 
        hash_map[num]=index
    return False 


nums = [1,2,3,1]
k = 2
print("Soldution using a hash map without Sliding Window: ",contain_dupli_219(nums,k),"\n")

## Another solution using a sliding window:
## At each step, we maintain a window of at most k+1 elements (indices left..right)
## and check whether it already contains the current element.
## To check for a duplicate, we use a hash set, since insertion, removal,
## and lookup are all O(1) on average. <---- 
## The real question is: how do we keep the window valid? <----check duplicate only in a valid window 
## A valid window means its length must be <= k+1 (i.e., right - left <= k).
## We keep adding elements, and whenever the window becomes too big
## (right - left > k), we remove the leftmost element and move the left pointer forward.
## The right pointer advances automatically with the for loop.

def contain_dupli_sliding_window(nums, k):
    window = set()
    left = 0
    n = len(nums)
    for right in range(n):
        ## shrink the window until it's valid (size <= k+1)
        if right - left > k:
            window.remove(nums[left])
            left += 1
        if nums[right] in window:
            return True
        window.add(nums[right])
    return False


nums = [1,2,3,1]
k = 3
print(f"Solution using a Hash Set with  a valid  Sliding Window , its length<={k}+1: ",contain_dupli_sliding_window(nums,k),"\n")
