class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        nos_visitados = set()
        atual = head

        while atual is not None:
            if atual in nos_visitados:
                return True
            nos_visitados.add(atual)
            atual = atual.next
        
        return False