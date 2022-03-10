""" 
Problem Link:- https://leetcode.com/problems/find-peak-element/ 

TestCase:-
1 2 3 1

Output:-
2 (index of peak element)

"""


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
                    return m
                elif arr[m-1] > arr[m]:
                    h = m-1
                else:
                    l = m+1
            elif m == 0:
                if arr[m] > arr[m+1]:
                    return 0
                else:
                    return 1
            elif m == n-1:
                if arr[m] > arr[m-1]:
                    return n-1
                else:
                    return n-2
 
lst = list(map(int,input().split()))
print(findPeakElement(lst))
