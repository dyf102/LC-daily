from collections import defaultdict, deque
import heapq

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """LC 127. Word Ladder
        BFS solution
        O(V + E)
        Better for unweighed graph
        Args:
            beginWord (str): [description]
            endWord (str): [description]
            wordList (List[str]): [description]

        Returns:
            int: [description]
        """
        n = len(wordList)
        startIdx = n
        try:
            endIdx = wordList.index(endWord)
        except ValueError:
            return 0
        wordList.append(beginWord)
        n += 1
        
        _map = [[False] * n for _ in range(n)]
        
        def isConnect(s1, s2):
            count = 0
            for i, c in enumerate(s1):
                if c != s2[i]:
                    count += 1
                    if count > 1:
                        return False
            return count == 1
        
        for i in range(n):
            for j in range(n):
                if i != j:
                    _map[i][j] = isConnect(wordList[i], wordList[j])
        
        queue = deque([startIdx])
        visited = [False] * n
        shortest = 0
        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                current = queue.popleft()
                if current == endIdx:
                    return shortest + 1
                visited[current] = True
                for j in range(n):
                    if _map[current][j] and not visited[j]:
                        queue.append(j)
            shortest += 1
        return 0
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Dikistra solution
        O(V + E*(Log(v)))
        """
        n = len(wordList)
        startIdx = n
        try:
            endIdx = wordList.index(endWord)
        except ValueError:
            return 0
        wordList.append(beginWord)
        n += 1
        
        _map = defaultdict(list)
        
        def isConnect(s1, s2):
            count = 0
            for i, c in enumerate(s1):
                if c != s2[i]:
                    count += 1
                    if count > 1:
                        return False
            return count == 1
        
        for i in range(n):
            for j in range(i + 1, n):
                if isConnect(wordList[i], wordList[j]):
                    _map[j].append(i)
                    _map[i].append(j)
        queue = [(0, startIdx)]
        
        dist = [n] * n
        dist[startIdx] = 0
        while len(queue) > 0:
            w, current = heapq.heappop(queue)
            if current == endIdx:
                return dist[endIdx] + 1
            for j in _map[current]:
                if dist[j] > dist[current] + 1:
                    dist[j] = dist[current] + 1
                    queue.append((w + 1, j))

        return 0