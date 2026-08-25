# You are given a non-empty array of digits representing a non-negative integer. The digits are stored such
# that the most significant digit is at the head of the array (index 0), and each element contains a single digit
# (0-9). Add one to the integer represented by the array and return the resulting array of digits.
# Example 1 : 
# Input: [1, 2, 3]
# Output: [1, 2, 4]
# Explanation: 123 + 1 = 124
# Example 2: 
# Input: [9, 9, 9]
# Output: [1, 0, 0, 0]
# Explanation: 999 + 1 = 1000 (array grows by one digit)
 
# if the last digit is <9 , we add 1 and it's done
# if not, the last digit is equal to 9 we  put it to 0,

#--- first solution
def plusOne(digits):
    n=len(digits)
    for i in range(n-1,-1,-1):
        nums=digits[i]+1
        if nums<10:
            digits[i]+=1
            return digits
        digits[i]=0

    return [1]+digits
L=[1,9,8]
print(" Solution using the first method: \n")
print(plusOne(L))


#---- second solution
def plusOne2(digits):
    digits=digits[::-1]
    one,i=1,0
    while one:
        if i<len(digits):
            if digits[i]==9:
                digits[i]=0
            else:
                digits[i]+=1
                one=0
        else:
            digits.append(1)
            one=0
        i+=1
    return digits[::-1]

L=[1,9,8]
print(plusOne2(L))


            
                    
#  suggetios for tow arrays          

def merged_tow_sorted(L1,L2):
    L=[]
    n,m=len(L1),len(L2)
    p1,p2=0,0
    while p1<n and p2<m:
        if L1[p1]>=L2[p2]:
            L.append(L2[p2])
            p2+=1
        else:
            L.append(L1[p1])
            p1+=1
    L.extend(L1[p1:])
    L.extend(L2[p2:])
    return L
    

print("-- Merge tow sorted array -- \n")
list1 = []
list2 = []
print(merged_tow_sorted(list1,list2))

print("---\n")
# for tow LinkedList : each  elemnet is a pair of value and pointer of the next element , every one know  the next element


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next=next


# Création de trois nœuds
n1 = ListNode(10)
n2 = ListNode(20)
n3 = ListNode(30)

# Chaînage des nœuds
n1.next = n2
n2.next = n3
print(n3.next) # the next is obv none  
# Parcours de la liste
list2=n1
print(list2) # the type of this object plus the adress 
print(list2.val)   # Affiche 1
print(list2.next.val)  # Affiche 2
print(list2.next.next.val)  # Affiche 3
print(list2.next.next.next) 



node3 = ListNode(3, None)  # 3 → None
node2 = ListNode(2, node3) # 2 → 3 → None
node1 = ListNode(1, node2) # 1 → 2 → 3 → None

# list1 pointe vers node1
list1 = node1
print(list1) # the type of this object plus the adress 
print(list1.val)   # Affiche 1
print(list1.next.val)  # Affiche 2
print(list1.next.next.val)  # Affiche 3
print(list1.next.next.next) # obv the end of the Linked list it will return None


# Helper functions
def create_linked_list(arr): #--> create a lInkedList using an array 
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
 
def linked_list_to_list(head): #--> create an array using a LinkedList
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result




class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def MergedTowSortedLinkedList(self, list1, list2):
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        return dummy.next



# Moves zero 
# L=[0,1,0,3,12]
# --> outuput=[1,3,12,0,0]
# this naive method is intuive but not efficace in memory 
def naivemethode(nums):
    L1=[]
    L2=[]
    for num in nums:
        if num!=0:
            L1.append(num)
        else:
            L2.append(num)
    return L1+L2

print("solution using naive way without using tow nested list : \n")
L=[0,1,0,3,12]
print(naivemethode(L))

# another way using nested lest
def movezero_naive(nums):
    non_zero=[x for x in nums if x!=0]
    zero_count=len(nums)-len(non_zero)
    return non_zero+[0]*zero_count


print("solution using naive way wit using tow nested list : \n")
L=[0,1,0,3,12]
print(movezero_naive(L))





# in this method we only use the input data straucture
def moveszero(nums):
    index=0
    for num in nums:
        if num!=0:
            nums[index]=num
            index+=1
    for i in range(index,len(nums)):
        nums[i]=0
    return nums
print("The optimized solution has the same O(n) time complexity, but unlike the naive version, it doesn't create any additional data structures that grow with input size. This means the space complexity is O(1) (constant extra space) :\n")
L=[0,1,0,3,12]
print(moveszero(L))





def moves_zero_2(nums):
    index=0
    for num in nums:
        if num!=0:
            nums[index]=num # move the first number different of zero 
            index+=1
    for i in range(index,len(nums)):
        nums[i]=0
    return nums
L=[0,0,3,12]  
print("Using tow loops , still needs optimization",moves_zero_2(L))

# the best solution and the optimized way :

def moves_zero_3(nums):
    i=0
    for j in range(len(nums)):
        if nums[j]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1

L=[1,0,3,12,0]   
print("the optimized way : ",moves_zero_2(L),"\n")















    
