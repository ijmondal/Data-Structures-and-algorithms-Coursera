# Uses python3
import sys
import itertools

def canPartition3(A):
    s = sum(A)
    target, rem = divmod(s,3)
    
    if rem !=0 or max(A) > target:
        return False
    
    nums = sorted(A, reverse=True)
    return search(nums, 3, target, target, set())

def search(nums, k, cur_target, full_target, visited):
    if k == 0:
        return True        
        
    elif cur_target < 0:
        return False
        
    elif cur_target == 0:
        return search(nums, k-1, full_target, full_target, visited)
        
    else:            
        for i in range(0, len(nums)):
            if i not in visited:
                visited.add(i)
                if search(nums, k, cur_target-nums[i], full_target, visited):           
                    return True
                visited.remove(i)
        return False

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    if canPartition3(A):
        print(1)
    else:
        print(0)
    

