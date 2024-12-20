"""
Given two integers, this benchmark finds the number
of possible values of X to satisfy the modular equation A mod X = B.

"benchmark_metadata": {[
    {
        "Function": [''],
        "Bug": [('', '')],
        "Fix": [('', '')]
    }
]}
The content of this file can be found in geeksforgeeks.
@misc{geeksforgeeks_2018,
    title={Python program for number of solutions to modular equations},
    url={https://www.geeksforgeeks.org/python-program-for-number-of-solutions-to-modular-equations/},
    journal={GeeksforGeeks}, author={GeeksforGeeks}, year={2018}, month={Dec}
} 
"""
import math
 
# Returns the number of divisors of (A - B)
# greater than B
def calculateDivisors(A, B):
    N = A - B
    noOfDivisors = 0
     
    a = math.sqrt(N)
    for i in range(1, int(a + 1)):
        # if N is divisible by i
        if ((N % i == 0)):
            # count only the divisors greater than B
            if (i > B):
                noOfDivisors +=1
                 
            # checking if a divisor isnot counted twice
            if ((N / i) != i and (N / i) > B):
                noOfDivisors += 1
                 
    return noOfDivisors
     
# Utility function to calculate number of all
# possible values of X for which the modular
# equation holds true 
    
def numberOfPossibleWaysUtil(A, B):
    # if A = B there are infinitely many solutions
    # to equation  or we say X can take infinitely
    # many values > A. We return -1 in this case 
    if (A == B):
        return -1
         
    # if A < B, there are no possible values of
    # X satisfying the equation
    if (A < B):
        return 0
         
    # the last case is when A > B, here we calculate
    # the number of divisors of (A - B), which are
    # greater than B    
     
    noOfDivisors = 0
    noOfDivisors = calculateDivisors(A, B)
    return noOfDivisors

def modular_equation(A, B):
    noOfSolutions = numberOfPossibleWaysUtil(A, B)
    return noOfSolutions


# if __name__ == "__main__":
#     r = modular_equation(-165,-185)
#     print(r)
