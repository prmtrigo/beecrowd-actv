class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        visitado = set()

        atual =  headA
        while atual:
            visitado.add(atual)
            atual = atual.next
        
        atual = headB
        while atual:
            if atual in visitado:
                return atual
            atual = atual.next
        
        return None
    
    def createLinkedList(arr):
        
        if not arr:
            return None
        
        head = ListNode(arr[0])
        
        current = head
        for i in range(1, len(arr)):
            current.next = ListNode(arr[i])
            current = current.next
        return head
    
    def connectLists(headA, headB, intersect_val):

        if not headA or headB:
            return
        
        atualA = headA

        while atualA and atualA.val != intersect_val:
            atualA = atualA.next

        atualB = headB

        while atualB.next:
            atualB = atualB.next

        atualB.next = atualA