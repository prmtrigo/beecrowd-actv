class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        inicio = 0
        final = len(height) - 1
        area_total = 0

        while inicio < final:
            area_atual = min(height[inicio], height[final]) * (final - inicio)
            area_total = max(area_atual, area_total)

            if height[inicio] < height[final]:
                inicio += 1
            else:
                final -= 1

        return area_total