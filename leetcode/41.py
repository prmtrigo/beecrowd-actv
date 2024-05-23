class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        numeros = len(nums)

        for i in range(numeros):
            while 1 <= nums[i] <= numeros and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        for i in range(numeros):
            if nums[i] != i+1:
                return i+1
            
        return numeros + 1