class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """LC 838. Push Dominoes
        Time complexity: O(N)
        There three cases for the two pointers
        1. 'L...L' or 'R ... R'
        2. 'R...L'
        3. 'L...R'
        Need consider 'R...L' or 'R..L' two cases
        """
        dominoes = 'L' + dominoes + 'R'
        
        left = 0
        right = 1
        
        n = len(dominoes)
        result = []
        
        while right < n:
            if dominoes[right] == '.':
                right += 1
            else:
                if dominoes[right] == dominoes[left]:
                    for i in range(left + 1, right + 1):
                        result.append(dominoes[right])
                elif dominoes[right] == 'L' and dominoes[left] == 'R':
                    m = (right - left - 1) # get number of '.' in between 
                    for i in range( 1 + m // 2 ): # include the boundry one
                        result.append('R')
                    if m % 2 == 1: # add middle '.' if it's necessary
                        result.append('.')
                    for i in range(1 + m // 2):
                        result.append('L')
                else:
                    for i in range(left + 1, right):
                        result.append('.')
                left = right
                right += 1
        return "".join(result)
        