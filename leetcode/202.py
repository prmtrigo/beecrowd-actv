class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sum_of_squares(n):
            soma_total = 0
            while n > 0:
                soma_total += (n % 10) ** 2
                n //= 10
            return soma_total
        
        visto = set()

        while n != 1 and n not in visto:
            visto.add(n)
            n = sum_of_squares(n)
        
        return n == 1