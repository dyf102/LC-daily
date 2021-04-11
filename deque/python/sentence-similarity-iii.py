from collections import deque

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        """LC 1813. Sentence Similarity III
        
        Args:
            sentence1 (str): [description]
            sentence2 (str): [description]

        Returns:
            bool: [description]
        """
        q1 = deque(sentence1.split())
        q2 = deque(sentence2.split())
        
        while len(q1) > 0 and len(q2) > 0:
            if q1[0] == q2[0]:
                q1.popleft()
                q2.popleft()
            elif q1[-1] == q2[-1]:
                q1.pop()
                q2.pop()
            else:
                return False
        return len(q1) == 0 or len(q2) == 0
        