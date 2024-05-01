class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        def planificar(node):

            if not node:
                return None
            
            if not node.child and not node.next:
                return node
            
            if not node.child:
                return planificar(node.next)
            
            no_filho = planificar(node.child)
            proximo_no = node.next

            if proximo_no:
                no_filho.next = proximo_no
                proximo_no.prev = no_filho

            node.next = node.child
            node.child.prev = node
            node.child = None

            return planificar(no_filho) if proximo_no else no_filho
        
        planificar(head)
        return head