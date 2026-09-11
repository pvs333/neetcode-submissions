class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            seen = set()
            for j in i:
                if j.isdigit():
                    if j in seen:
                        return False
                    seen.add(j)

        for j in range(9):
            seen=set()
            for i in range(9):
                if board[i][j].isdigit():
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])

        start = [[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]

        for k in start:
            seen = set()
            for j in range(k[0], k[0]+3):
                for i in range(k[1], k[1]+3):
                    if board[i][j].isdigit():
                        if board[i][j] in seen:
                            return False
                        seen.add(board[i][j])
        return True
