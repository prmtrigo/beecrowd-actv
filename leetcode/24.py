def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
    if not head or not head.next:
        return head
    
    temporario = ListNode(0)
    temporario.next = head

    atual = temporario

    while atual.next and atual.next.next:
        primeiro = atual.next
        segundo = atual.next.next

        primeiro.next = segundo.next

        atual.next = segundo
        atual.next.next = primeiro

        atual = atual.next.next
        
    return temporario.next