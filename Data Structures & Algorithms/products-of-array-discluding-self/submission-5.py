class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            cur = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                cur *= nums[j]
            output.append(cur)
        return output