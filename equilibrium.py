"""This module implements solution for the equilibrium index algorithms problem.

The algorithm returns only one such index where solution exists else returns -1
"""

def equilibrium_index(arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        total = 0
        sum_at_idx = 0
        for i in arr:
            total += i
            
        # sum for index -1 and index N+1 is 0
        for i in range(0, len(arr)):
            if sum_at_idx == total - sum_at_idx - arr[i]:
                return i
            sum_at_idx += arr[i]
        return -1


arr = [8,2,7,2,-2,12,4,3]
print equilibrium_index(arr)
