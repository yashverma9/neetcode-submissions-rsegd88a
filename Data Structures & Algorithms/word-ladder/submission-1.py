from collections import defaultdict
from collections import deque
class Solution:
    # Optimal
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or endWord == beginWord:
            return 0

        adjList = defaultdict(list)
        wordList.append(beginWord)

        # Create graph adj list using pattern matching
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adjList[pattern].append(word)
            
        q = deque()
        visited = set()

        q.append(beginWord)

        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei in adjList[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            
            res += 1
        
        return 0






