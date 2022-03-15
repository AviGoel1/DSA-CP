""" 
Problem Link:- https://www.includehelp.com/icp/maximum-value-in-a-bitonic-array.aspx

TestCase:-
1 4 8 3 2

Output:-
8 

"""

# Approach - If we look carefully we can see that in this question we are just finding the peak element because it is a bitonic array which is first monotonically increases than monotonically decreases there will only be one peak element that would be the maximum in the array.


def findPeakElement(arr):
        n = len(arr)
        if n==1:
            return 0
        l = 0
        h = n-1
        while l <= h:
            m = l + (h-l)//2
            if m > 0 and m < n-1:
                if arr[m] > arr[m-1] and arr[m] > arr[m+1]:
                    return arr[m]
                elif arr[m-1] > arr[m]:
                    h = m-1
                else:
                    l = m+1
            elif m == 0:
                if arr[m] > arr[m+1]:
                    return arr[0]
                else:
                    return arr[1]
            elif m == n-1:
                if arr[m] > arr[m-1]:
                    return arr[n-1]
                else:
                    return arr[n-2]
 
lst = list(map(int,input().split()))
print(findPeakElement(lst))
