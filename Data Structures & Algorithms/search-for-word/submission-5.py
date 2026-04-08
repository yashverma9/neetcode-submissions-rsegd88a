class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Un-Optimal - 
        # Time - O(L*m*n*3^L) or O(L*m*n*4^L) as every step except first we have 3 directions to go to, word Length L.
        # We use another L for making new string at every step (VERY UNOPTIMAL) 
        # Space - O(m*n + L) where L is word size - m*n for visited array + L is the depth of recursion which is word length L
        '''
        Backtrack all possible options using visited array. We try backtracking in possible 
        directions from every possible starting point and track visited indeces to avoid
        going through same index in a path. Very unoptimal as every step we are making new string,
        plus we use extra space for a visited array
        '''
        
        row = len(board)
        col = len(board[0])
        found = False

        def backtrack(i, j, string, visited):
            nonlocal found
            if string == word:
                found = True
                return
            
            if len(string) == len(word):
                return

            # Go right
            if j < col - 1 and not visited[i][j+1]:
                visited[i][j+1] = True
                backtrack(i, j + 1, string + board[i][j+1], visited)
                visited[i][j+1] = False

            # Go bottom
            if i < row - 1 and not visited[i+1][j]:
                visited[i+1][j] = True
                backtrack(i + 1, j, string + board[i+1][j], visited)
                visited[i+1][j] = False

            # Go left
            if j > 0 and not visited[i][j-1]:
                visited[i][j-1] = True
                backtrack(i, j - 1, string + board[i][j-1], visited)
                visited[i][j-1] = False

            # Go top
            if i > 0 and not visited[i-1][j]:
                visited[i-1][j] = True
                backtrack(i - 1, j, string + board[i-1][j], visited)
                visited[i-1][j] = False
            return
        

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    visited = [[False for _ in range(col)] for _ in range(row)]
                    visited[i][j] = True
                    backtrack(i, j, board[i][j], visited)
                    if found:
                        return True
        
        return False


        