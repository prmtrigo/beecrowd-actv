class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def check(root):
            if not root:
                return 0, True
            altura_esquerda, equilibrio_esquerdo = check(root.left)
            altura_direita, equilibrio_direito = check(root.right)
            return max(altura_esquerda, altura_direita) + 1, equilibrio_esquerdo and equilibrio_direito and abs(altura_esquerda - altura_direita) <= 1
        return check(root)[1]