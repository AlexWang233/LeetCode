class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        l = len(beginWord)
        d = defaultdict(list)
        for word in wordList:
            for i in range(l):
                d[word[:i] + "*" + word[i+1:]].append(word) 
        q = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)
        while q:
            cur, level = q.popleft()
            for i in range(l):
                inter = cur[:i] + "*" + cur[i+1:]
                for word in d[inter]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited.add(word)
                        q.append((word, level + 1))
        return 0
