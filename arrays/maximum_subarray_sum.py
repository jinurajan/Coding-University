"""
Given an array of n numbers calculate the maximum subarray sum ie the largest possible sum of a 
sequence of consecutive values in the array

Best Algorithm: maximum_subarray_sum_4 Using Kadane's Algorithm (DP)
"""
import math

def maximum_subarray_sum_1(array):
    """
    Time complexity O(n^3)
    edge case not handled when array is of len 1 and element < 0
    """
    best = 0
    for i in range(len(array)):
        for j in range(i, len(array)):
            sum = 0
            for k in range(i, j):
                sum += array[k]
            best = max(sum, best)
    return best


def maximum_subarray_sum_2(array):
    """
    Time complexity O(n^2)
    edge case not handled when array is of len 1 and element < 0
    """
    best = 0
    for i in range(len(array)):
        sum = 0
        for j in range(i, len(array)):
            sum += array[j]
            best = max(sum, best)
    return best

def maximum_subarray_sum_3(array):
    """
    Time complexity O(n)
    edge case not handled when array is of len 1 and element < 0
    """
    best = 0
    sum = 0
    for i in range(len(array)):
        sum = max(array[i], sum+array[i])
        best = max(best, sum)
    return best

def maximum_subarray_sum_4(array):
    """
    Time complexity O(n)
    Dynamic programming: Kadane's Algorithm
    edge case when array has only one element
    """
    best = array[0]
    sum = array[0]
    for i in range(1, len(array)):
        sum = max(array[i], sum+array[i])
        best = max(best, sum)
    return best

def maximum_subarray_sum_5(array):
    """
    Divide and conquer Technique
    Time complexity = O(N.logN)
    Space complexity = O(logN)
    """
    def find_best_subarray(array, left, right):
        if left > right:
            return -math.inf
        mid = (left + right) // 2
        curr = best_left_sum = best_right_sum = 0
        for i in range(mid-1, left-1, -1):
            curr += array[i]
            best_left_sum = max(curr, best_left_sum)
        curr = 0
        for i in range(mid+1, right+1):
            curr += array[i]
            best_right_sum = max(curr, best_right_sum)
        
        best_combined_sum = array[mid] + best_left_sum + best_right_sum
        left_half = find_best_subarray(array, left, mid-1)
        right_half = find_best_subarray(array, mid+1, right)
        
        return max(best_combined_sum, left_half, right_half)
    
    return find_best_subarray(array, 0, len(array)-1)
        



array = [-1, 2, 4, -3, 5, 2, -5, 2]
print(maximum_subarray_sum_1(array))
print(maximum_subarray_sum_2(array))
print(maximum_subarray_sum_3(array))
print(maximum_subarray_sum_4(array))
print(maximum_subarray_sum_5(array))