class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        resposta = []
        contador = 0
        for i in range(len(s)):
            if s[i] == '(':
                contador += 1

            if contador > 1:
                resposta.append(s[i])

            if s[i] == ')':
                contador -= 1

        return ''.join(resposta)
