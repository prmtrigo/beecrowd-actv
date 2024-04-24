def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
       
    dummy = ListNode(0)
    dummy.next = head
    anterior, atual = dummy, head

    while atual:
      if atual.val == val:anterior.next = atual.next
      else: anterior = atual
      atual = atual.next

    return dummy.next