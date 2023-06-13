class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mp = defaultdict(list)
        for i in range(len(accounts)):
            for email in accounts[i][1:]:
                mp[email].append(i)
        
        def dfs(i):
            if visited[i]:
                return
            visited[i] = True
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for ngbr in mp[email]:
                    dfs(ngbr)

        res = []
        visited = [False] * len(accounts)
        for i in range(len(accounts)):
            if visited[i]:
                continue
            name, emails = accounts[i][0], set()
            dfs(i)
            res.append([name] + sorted(emails))
        return res