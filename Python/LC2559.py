class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        arr = [0]
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        for w in words:
            arr.append(arr[-1])
            if w[0] in vowels and w[-1] in vowels:
                arr[-1] += 1
        
        ans = []
        for start, end in queries:
            ans.append(arr[end + 1] - arr[start])
        
        return ans