""" Problem Link:- https://practice.geeksforgeeks.org/problems/search-in-a-matrix-1587115621/1

TestCase:-
3
3, 30, 38
36, 43, 60
40, 51, 69
62

Output:-
0 (0 -> Element not present, 1 -> Element present)

"""

def search(self,matrix, n, m, key): 
    	# code here 
    	i = 0
    	j = m-1
    	while i < n and j >= 0:
    	    if matrix[i][j] == key:
    	        return 1
    	    elif matrix[i][j] > key:
    	        j -= 1
    	    else:
    	        i += 1
    	return 0

n = int(input())
mat = []
for i in range(n):
  mat.append(list(map(int,input().split())))
m = len(mat[0])
key = int(input())
print(search(mat,n,m,key)
