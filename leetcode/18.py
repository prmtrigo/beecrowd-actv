class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        soma = []

        for i in range (len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                proximo, final = j+1, len(nums)-1

                while proximo < final:
                    soma_atual = nums[i] + nums[j] + nums[proximo] + nums[final]
                    
                    if soma_atual == target:
                        soma.append([nums[i], nums[j], nums[proximo], nums[final]])
                        
                        while proximo < final and nums[proximo] == nums[proximo + 1]:
                            proximo += 1
                        while proximo < final and nums[final] == nums[final -1]:
                            final -= 1
                        
                        proximo += 1
                        final -= 1

                    elif soma_atual < target:
                        proximo += 1
                    else:
                        final -= 1
        return soma


