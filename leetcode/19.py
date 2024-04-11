class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        primeiro = dummy
        segundo = dummy

        for i in range(n+1):
            primeiro = primeiro.next

        while primeiro is not None:
            primeiro =  primeiro.next
            segundo = segundo.next

        segundo.next = segundo.next.next

        return dummy.next