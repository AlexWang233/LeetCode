class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        l = len(words)

        for i in range(l):
            for j in range(l):
                if i != j and words[j].find(words[i]) != -1:
                    ans.append(words[i])
                    break
        
        return ans