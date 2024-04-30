def getDecimalValue(self, head: ListNode) -> int:
    resposta = 0
    while head:
        resposta = resposta * 2 + head.val
        head = head.next
    return resposta