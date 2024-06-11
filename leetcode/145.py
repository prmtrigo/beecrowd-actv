
class Solution:
    def posOrdem(self, node: Optional[TreeNode], resposta: List[int]) -> None:
        if node:
            self.posOrdem(node.left, resposta)
            self.posOrdem(node.right, resposta)
            resposta.append(node.val)
        
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        resposta = []
        self.posOrdem(root, resposta)
        return resposta