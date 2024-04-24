def isPalindrome(self, head: Optional[ListNode]) -> bool:
    self.atual = head
    return self.solve(head)

def solve(self, head: Optional[ListNode]) -> bool:
    if head is None:
        return True

    res = self.solve(head.next) and head.val == self.atual.val
    self.atual = self.atual.next
    return res