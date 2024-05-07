class Solution:
    def calPoints(self, o: List[str]) -> int:

        i = 0
        operacoes = []

        while i < len(o):
            if o[i]!= "C" and o[i]!= "D" and o[i]!= "+":
                operacoes.append(int(o[i]))
            elif o[i]=="C":
                    operacoes.remove(operacoes[-1])
            elif o[i] == "D":
                    operacoes.append(operacoes[-1]*2)
            elif o[i] == "+":
                    operacoes.append(operacoes[-1] + operacoes[-2])
            i += 1

        return sum(operacoes)   