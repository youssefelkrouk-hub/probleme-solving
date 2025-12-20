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
        max_pair=0
        for j in range(1,len(values)):
            second=values[j]-j
            max_pair=max(max_pair,second+first)
            first=max(first,values[j]+j)
        return max_pair


values = [8,1,5,2,6]
print(Solution.maxScoreSightseeingPair(values))


