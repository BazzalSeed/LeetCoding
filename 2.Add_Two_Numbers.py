"""
Note:
1. guard l1 and l2 to be not None
2. distinquish first run for head
===========
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

https://leetcode.com/problems/add-two-numbers/
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # return self.int_to_list( (self.list_to_int(l1)+self.list_to_int(l2)))
        carry_over = 0
        head = None
        next_node = None
        radix = 10
        while(l1 or l2 or carry_over):
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            new_val = (l1_val + l2_val + carry_over) % radix
            carry_over = (l1_val + l2_val + carry_over) / radix
            if not head:
                head = ListNode(new_val)
                next_node = head
            else:
                next_node.next = ListNode(new_val)
                next_node = next_node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return head

    def list_to_int(self, l):
        value = 0
        times = 1
        while l:
            value += l.val * times
            times = 10 * times
            l = l.next
        return value

    def int_to_list(self, n):
        if n == 0:
            return ListNode(0)
        head = None
        next_node = None
        while (n):
            cur = n % 10
            n = n / 10
            if not head:
                head = ListNode(cur)
                next_node = head
            else:
                next_node.next = ListNode(cur)
                next_node = next_node.next
        return head
