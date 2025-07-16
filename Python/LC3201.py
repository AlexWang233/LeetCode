class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd = even = both = 0
        parity = nums[0] % 2
        if parity == 1:
            odd += 1
        else:
            even += 1
        both += 1
        for n in nums[1:]:
            p = n % 2
            if p == 1:
                odd += 1
            else:
                even += 1
            if p + parity == 1:
                both += 1
            parity = p
        return max([odd, even, both])