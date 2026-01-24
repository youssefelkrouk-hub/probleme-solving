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



#the optimal approach
# TIME COMPLEXITY: O(log(min(n,m)))
# SPACE COMPLEXITY: O(1)
# def findMedianSortedArrays_optimal(nums1, nums2):
#     if len(nums1) > len(nums2):
#         nums1, nums2 = nums2, nums1

#     x, y = len(nums1), len(nums2)
#     low, high = 0, x

#     while low <= high:
#         partitionX = (low + high) // 2
#         partitionY = (x + y + 1) // 2 - partitionX

#         maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
#         maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]

#         minX = float('inf') if partitionX == x else nums1[partitionX]
#         minY = float('inf') if partitionY == y else nums2[partitionY]

#         if maxX <= minY and maxY <= minX:
#             if (x + y) % 2 == 0:
#                 return (max(maxX, maxY) + min(minX, minY)) / 2
#             else:
#                 return max(maxX, maxY)
#         elif maxX > minY:
#             high = partitionX - 1
#         else:
#             low = partitionX + 1


