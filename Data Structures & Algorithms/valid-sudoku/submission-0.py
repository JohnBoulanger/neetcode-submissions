class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # pass through board only once
        # track 27 sets, 1 for each row, col, 3x3
        colSets = [set() for _ in range(9)]
        rowSets = [set() for _ in range(9)]
        # top letf, top middle, top right, middle left, etc...
        gridSets = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                # compute grids box set
                box = ((row // 3) * 3) + ((col // 3))
                if val == ".": continue
                # check if in any of the sets
                if val in colSets[col] or val in rowSets[row] or val in gridSets[box]: return False
                # if not add them to sets
                colSets[col].add(val)
                rowSets[row].add(val)
                gridSets[box].add(val)            

        return True