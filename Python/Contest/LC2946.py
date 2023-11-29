class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        for arr in mat:
            l = len(arr)
            for i in range(l):
                if arr[i] != arr[(i + k) % l]:
                    return False

        return True