from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        foundTheWord = False
        def dfs(x, y, indexOfLetter):

            nonlocal foundTheWord
            
            # If the index is greater than the length of word, then we are done.
            if indexOfLetter >= len(word):
                foundTheWord = True
                return
                
            # if we are out of bounds of the board, we stop searching.
            outOfBoundsInY = y < 0 or y >= len(board)
            outOfBoundsInX = x < 0 or x >= len(board[0])

            if outOfBoundsInX or outOfBoundsInY:
                return
            
            # Grab the letter we are looking for.
            # And Grab all 4 possible directions and we search if the letter works.

            letterRequired = word[indexOfLetter]
            elementAtBoardCoordinate = board[y][x]
            
            if elementAtBoardCoordinate != letterRequired:
                return
            #print(indexOfLetter, elementAtBoardCoordinate, letterRequired, (x,y), foundTheWord)

            # If the current letter is correct, we search for adjacent letters in the next index.
            # and we change the current board value at [y][x] so we don't re-search this node.
            board[y][x] = "#"
            
            # up
            dfs(x, y + 1, indexOfLetter + 1)

            # down
            dfs(x, y - 1, indexOfLetter + 1)


            # left
            dfs(x - 1, y, indexOfLetter + 1)

            # right
            dfs(x + 1, y, indexOfLetter + 1)
            
            board[y][x] = elementAtBoardCoordinate
        
        for i in range(len(board[0])):
            for j in range(len(board)):
                dfs(i, j, 0)
        
        return foundTheWord

if __name__ == '__main__':
    print("Successfully compiled the solution")
