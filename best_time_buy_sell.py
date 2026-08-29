# Find the maximum profit you can achieve by buying on one day and selling on a future day.

# Given an integer array prices where prices[i] is the price of a stock on day i, return the 
# maximum profit achievable.You may buy on any day and sell on a future day.Y
# You may not buy and sell on the same day.

# Naive way :  if to solve this problem using tow nested loop 
# for each  buying day  i calculate 


def best_time_buy_sell(nums):
    n=len(nums)
    max_profit=0
    for i in range(n):
        for j in range(i+1,n):
            profit=nums[j]-nums[i]
            max_profit=max(max_profit,profit)
    return max_profit

prices = [7,1,5,3,6,4]
print("Time Complexity: O(n2) — All pair comparisons.Space Complexity: O(1) — Constant space :",best_time_buy_sell(prices),"\n")

# another i suffit 
#Greedy Approach :
# # Instead of brute force (checking all pairs of days), the greedy idea is:
    #----> Track the minimum price so far (the best day to buy up to now).
    #----> At each day, compute the profit if sold today = price - min_price.
    #----> Update the maximum profit if this profit is larger.
    #----> This ensures you always buy before you sell, respecting the timeline.


def best_time_optimized(prices):
    min_price=float('inf')
    max_profit=0
    for i in range(len(prices)):
        min_price=min(min_price,prices[i]) # this the best day to buy up to now
        profit=prices[i]-min_price
        max_profit=max(max_profit,profit)
    return max_profit


prices = [2, 10, 1]
print("Greedy aproach,tracking just the minimum : ",best_time_optimized(prices))



# another way  to catch the best day to buy 


def another_way(prices):
    n,max_profit=len(prices),0
    right,left=1,0
    while right<n:
        if prices[right]<prices[left]:
            left=right
        current_profit=prices[right]-prices[left]
        max_profit=max(max_profit,current_profit)
        right+=1
    return max_profit

        
prices = [2, 10, 1]
print("using a while  loop to check if the right price or the left ",another_way(prices))







