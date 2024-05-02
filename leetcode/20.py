class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        mapping = {")":"(", "}":"{", "]":"["}

        for caractere in s:
            if caractere in mapping.values():
                stack.append(caractere)

            elif caractere in mapping.keys():
                if stack == [] or mapping[caractere] != stack.pop():
                    return False

        return not stack
