class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if not nums2:
            return None
        
        mapear = {}
        estaca = []
        estaca.append(nums2[0])

        for i in range(1, len(nums2)):
            while estaca and estaca[-1] < nums2[i]:
                mapear[estaca[-1]] = nums2[i]
                estaca.pop()
            estaca.append(nums2[i])

        return [mapear.get(n, -1) for n in nums1]
