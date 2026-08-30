class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numsSet = set(nums)
        for n in numsSet:
            if (n-1) not in numsSet:
                longest = 0
                while (n+longest) in numsSet:
                    longest += 1
                res = max(res, longest)
        return res