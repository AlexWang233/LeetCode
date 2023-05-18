class Solution:
    def findKth(self, arr1, arr2, ind) -> float:
        l1, l2 = len(arr1), len(arr2)
        if l1 <= 0:
            return arr2[ind]
        if l2 <= 0:
            return arr1[ind]
        med1, med2 = l1 // 2, l2 // 2
        n1, n2 = arr1[l1//2], arr2[l2//2]
        if med1 + med2 < ind:
            if n1 > n2:
                return self.findKth(arr1, arr2[med2 + 1:], ind - med2 - 1)
            return self.findKth(arr1[med1 + 1:], arr2, ind - med1 - 1)
        else:
            if n1 > n2:
                return self.findKth(arr1[:med1], arr2, ind)
            return self.findKth(arr1, arr2[:med2], ind)


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, l2 = len(nums1), len(nums2)
        i = (l1 + l2) // 2
        if (l1 + l2) % 2:
            return self.findKth(nums1, nums2, i)
        return (self.findKth(nums1, nums2, i) + self.findKth(nums1, nums2, i-1))/2
