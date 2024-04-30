def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    devagar = head
    rapido = head

    while rapido is not None and rapido.next is not None:
        devagar = devagar.next
        rapido = rapido.next.next

    return devagar