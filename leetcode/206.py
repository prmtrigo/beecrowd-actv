def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
    anterior = None
    atual = head

    while atual is not None:
        proximo = atual.next
        atual.next = anterior

        anterior = atual
        atual = proximo

        #basicamente, usando o atual como um temporário!

    return anterior