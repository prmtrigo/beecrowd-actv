class Solution:
    def romanToInt(self, s: str) -> int:
        
        romano_inteiro = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        valor_anterior = 0

        for char in s:
            valor_atual = romano_inteiro[char]
            if valor_atual > valor_anterior:
                total += valor_atual - 2 * valor_anterior
            else:
                total += valor_atual
            
            valor_anterior = valor_atual
        
        return total