"""
Educative.io: Dynamic programming Beginner
Problem 3: Equal subset sum partition

Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both the subsets is equal.

{1,2,3,4} -> True {1,4} {2, 3}
{1,1,3,4,7} -> True {1, 3, 4} {1, 7}
{2,3,4,6} -> False

for each number 'i' 
  create a new set which INCLUDES number 'i' if it does not exceed 'S/2', and recursively 
      process the remaining numbers
  create a new set WITHOUT number 'i', and recursively process the remaining items 
return true if any of the above sets has a sum equal to 'S/2', otherwise return false

"""

def can_partition(num):
    """
    Time complexity: O(2^n)
    Space complexity: O(n)
    """
    s = sum(num)
    if s %2 != 0 or not num:
        # if s is an odd number, we cant have two subsets with same sum
        return False
    def can_partition_recursive(index, sum_val):
        if sum_val == 0:
            return True
        if index >= len(num):
            return False
        if num[index] <= sum_val:
            if can_partition_recursive(index+1, sum_val-num[index]):
                return True
        return can_partition_recursive(index+1, sum_val)
        
    return can_partition_recursive(0, s//2)


def can_partition_top_down_1(num):
    """
    Using Dictionary for memoization
    Time complexity: O(n)
    Space complexity: O(n)
    """
    s = sum(num)
    if s %2 != 0 or not num:
        # if s is an odd number, we cant have two subsets with same sum
        return False
    mem = {}
    def can_partition_recursive(index, sum_val):
        if (index, sum_val) in mem:
            return mem[(index, sum_val)]
        if sum_val == 0:
            return True
        if index >= len(num):
            return False
        if num[index] <= sum_val:
            if can_partition_recursive(index+1, sum_val-num[index]):
                mem[(index, sum_val)] = True
                return True
        mem[(index, sum_val)] = can_partition_recursive(index+1, sum_val)
        return mem[(index, sum_val)]
        
    return can_partition_recursive(0, s//2)



def can_partition_top_down_2(num):
    """
    Using Table / Array for memoization
    Time complexity: O(n)
    Space complexity: O(n*s) s = sum of all numbers / 2
    """
    s = sum(num)
    if s %2 != 0 or not num:
        # if s is an odd number, we cant have two subsets with same sum
        return False
    dp = [[-1 for i in range(int(s/2)+1)] for j in range(len(num))]
    def can_partition_recursive(index, sum_val):
        if sum_val == 0:
            return 1
        if index >= len(num):
            return 0
        if dp[index][sum_val] != -1:
            return dp[index][sum_val]
        if num[index] <= sum_val:
            if can_partition_recursive(index+1, sum_val-num[index]):
                dp[index][sum_val] = 1
                return 1
        dp[index][sum_val] = can_partition_recursive(index+1, sum_val)
        return dp[index][sum_val]
        
    return True if can_partition_recursive(0, s//2) == 1 else False


def can_partition_bottom_up_1(num):
    """
    Computing en-route :D 
    Time complexity: O(n)
    Space complexity: O(n*s) s = sum of all numbers / 2
    dp[i][s] is true if we can make sum s from the first i numbers
    So, for each number at index ‘i’ (0 <= i < num.length) and sum ‘s’ (0 <= s <= S/2), we have two options:

    Exclude the number. In this case, we will see if we can get ‘s’ from the subset excluding this number: dp[i-1][s]
    Include the number if its value is not more than ‘s’. In this case, we will see if we can find a subset to get the remaining sum: dp[i-1][s-num[i]]
    """
    s = sum(num)
    if s % 2 != 0 or not num:
        # if s is an odd number, we cant have two subsets with same sum
        return False
    s = int(s/2)
    n = len(num)
    dp = [[False for i in range(s+1)] for j in range(n)]
    # populate sum = 0 column since we can always have 0 without including any element
    for i in range(n):
        dp[i][0] = True
    # with only one number for eg {1} we can only make it if the value at index is equal to 1
    for j in range(1, s+1):
        dp[0][j] = num[0] == j
    
    for i in range(1, n):
        for j in range(1, s+1):
            # if we can make sum without using current element
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            elif j >= num[i]: # current value will be if value at j-num[i] is true
                dp[i][j] = dp[i-1][j-num[i]]
    return dp[n-1][s]
    


num = [1,2,3,4]
print(can_partition(num))
print(can_partition_top_down_1(num))
print(can_partition_top_down_2(num))
print(can_partition_bottom_up_1(num))
num =[1,1,3,4,7]
print(can_partition(num))
print(can_partition_top_down_1(num))
print(can_partition_top_down_2(num))
print(can_partition_bottom_up_1(num))
num = [2,3,4,6]
print(can_partition(num))
print(can_partition_top_down_1(num))
print(can_partition_top_down_2(num))
print(can_partition_bottom_up_1(num))






