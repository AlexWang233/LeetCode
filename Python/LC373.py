class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        hq = []
        l1 = len(nums1)
        l2 = len(nums2)
        for i in range(min(k, l1)):
            heapq.heappush(hq, (nums1[i] + nums2[0], nums1[i], nums2[0], 0))
        for _ in range(k):
            temp, n, m, i = heapq.heappop(hq)
            res.append([n, m])
            if i + 1 < l2:
                heapq.heappush(hq, (n + nums2[i + 1], n, nums2[i+1], i+1))
            if not hq:
                break
        return res