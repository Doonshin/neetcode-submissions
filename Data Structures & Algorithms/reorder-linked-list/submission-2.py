# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

         # 2. 後半を逆順にする
        pre = None
        second = slow.next
        slow.next = None
        while second:
            temp = second.next
            second.next = pre
            pre = second
            second = temp

         # 3. 前後を交互にマージする
        first, second = head, pre
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2



        



