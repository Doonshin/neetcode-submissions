# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         # dummy = ListNode(0, head)
#         # fast = dummy
#         # slow = head
#         # for _ in range(n+1):
#         #     fast = fast.next
#         # while fast:
#         #     fast = fast.next
#         #     slow = slow.next

#         # # remove = slow.next
#         # # slow.next = remove.next
#         # # remove.next = None
#         # slow.next = slow.next.next
#         dummy = ListNode(0, head)  # ダミーノード
#         fast = dummy
#         slow = dummy
        
#         for _ in range(n + 1):  # ダミーからスタートなので n+1
#             fast = fast.next
        
#         while fast:
#             fast = fast.next
#             slow = slow.next
        

#         return dummy.next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # ダミーノード
        fast = dummy
        slow = dummy
        
        for _ in range(n + 1):  # ダミーからスタートなので n+1
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        
        return dummy.next  # 本来の head を返す