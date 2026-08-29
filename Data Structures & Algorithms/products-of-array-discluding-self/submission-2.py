class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputs = [1] * len(nums)
        pref = 1
        for i in range(len(nums)):
            outputs[i] = pref
            pref *= nums[i]
        post = 1
        for i in range(len(nums)-1, -1, -1):
            outputs[i] *= post
            post *= nums[i] 
        return outputs

