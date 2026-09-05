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

#another syntaxe but still using a hash of fraquence , without sliding window: Using nested if statment 

def contain_dupli_syntaxe(nums,k):
    freq={}
    for index,val in enumerate(nums):
        if val in freq:
            if abs(index-freq[val])<=k:
                return True
        freq[val]=index
    return False 

nums = [1,2,3,1]
k =3
print("Soldution using a hash map without Sliding Window,using another syntaxe: ",contain_dupli_syntaxe(nums,k),"\n")






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
print(f"Solution using a Hash Set with  a valid  Sliding Window , its length<={k}+1:",contain_dupli_sliding_window(nums,k),"\n")


#1----> Create an empty hash set
#2----> Iterate through the array with index i
#3----> If nums[i] is already in the set, return true (duplicate within window)
#4----> Add nums[i] to the set
#5----> If the set size exceeds k, remove nums[i - k] (the element leaving the window)
#6---> If we finish without finding a duplicate, return false.

def contain_dupli_set_slid(nums,k):
    window=set()
    for i,val in enumerate(nums):
        if val in window:
            return True
        window.add(val)
        if len(window)>k:
            window.remove(nums[i-k])
    return False

nums = [1,2,3,1]
k = 3
print("Hash set + sliding Window  another aproach : ",contain_dupli_sliding_window(nums,k),"\n")


## Sliding window based on two pointers approach:
## We use a hash set to represent the current window of elements.
## - `right` scans forward through the array, adding each new element.
## - `left` marks the start of the valid window (of size <= k+1).
## - Whenever the window grows too large (right - left > k),
##   we shrink it from the left by removing nums[left] and advancing left.
## - Before adding nums[right], we check if it's already in the window:
##   if so, we found a duplicate within distance k.

def containsNearbyDuplicate(nums, k):
    window = set()
    left = 0
    right = 0
    n = len(nums)

    while right < n:
        ## shrink the window from the left until it's valid (size <= k+1)
        while right - left > k:
            window.remove(nums[left])
            left += 1

        if nums[right] in window:
            return True

        window.add(nums[right])
        right += 1

    return False

nums = [1,2,3,1]
k = 3
print("Another aproach using a while loop to impliment a sliding window with tow pointers ",containsNearbyDuplicate(nums,k))

