class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        tamanho_1 = len(nums1)
        tamanho_2 = len(nums2)
        minimo, maximo, meio = 0,tamanho_1,(tamanho_1+tamanho_2+1)//2

        while minimo <= maximo:
            p1 = (minimo + maximo)//2
            p2 = meio - p1

            if p1 < tamanho_1 and nums1[p1] < nums2[p2 - 1]:
                minimo = p1 + 1
            elif p1 > 0 and nums1[p1 - 1] > nums2[p2]:
                maximo = p1 - 1
            else:
                if p1 == 0:
                    maximo_esquerda = nums2[p2-1]
                elif p2 == 0:
                    maximo_esquerda = nums1[p1-1]
                else:
                    maximo_esquerda = max(nums1[p1-1], nums2[p2-1])
            
                if (tamanho_1 + tamanho_2) % 2 == 1:
                    return maximo_esquerda
                
                if p1 == tamanho_1:
                    minimo_direita = nums2[p2]
                elif p2 == tamanho_2:
                    minimo_direita = nums1[p1]
                else:
                    minimo_direita = min(nums1[p1], nums2[p2])
                
                return (maximo_esquerda + minimo_direita) / 2.0