class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        l = len(req_skills)
        skills = {skill: ind for ind, skill in enumerate(req_skills)}
        dp = {0: []}
        for i, p in enumerate(people):
            cur = 0
            for skill in p:
                if skill in skills:
                    cur |= 1 << skills[skill]
            for prev, ppl in dp.copy().items():
                nxt = prev | cur
                if nxt == prev:
                    continue
                if nxt not in dp or len(dp[nxt]) > len(ppl) + 1:
                    dp[nxt] = ppl + [i]
        return dp[(1 << l) - 1]