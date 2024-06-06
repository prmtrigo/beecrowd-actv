class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        arvore = []
        resultado = []

        while root or arvore:
            while root:
                arvore.append(root)
                root = root.left
            
            root = arvore.pop()
            resultado.append(root.val)
            root = root.right

        return resultado