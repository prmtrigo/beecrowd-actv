class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        vetor_pares = {}

        for i, num in enumerate(nums):
            if target - num in vetor_pares:
                return [vetor_pares[target - num], i]

            vetor_pares[num] = i