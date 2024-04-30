def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

    temporario = ListNode(0)
    temporario.next = head
    anterior = temporario

    while head and head.next:
        if head.val == head.next.val:
            while head and head.next and head.val == head.next.val:
                head = head.next
            head = head.next
            anterior.next = head
        
        else:
            anterior = anterior.next
            head = head.next

    return temporario.next