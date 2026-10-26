class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        spaces = []

        while l < r:
            width = r - l
            height = min(heights[r], heights[l])
            area = width * height
            spaces.append(area)

            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
                r -= 1
            
            

        return max(spaces)

            


