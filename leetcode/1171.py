def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:

    dummy = ListNode(0)
    dummy.next = head
    soma_prefixo = 0
    prefix_sums = {0: dummy}
    current = head

    while current:
        soma_prefixo += current.val
        if soma_prefixo in prefix_sums:
            to_delete = prefix_sums[soma_prefixo].next
            temp_sum = soma_prefixo + to_delete.val
            while to_delete != current:
                del prefix_sums[temp_sum]
                to_delete = to_delete.next
                temp_sum += to_delete.val
            prefix_sums[soma_prefixo].next = current.next
        else:
            prefix_sums[soma_prefixo] = current
        current = current.next

    return dummy.next
