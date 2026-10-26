class Solution:
    from collections import defaultdict
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                if board[i][j] in rows[i]:
                    return False
                rows[i].add(board[i][j])

                if board[i][j] in columns[j]:
                    return False
                columns[j].add(board[i][j])

                box_keys = (i//3, j//3)

                if board[i][j] in boxes[box_keys]:
                    return False
                boxes[box_keys].add(board[i][j])
        return True






        