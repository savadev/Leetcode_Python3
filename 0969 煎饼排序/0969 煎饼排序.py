#label: sort difficulty: medium

"""
思路：

按照题意，每次操作只能翻转前K个元素，所以得出结论排序应该先从最末尾排起，不然排好的顺序就会被接下来的翻转操作所打乱，

因此我们每次都应该先把未排序数组里的最大元素放到未排序数组的最末尾，

比如 [1,4,2,3]这个数组，首先就应该想办法把4放到最后，

直接一步翻转放到最后显然不可行，那就倒着想，怎么假设已经放好了[X,X,X,4]，它的上一步应该是什么，

根据翻转的规则不难得出，上一步应该就是[4,X,X,X]

因此可以总结出翻转的规则：

        1. 每次都要处理未排序数组里的最大元素

        2. 先把这个最大元素翻转到未排序数组的头部 (K = 最大元素的下标 + 1 ）

        3. 再翻转整个未排序数组（定义一个变量num代表已经排好的元素个数， K = 元素总数-num），就可以使得这个最大元素排好位置

        4. 把两次翻转的K依次加入到res中去（这种翻转规则的翻转总数最多为数组长度的两倍，满足题目要求 <10 * A.length ）

举例[1, 4 , 2, 3]的操作步骤：

 [1,4,2,3] -----------------> [4,1,2,3] ----------------> [3,2,1,4]

 [3,2,1,4] -----------------> [1,2,3,4](排序已完成)

"""

class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        l = len(A)
        num = 0  #已排好序的元素个数
        res = []
        while(num < l - 1):
            maxe = max(A)
            index = A.index(maxe)
            if index != l - num -1:
                res.append(index + 1)
                res.append(l-num)     
                A[:index + 1] = A[:index + 1][::-1]
                A[:l - num] = A[:l - num][::-1]
            
            A = A[:-1]
            num += 1
            
        return res
 
