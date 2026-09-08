class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = -100
        while l < r:
            lht = heights[l]
            rht = heights[r]
            breadth = min(lht,rht)
            length = r - l
            area = length * breadth
            if maxArea < area:
                maxArea = area
            if lht <= rht:
                l += 1
            else:
                r -= 1
        return maxArea 