class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        
        atual = head

        while atual.next:
            if atual.val == atual.next.val:
                atual.next = atual.next.next
            else:
                atual = atual.next

        return head