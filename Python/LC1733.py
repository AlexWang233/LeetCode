class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        languages = [set(i) for i in languages]
        ppl = set()
        for i, j in friendships:
            if len(languages[i - 1] & languages[j - 1]) == 0:
                ppl.add(i - 1)
                ppl.add(j - 1)

        ans = 1000
        for i in range(1, n + 1):
            cur = 0
            for p in ppl:
                if i not in languages[p]: 
                    cur += 1
            ans = min(ans, cur)

        return ans