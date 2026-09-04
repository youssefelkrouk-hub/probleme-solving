# Given an integer array nums, return True if any value appears at least twice, and False if
# every element is distinct.

def contains_duplicate_map_1(nums):
    seen={}   # this way is  to initialize a empty dictionary not a set, for set we use : s=set()
    for index,num in enumerate(nums):
        if num in seen: 
            return [True,index]
        seen[num]=index 
    return [False,None] 
        
nums=[1,2,3,4]
print("using a map to store each number with his index  , with a list format [if exist,the index of this elemnt where his congurence]:",contains_duplicate_map_1(nums),"\n")

def contains_duplicate_map_2(nums):
    map={}

    for num in nums:
        if num in map and map[num]>=1:
            return True
        map[num]=map.get(num,0)+1 # if we want to start with zero 
    return False
nums=[1,2,2,4]
print("using a map table , wich the value is number of occurence of each elment of the list : ",contains_duplicate_map_2(nums),"\n")

def contains_duplicate_map_3(nums):
    map={}
    for num in nums:
        map[num]=map.get(num,0)+1 # this method check if the element is in the  map , if not return 0, if yes it return the map[num] of  this num 
        if map[num]>1:
            return True
    return False
nums=[1,2,2,4]
print("using a map table , wich the value is number of occurence of each elment of the list count first then compare later : ",contains_duplicate_map_3(nums),"\n")
# Using an alternative of the map.get(nu,default) method
def contains_duplicate_map_4(nums):
    Counts={}
    for num in nums:
        if num in Counts:
            Counts[num]+=1
        else:
            Counts[num]=1
        return Counts[num]>=1
    
nums=[1,2,2,1]
print("Using an alternative of the map.get(num,default) method:",contains_duplicate_map_4(nums),"\n")


def contains_duplicate_set(nums):
    seen=set()
    for num in nums:
        if num in seen:
            return True
    return False

nums=[1,2,2,3,4]
print(" using a set to store each number with his index :  ",contains_duplicate_set(nums),"\n")


from collections import Counter 
def contains_duplicate_collections(nums):
    nums=Counter(nums)
    for num in nums:
        if nums[num]>1:
            return True 
    return False

num=[1,1,2,3,4]
print("usgin  collection.counter  in python ",contains_duplicate_collections(nums),"\n")

# all of those solution use an extra memory : 

def contains_duplicate(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i]==nums[i+1]:
            return True
    return False

nums=[1,4,3,1]
print("usinf  a quick sort that python use in the backend  to sort the list ,then check if there is any duplicate O(nlog(n)+n)=O(nlogn):",contains_duplicate(nums),"\n")



# the last idea is  using  Converting a list into a set : wich cost O(n)  , and then compare with the len of the originial list
# s=set(my_list) which the same as : {x for x in my_list} nested list

def last_contain_duplicate(nums):
    return len({num for num in nums})!=len(nums)



nums=[1,3,2,34,1]
print("Converting a list into a set technique : ",last_contain_duplicate(nums))









s = set([1, 2, 2, 3, 3, 3, 4])
print("set doean't support the duplicate ,wich enforce  the data-structure",s)   # {1, 2, 3, 4}
print("Set (mutable) ✅ : elements can be added or removed after creation ","\n")
s = set([1, 2, 2, 3])   # {1, 2, 3} eliminate duplicate , no duplicate  for a set , 
print(s,"\n")
s.remove(1) # set is Mutable u can  remove , add any value you want
print(s,"\n")
s.pop()           # removes an arbitrary element
print(s,"\n")
s.clear()         # empty set now
print(s,"\n")


s |= {5, 6}       # in-place union, modifies s directly 
print(s,"\n")
print("frozenset (immutable) ❌: Once created you can't change it , or somthing ","\n")
empty = set()            # NOT {} — that's an empty dict!
fs = frozenset([1, 2, 3])
# fs.remove(1) #generate an error ,'frozenset' object has no attribute 'remove'
# print(fs)






