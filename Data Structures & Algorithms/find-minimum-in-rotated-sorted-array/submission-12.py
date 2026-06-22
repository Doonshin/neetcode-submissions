class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search 
        # r、l でポインタ
        # 中間のポインタ -> m
        # [1,2,3,4,5], [3,4,5,6,1,2]

        # (r + l)//2
        # l <= m の場合, l = m + 1
        



        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            else: l = m + 1

        return nums[l] 

# rotate指定いる場合全ての左側のの数字は右側より小さい
# 例
# [3,4,5,1,2]