print("Probleme of Maximum sub array")

class Solution:
    def Max_subarray(array):
        current_sum=array[0]
        max_sum=array[0]
        for j in range(1,len(array)):
            if current_sum<0:
                current_sum=array[j]
            else:
                current_sum+=array[j]
            max_sum=max(max_sum,current_sum)
        return max_sum
    

array=[-2,1,-3,4,-1,2,1,-5,4]
print(Solution.Max_subarray(array))


print("Best Sightseeing Pair")
#version with O(n**2) time complexity
def maxScoreSightseeingPair(values):
    max_pair=0
    n=len(values)
    for i in range(0,n-1):
        for j in range(i+1,n):
            current_score=values[i]+values[j]+i-j
            if current_score>max_pair:
                max_pair=current_score
    return max_pair

values = [8,1,5,2,6]
print(maxScoreSightseeingPair(values))

 
print("En utilisant Kandan's aproch")

class Solution:
    def maxScoreSightseeingPair(values):
        first=values[0]+0
        max_pair=float("-inf")
        for j in range(1,len(values)):
            second=values[j]-j
            max_pair=max(max_pair,second+first)
            first=max(first,values[j]+j)
        return max_pair


values = [8,1,5,2,6]
print(Solution.maxScoreSightseeingPair(values))


def maxScoreSightseeingPair_2(values) :
    # Initialize max_left with first element
    max_left = values[0] + 0
    result = 0


    for j in range(1, len(values)):
        # Calculate score using decomposed formula
        # score = (values[i] + i) + (values[j] - j)
        right_component = values[j] - j
        score = max_left + right_component

        # Update result if better score found
        result = max(result, score)

        # Update max_left for next iteration
        # max_left represents max(values[i] + i) for all i < j
        left_component = values[j] + j
        max_left = max(max_left, left_component)

    return result

values = [8,1,5,2,6]
print(maxScoreSightseeingPair_2(values))


#Define Median of Two Sorted Arrays

#the brute force approach
#// Brute Force:
# // 1.Merge Both Array
# // 2.Sort them
# // 3.Find Median
# // TIME COMPLEXITY: O(n)+O(nlogn)+O(n)
# // SPACE COMPLEXITY: O(1)
#in a sorted array :
#si n =len  alors on trouve la mediane en faisant :
#en affet la median est la valeur centrale qui divise un ensemble de données en deux moitiés égales.
# si n est impair : mediane=arr[n//2] 
# si n est pair : mediane=(arr[n//2-1]+arr[n//2])/2


def findMedianSortedArrays(nums1,nums2):
    merged=nums1+nums2
    merged.sort()
    n=len(merged)
    return (merged[n//2-1]+merged[n//2])/2 if n%2==0 else merged[n//2] 


nums1 = [1, 3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2)) # Output: 2.0



# the optimal approach
# TIME COMPLEXITY: O(log(min(n,m)))
# SPACE COMPLEXITY: O(1)
def findMedianSortedArrays_optimal(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    x, y = len(nums1), len(nums2)
    low, high = 0, x

    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (x + y + 1) // 2 - partitionX

        maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]

        minX = float('inf') if partitionX == x else nums1[partitionX]
        minY = float('inf') if partitionY == y else nums2[partitionY]

        if maxX <= minY and maxY <= minX:
            if (x + y) % 2 == 0:
                return (max(maxX, maxY) + min(minX, minY)) / 2
            else:
                return max(maxX, maxY)
        elif maxX > minY:
            high = partitionX - 1
        else:
            low = partitionX + 1



print("Longest Substring Without Repeating Characters : ","\n")

# 6. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters...

def is_unique(sub): # a helper  function to check the uniquness of charchters in a  subcharcter 
    return len(sub)==len(set(sub))

def substring_longest(sub):
    max_len=0
    n=len(sub)
    for i in range(n):
        for j in range(i,n):
            if is_unique(sub[i:j+1]): # if the slicing the j+1 is not inculuded , that's mean i--->j : 
                max_len=max(max_len,j-i+1)
    return max_len 


s="pwwkew"
print("Space complexity: O(n) — for the temporary slice and the set built inside is_unique.Time complexity is O(n**3) too loop and cheking : ",substring_longest(s) ,"\n")



sub="youssef"
print("slicing doean't includ the last index : ",sub[1:3],"\n")

# Another brute force solution without using  any hekper funtion , but the time complexity O(n**2) , but aligne with the intuition of using a set for the seen characters: 

def bruteforce_substring_longest(s):
    max_len=0
    n=len(s)
    for i in range(n):
        seen=set()
        for j in range(i,n):
            if s[j] in seen:
                break
            seen.add(s[j]) 
            max_len=max(max_len,j-i+1)
    return max_len

s="tmmzuxt"
print("using a set to add the seen character : ",bruteforce_substring_longest(s),"\n")



# Approach 2: Sliding Window + Hash Set
# Intuition
# Maintain a window [left, right] that always contains unique characters. Expand it by moving right forward. When s[right] is already in the window, move left forward and remove characters from the set until the duplicate is gone, then add s[right].

# A hash set holds the characters currently in the window, so the duplicate check is O(1).

def Longets_substring_set(s):
    left,max_len=0,0
    seen=set()
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left+=1
        seen.add(s[right])
        max_len=max(max_len,right-left+1)
    return max_len

s="tmmzuxt" 
print("the optimized solution   using a hash set  : ",Longets_substring_set(s),"\n")

# Instead of re-checking uniqueness from scratch for every substring (which is what made the naive version slow), 
# you keep a running window [left, right] that represents your current substring, and a hash map that tells you instantly whether a character is already inside that window — and where.
# Map key → the character
# Map value → the last index where that character was seen

# Approach 3: Sliding Window + Hash Map (Optimal)
# Intuition
# Replace the set with a hash map that stores the most recent index of each character. On a duplicate, move the left pointer directly past the previous occurrence instead of sliding it one step at a time.



# When s[right] already exists in the map at index prevIndex, set left = max(left, prevIndex + 1). 
# The max matters because left may already be past prevIndex from an earlier jump. 
# Without it, left could move backward and re-include a character that was already removed from the window. 
# Concretely, in "abba": after processing the second b, left is at index 2; 
# reaching the final a finds its previous index 0, and max(2, 0 + 1) keeps left at 2 rather than rewinding to 1.


def longest_substring(s):
    left,max_len=0,0
    seen_map={}
    for right,ch in enumerate(s):
        if ch in seen_map and seen_map[ch]>=left:
            left=seen_map[ch]+1
        seen_map[ch]=right   # else : add ch and his index to the seen_map 
        max_len=max(max_len,right-left+1)   # always modify the max_len by the max between max_len and right-left+1
    return max_len

s="tmmzuxt" 
print("the optimized solution   using a hash map table : ",longest_substring(s),"\n")


print("another way ","\n")

def longest_substring_2(s):
    last_index={}
    left,max_len=0,0
    for right,c in enumerate(s):
        if c in last_index and last_index[c]>=left:
            left=last_index[c]+1
        last_index[c]=right
        max_len=max(max_len,right-left+1)
    return max_len

s="tmmzuxt" 
print("Using a map : ",longest_substring_2(s),"\n")


