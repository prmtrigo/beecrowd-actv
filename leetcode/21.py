class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        atual = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                atual.next = list1
                list1, atual = list1.next, list1

            else:
                atual.next = list2
                list2, atual = list2.next, list2

        if list1 or list2:
            atual.next = list1 if list1 else list2
        
        return dummy.next