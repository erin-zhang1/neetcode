class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        spaces = []

        while i < j:
            height = min(heights[i], heights[j])
            distance = j - i
            space = height * distance
            spaces.append(space)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return max(spaces)
