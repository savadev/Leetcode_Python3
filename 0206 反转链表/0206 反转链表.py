#label: 链表 difficulty: easy

"""
思路一：

迭代法

最经典的反转链表的方法，清华数据结构书中介绍
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre,cur = None,head
        while cur:
            tmp = cur.next # 保存该节点的下一个节点
            cur.next = pre
            pre = cur #pre前进一个节点
            cur = tmp #cur前进一个节点
        return pre
        
“”“
思路二：

利用栈先进后出的性质。

将所有节点压入栈，然后逐个弹出连接next指针。

”“”

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        stack = []
        p = head
        while p:
            stack.append(p)
            p = p.next
    
        newhead = stack[-1]
        p = newhead
        stack.pop() #将节点newhead弹出
        while stack:
            p.next = stack.pop()
            p = p.next
            
        p.next = None
        return newhead
    
“”“
思路三：

递归，假设我们已经得到了把head.next翻转完成的结果，p指向这个结果的头，

head的next指针此时指向这个结果的最后一个节点，即head.next

为了将head也翻转，我们需要让head.next的next指针指向head，然后把head的next置空，

最后返回p即可。

”“”

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p



