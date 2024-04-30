def rotateRight(self, head: ListNode, k: int) -> ListNode:

    if not head:
        return None
    
    ultimo_elemento = head
    tamanho = 1

    while ultimo_elemento.next:
        ultimo_elemento = ultimo_elemento.next
        tamanho += 1

    k = k % tamanho

    ultimo_elemento.next = head

    no_temporario = head
    for i in range (tamanho - k - 1):
        no_temporario = no_temporario.next

    resposta = no_temporario.next
    no_temporario.next = None

    return resposta