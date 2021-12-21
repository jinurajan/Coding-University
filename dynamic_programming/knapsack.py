"""
Educative.io: Dynamic programming Beginner
Problem 2: 0/1 knapsack

Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack that has a capacity ‘C’. The goal is to get the maximum profit from the items in the knapsack. Each item can only be selected once, as we don’t have multiple quantities of any item.
Let’s take Merry’s example, who wants to carry some fruits in the knapsack to get maximum profit. Here are the weights and profits of the fruits:

Items: { Apple, Orange, Banana, Melon }
Weights: { 2, 3, 1, 4 }
Profits: { 4, 5, 3, 7 }
Knapsack capacity: 5

Let’s try to put different combinations of fruits in the knapsack, such that their total weight is not more than 5:

Apple + Orange (total weight 5) => 9 profit
Apple + Banana (total weight 3) => 7 profit
Orange + Banana (total weight 4) => 8 profit
Banana + Melon (total weight 5) => 10 profit

This shows that Banana + Melon is the best combination, as it gives us the maximum profit and the total weight does not exceed the capacity.

Problem: Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number ‘C’. Write a function that returns the maximum profit. Each item can only be selected once, which means either we put an item in the knapsack or skip it.

"""

def solve_knapsack(profits, weights, capacity):
    # brute force: Try all possible scenarios
    # at every stage we have two options either include / do not include
    # handle edge cases for index and capacity
    """
        for each item 'i' 
        create a new set which INCLUDES item 'i' if the total weight does not exceed the capacity, and 
            recursively process the remaining capacity and items
        create a new set WITHOUT item 'i', and recursively process the remaining items 
        return the set from the above two sets with higher profit
        time complexity: O(2^n)
        space complexity: O(n)
    """
    def helper(index, balance):
        if balance <= 0 or index >= len(profits):
          return 0
        p1 = 0
        if balance >= weights[index]:
            p1 = profits[index] + helper(index+1, balance-weights[index])
        p2 = helper(index+1, balance)
        return max(p1, p2)
    return helper(0, capacity)


def solve_knapsack_topdown(profits, weights, capacity):
    # using dictionary
    mem = {}
    def helper(index, balance):
        if index >= len(profits) or balance <= 0:
            return 0
        if (index, balance) in mem:
            return mem[(index, balance)]
        p1 = 0
        if balance >= weights[index]:
            p1 = profits[index] + helper(index+1, balance-weights[index])
        p2 = helper(index+1, balance)
        mem[(index, balance)] = max(p1, p2)
        return mem[(index, balance)]
    return helper(0, capacity)
    

def solve_knapsack_topdown_1(profits, weights, capacity):
    # using array
    dp =[[-1 for x in range(capacity+1)] for y in range(len(profits))]
    def helper(index, balance):
        if index >= len(profits) or balance <= 0:
            return 0
        if dp[index][balance] != -1:
            return dp[index][balance]
        p1 = 0
        if balance >= weights[index]:
            p1 = profits[index] + helper(index+1, balance-weights[index])
        p2 = helper(index+1, balance)
        dp[index][balance] = max(p1, p2)
        return dp[index][balance]
    return helper(0, capacity)


def solve_knapsack_bottomup(profits, weights, capacity):
    """
        So, for each item at index ‘i’ (0 <= i < items.length) and capacity ‘c’ (0 <= c <= capacity), we have two options:
        Exclude the item at index ‘i’. In this case, we will take whatever profit we get from the sub-array excluding this item => dp[i-1][c]
        Include the item at index ‘i’ if its weight is not more than the capacity. In this case, we include its profit plus whatever profit we get from the remaining capacity and from remaining items => profits[i] + dp[i-1][c-weights[i]]   
        dp[i][c] = max (dp[i-1][c], profits[i] + dp[i-1][c-weights[i]]) 
    """
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0
    dp =[[0 for x in range(capacity+1)] for y in range(n)]
    # populate the capacity = 0 columns, with '0' capacity we have '0' profit. Not required since we already initialzed with 0
    # for i in range(0, n):
    #     dp[0][i] = 0

    # if we have only one weight, we will take it if it is not more than the capacity
    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]
    for i in range(1, n):
        for c in range(1, capacity+1):
            p1, p2 = 0, 0
            if weights[i] <= c:
                p1 = profits[i] + dp[i-1][c-weights[i]]
            p2 = dp[i-1][c]
            dp[i][c] = max(p1, p2)
    return dp[n-1][capacity]

def solve_knapsack_bottomup_1(profits, weights, capacity):
    # with O(C) space complexity. store only the previous two rows
    # basic checks
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0
    dp =[[0 for x in range(capacity+1)] for y in range(2)]
    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]
    for i in range(1, n):
        for c in range(1, capacity+1):
            p1, p2 = 0, 0
            if weights[i] <= c:
                p1 = profits[i] + dp[(i-1) % 2][c-weights[i]]
            p2 = dp[(i-1) % 2][c]
            dp[i % 2][c] = max(p1, p2)
    return dp[(n-1) % 2][capacity]

def solve_knapsack_bottomup_2(profits, weights, capacity):
    # with single array. use same array for previous and next iteration
    # basic checks
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0
    dp = [0 for x in range(capacity+1)]

    # if we have only one weight, we will take it if it is not more than the capacity
    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[c] = profits[0]
    
    for i in range(1, n):
        for c in range(capacity, -1, -1):
            p1, p2 = 0, 0
            if weights[i] <= c:
                p1 = profits[i] + dp[c-weights[i]]
            p2 = dp[c]
            dp[c] = max(p1, p2)
    return dp[capacity]


def solve_knapsack_bottomup_with_printing(profits, weights, capacity):
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0
    dp =[[0 for x in range(capacity+1)] for y in range(n)]
    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]
    for i in range(1, n):
        for c in range(1, capacity+1):
            p1, p2 = 0, 0
            if weights[i] <= c:
                p1 = profits[i] + dp[i-1][c-weights[i]]
            p2 = dp[i-1][c]
            dp[i][c] = max(p1, p2)
    print_selected_elements(dp, weights, profits, capacity)
    return dp[n-1][capacity]



def print_selected_elements(dp, weights, profits, capacity):
    print("Selected weights are: ", end='')
    n = len(weights)
    totalProfit = dp[n-1][capacity]
    for i in range(n-1, 0, -1):
        if totalProfit != dp[i - 1][capacity]:
            print(str(weights[i]) + " ", end='')
            capacity -= weights[i]
            totalProfit -= profits[i]

    if totalProfit != 0:
        print(str(weights[0]) + " ", end='')
    print()


print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))

print(solve_knapsack_topdown([1, 6, 10, 16], [1, 2, 3, 5], 7))
print(solve_knapsack_topdown([1, 6, 10, 16], [1, 2, 3, 5], 6))


print(solve_knapsack_topdown_1([1, 6, 10, 16], [1, 2, 3, 5], 7))
print(solve_knapsack_topdown_1([1, 6, 10, 16], [1, 2, 3, 5], 6))

print(solve_knapsack_bottomup([1, 6, 10, 16], [1, 2, 3, 5], 7))
print(solve_knapsack_bottomup([1, 6, 10, 16], [1, 2, 3, 5], 6))

print(solve_knapsack_bottomup_1([1, 6, 10, 16], [1, 2, 3, 5], 7))
print(solve_knapsack_bottomup_1([1, 6, 10, 16], [1, 2, 3, 5], 6))

print(solve_knapsack_bottomup_2([1, 6, 10, 16], [1, 2, 3, 5], 7))
print(solve_knapsack_bottomup_2([1, 6, 10, 16], [1, 2, 3, 5], 6))

print(solve_knapsack_bottomup_with_printing([1, 6, 10, 16], [1, 2, 3, 5], 7))
print(solve_knapsack_bottomup_with_printing([1, 6, 10, 16], [1, 2, 3, 5], 6))