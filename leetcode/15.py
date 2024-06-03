class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        resultado = []

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            inicio, final = i + 1, len(nums) - 1

            while inicio < final:
                soma = nums[i] + nums[inicio] + nums[final]

                if soma == 0:
                    resultado.append([nums[i], nums[inicio], nums[final]])

                    while inicio < final and nums[inicio] == nums[inicio + 1]:
                        inicio += 1
                    
                    while inicio < final and nums[final] == nums[final - 1]:
                        final -= 1

                    inicio += 1
                    final -= 1

                elif soma < 0:
                    inicio += 1

                else:
                    final -= 1

        return resultado