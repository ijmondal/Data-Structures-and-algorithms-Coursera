# Uses python3
import sys

def get_number_of_inversions(a, left, right):
    number_of_inversions = 0
    if left < right:
        ave = left + (right - left) // 2
        number_of_inversions += get_number_of_inversions(a, left, ave)
        number_of_inversions += get_number_of_inversions(a, ave+1, right)
        #write your code here
        number_of_inversions += merge(a, left, ave, right)
    return number_of_inversions

def merge(A, l, m, r):
    k = l
    n1 = m-l+1
    n2 = r-m
    L = [0]*(n1)
    R = [0]*(n2)
    
    for i in range(0 , n1): 
        L[i] = A[l + i] 
  
    for j in range(0 , n2): 
        R[j] = A[m+1 + j] 
    
    i,j = 0, 0
    inv=0
    
    while i<n1 and j<n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
                       
        else:
            A[k] = R[j]
            j += 1
            inv += n1-i
        k += 1
    
    while i <n1:
        A[k] = L[i]
        i +=1
        k += 1
        
    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1 
        
    return inv
if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    n = 7
    a = [6, 9, 8, 7, 3, 2, 1]
    
    
   
    print(get_number_of_inversions(a, 0, n-1))
    print(a)