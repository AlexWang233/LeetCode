class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        def sortSection(temp):
            temp2 = []
            for n, i in temp:
                temp2.append(i)
            temp2.sort()
            for i in range(len(temp2)):
                nums[temp2[i]] = temp[i][0]

        arr = [[n, i] for i, n in enumerate(nums)]
        arr.sort()
        temp = [arr[0]]
        for i in range(1, len(nums)):
            if arr[i][0] - arr[i-1][0] <= limit:
                temp.append(arr[i])
            else:
                sortSection(temp)
                temp = [arr[i]]

        sortSection(temp)

        return nums
