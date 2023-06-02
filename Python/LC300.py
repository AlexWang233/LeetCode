class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = []
        
        for n in nums:
            if len(arr) == 0 or n > arr[-1]:
                arr.append(n)
            else:
                left, right = 0, len(arr)
                while left < right:
                    mid = (int)((left + right)/2)
                    if n > arr[mid]:
                        left = mid + 1
                    else:
                        right = mid
                        
                arr[right] = n
                
        return len(arr)
                