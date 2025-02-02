class Solution:
    def check(self, nums: List[int]) -> bool:
        flag = False
        start = nums[0]
        cur = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                if flag:
                    return False
                flag = True
                cur = nums[-1]
        return cur <= start