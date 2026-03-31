class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        neigh = defaultdict(list)


        for word in wordList:
            length = len(word)
            for j in range(length):
                pattern = word[:j] + "*" + word[j+1:]
                neigh[pattern].append(word)

        res = 1
        visit = set()
        visit.add(beginWord)
        queue = deque()
        queue.append(beginWord)


        while queue:
            length = len(queue)
            for i in range(length):
                word = queue.popleft()

                if word == endWord:
                    return res

                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for nei in neigh[pattern]:
                        if nei not in visit:
                            queue.append(nei)
                            visit.add(nei)

            res+=1
        return 0




        