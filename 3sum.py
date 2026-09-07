#Continue : Skips the rest of the current iteration and jumps to the next one.
#Useful for ignoring certain cases but continuing the loop.

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    if n == 3:
        continue  # this mean don't consider n==3
    print(n)

print("\n")

for i in numbers:
    print(i)
    if i==3:
        break  # Exits the loop entirely 



# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.


def three_sum(nums):
    res=[]
    nums.sort()
    for i,a in enumerate(nums):
        if i >0 and a==nums[i-1]:
            continue #Skip the duplicate values 
        left,right=i+1,len(nums)-1
        while left<right:
            sum=a+nums[left]+nums[right]
            if sum>0:
                right-=1
            elif sum<0:
                left+=1
            else:
                res.append([a,nums[left],nums[right]])
                left+=1
                while nums[left]==nums[left-1] and left<right:
                    left+=1
    return res

nums=[-4,-1 ,-1,0,1]
print(three_sum(nums))
