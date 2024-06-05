class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        soma = float('inf')

        for i in range (len(nums)-2):
            proximo, final = i+1, len(nums) -1

            while proximo < final:
                soma_atual = nums[i] + nums[proximo] + nums[final]
                
                if soma_atual == target:
                    return soma_atual
                
                if abs(soma_atual - target) < abs(soma - target):
                    soma = soma_atual
                
                if soma_atual < target:
                    proximo += 1
                else:
                    final -= 1

        return soma
