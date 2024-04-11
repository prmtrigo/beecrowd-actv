class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    atual = dummy
    carry = 0

    while carry or l1 or l2:
      if l1:
        carry += l1.val
        l1 = l1.next

      if l2:
        carry += l2.val
        l2 = l2.next
        
      atual.next = ListNode(carry % 10)
      carry //= 10
      atual = atual.next

    return dummy.next