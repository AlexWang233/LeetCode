class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preq = defaultdict(lambda: set())
        postq = defaultdict(lambda: set())
        for pre, post in prerequisites:
            preq[pre].add(post)
            postq[post].add(pre)

        q = []
        for i in range(numCourses):
            if len(preq[i]) == 0:
                q.append(i)

        ans = []
        while len(q) > 0:
            cur = []
            for c in q:
                ans.append(c)
                for p in postq[c]:
                    preq[p].remove(c)
                    if len(preq[p]) == 0:
                        cur.append(p)
                postq[c] = set()
            q = cur


        if len(ans) < numCourses:
            return []
        return ans