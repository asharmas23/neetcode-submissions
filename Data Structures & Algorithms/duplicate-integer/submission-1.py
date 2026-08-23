class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unq = set(nums)

        return (len(unq) != len(nums))
        