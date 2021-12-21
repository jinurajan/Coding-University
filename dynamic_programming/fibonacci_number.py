"""
Educative.io: Dynamic programming Beginner
Problem 1: Fibonacci Number

DP is an optimization problem
Optimal substructure property
-----------------------------
any problem has Optimal substructure property if its overall optimal solution can be constructed from the optimal
solutions of its subproblems
eg: Fibonacci numbers have optimal substructure property
Fib(n) = Fib(n-1) + Fib(n-2)

Dynamic Programming methods

1. Top Down with Memoization (we do it top-down in the sense that we solve the top problem first (which typically recurses down to solve the sub-problems)
    - recursively find solutions for smaller subproblems
    - cache / memoize its result
2. Bottom Up with Tabulation
    - solve all subproblems first
    - fill in the table
    - compute the result to the original problem

"""

def calculate_fibonacci(n):
    if n < 2:
        return n
    return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)


def calculate_fibonacci_topdown(n):
    mem = {0:0, 1:1}

    def calculate_fibonacci_recursion(n):
        if n in mem:
            return mem[n]
        mem[n] = calculate_fibonacci_recursion(n-1) + calculate_fibonacci_recursion(n-2)
        return mem[n]

    return calculate_fibonacci_recursion(n)


def calculate_fibonacci_bottom_up(n):
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]



print(calculate_fibonacci(10))
print(calculate_fibonacci_topdown(10))
print(calculate_fibonacci_bottom_up(10))