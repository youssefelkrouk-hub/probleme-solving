# Le Boyer–Moore string-search algorithm (1977), utilisé pour rechercher efficacement un motif dans un texte.

# Le Boyer–Moore majority vote algorithm (1981), utilisé pour trouver un élément majoritaire dans une séquence.

# Pour la preméore il exist un problem dans Leetcode qu'il le traite  , de meme pour la deuxiéme sous le nom du Majority voting :


# first  solution : naive way brute force 
# lopper sur haystack et voir si : haystack[i:i+m]==needle
print("cette algorithm seulment pour voir si le text contient un mot ou non \n ")
def contient(haystack, needle):
    n,m=len(haystack),len(needle)
    for i in range(n-m+1):
        if haystack[i:i+m]==needle:
            return True
    return False 

haystack = "abcde"
needle = "cd"
print(contient(haystack,needle))

def contient_loop(haystack,needle):
    n,m=len(haystack),len(needle)
    for i in range(n-m+1):
        j=0
        while j<m and haystack[i+j]==needle[j]:
            j+=1
        if j==m:
            return True 
    return False

print("loop way for looking for a word in a sentence :",contient_loop(haystack,needle),"\n")

haystack = "abcde"
needle = "cd"
    
# --> Leetcode28 : Find the first  Index  of the occurence in a String

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

def leetcode_28(haystack,needle):
    if needle=="":
        return 0
    n,m=len(haystack),len(needle)
    for i in range(n-m+1): # il ya n-m+1  caractére needle  de longeur m dans haystack de longeur n
        j=0 # incrementer ce pointeur tant que il y'a matching des caractéres
        while j<m and haystack[i+j]==needle[j]:  #  this simple mean we compare haystack[i+m] and needle
            j+=1 
        if j==m: #si on est arriver à la fin avec tout les caractére qui match bon on trouver bien le motif dans le text
            return i
    return -1
print("solving the easy 28 leetcode of string matching  :", leetcode_28(haystack,needle),"\n")

haystack = "hello"
needle = "hh"

print("====== Time Complexity is O(n*m) and Space Complexity is O(1) we don't create any new data structure : \n" )

# another way using tow pointers , but the  time complexity is the same :

def tow_pointers(haystack,needle):
    n,m=len(haystack),len(needle)
    # simple case 
    if m==0:
        return 0
    i=0
    while i<m:
        nIndex=0
        j=i
        while j<n and nIndex<m and haystack[j]==needle[nIndex]:
            nIndex+=1
            j+=1
        if nIndex==m:
            return i
        i+=1
    return -1


haystack = "mississippi"
needle = "issip"
print("using sliding window method :",tow_pointers(haystack,needle), "\n")

print(" Boyer–Moore Majority Vote Algorithm Leetcode problem 169 : \n")

# The algorithm is a selection by cancellation method.
# It’s designed to identify a “dominant” element in a sequence without counting every element explicitly.

# General Step : 
# 1. Initialisation : 
  # --> Candidate =None 
  # --> Counter =0
# 2. Iterate through the sequence :
  # if Counter=0 : --> set the current candidate   as the new Candidate 
  # if the current element==Candidate : --> incremente Counter
  # else : --> decremente the Counter

# 3. Results
  # At the end, the Candidate is the element that “survived” all  cancellations.
  # In the majority element problem, this candidate is the one that appears more than half the time.
  # In general, it’s the element that dominates relative to others. 
  # that's mean this the element  , that we do incremente a lot then decremente 


# the brute force aproach  we use to for loop , the first for  fixing a current element , the second for counting the occurence and then compare with the n/2 


def brute_force(nums):
    n=len(nums)
    for i in range(n):
        count=0
        for j in range(n):
            if nums[i]==nums[j]:
                count+=1
        if count>n//2:
            return nums[i]
    return None


nums = [3,2,3]

# solution using hashing 






print(" Majority voting in a list Time Complexity is O(n**2) , Space Complexity is O(1): ",brute_force(nums),"\n")

# Boyer–Moore Majority Vote → 𝑂(𝑛) time, 𝑂(1) space (most efficient).


def Majority_Vonting(nums):
    n=len(nums)
    Candidate=None
    Counter=0
    for Current_Candidate in nums:
        if Counter==0:
            Candidate=Current_Candidate
        if Current_Candidate==Candidate:
            Counter+=1
        else:
            Counter-=1
    return Candidate

nums = [3,2,3,2]
print(" Solution Using Optimized Way , Time Complexity is O(n) , Time complexity is O(1)  ",Majority_Vonting(nums),"\n")

    

def Majority_Vonting_1(nums):
    count,res=0,0
    for n in nums:
        if count==0:
            res=n
        count+=(1 if n==res else -1)
    return res

nums = [3,2,3,2]
print("Using a nest way to incremente the ",Majority_Vonting_1(nums))

# Another method using Hashmap wich is a dict  : with a single loop, but  we need to create a dic wich mean time complexity : O(n)
# Dictionary stores counts for all unique elements
# In summary : Hash map → 𝑂(𝑛) time, 𝑂(𝑛) space. 


def hash_majoriting_voting(nums):
    freq={}
    n=len(nums)
    for num in nums:
        freq[num]=freq.get(num,0)+1
        if freq[num]>n//2:
            return num
    return None
nums = [3,2,3]
print("Solution Usig a Dictinary to store each elment with his frequence: 𝑂(𝑛) time, 𝑂(𝑛) space  ",hash_majoriting_voting(nums),"\n")
    



