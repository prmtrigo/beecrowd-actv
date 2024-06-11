class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        resposta = []

        def orderTransversal(node):
            if node:
                resposta.append(node.val)
                orderTransversal(node.left)
                orderTransversal(node.right)
                return resposta
            
        return orderTransversal(root)