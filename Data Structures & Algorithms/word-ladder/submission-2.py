from collections import defaultdict
from collections import deque
class Solution:
    # Optimal
    '''
    Time - O(n*m^2) - for building graph, BFS is (n^2*m) - because we can have n^2 edges for n words
    Space - O(n*m^2) - for storing upto n words in each m patterns, each string is m length

    In the un-optimal way we saw that building the adj list took n^2 * m where n was no of words, m was length
    of the words. However, as the problem states the words can be many, but length can be small. We find a way
    to build the graph using patterns which is only n * m^2. And instead of DFS, we choose BFS which allows
    us to find shortest path to the end word optimally. In the end we return the no. of levels we went till
    we reach the end word. 

    Pattern matching basics - we basically convert a string like "hot" to "h*t", "*ot", and "ho*". We map
    all possible patterns to possible words and thats how we know which word can reach which word.
    '''
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






