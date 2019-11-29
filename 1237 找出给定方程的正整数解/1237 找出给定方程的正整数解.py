#label: 二分算法 difficulty: easy

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        #严格递增，暗示采用二分法求解
        res = []
        for x in range(1, 1001):
            left, right = 1, 1000
            
            while left <= right:
                mid = (left + right) // 2
                t = customfunction.f(x, mid)
                if t == z:
                    res.append([x, mid])
                    break
                elif t > z:
                    right = mid - 1
                elif t < z:
                    left = mid + 1
                    
        return res


