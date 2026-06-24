class Solution:


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        houses = [set() for _ in range(9)]
        rows =[set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        for i in range (9):
            for j in range(9):
                value = board[i][j]
                if value == ".":
                    continue
                r = i // 3
                c = j//3
                house = (r*3 + c )

                if value in houses[house]:
                    print(f"Found matching in house {house+1}")
                    return False
                else:
                    houses[house].add(value)

                if value in rows[i]:
                    print(value, rows)
                    print(f"Found matching in row {i}")
                    return False
                else:
                    rows[i].add(value)
                
                if value in cols[j]:
                    print(f"Found matching in col {j}")
                    return False
                else:
                    cols[j].add(value)

        return True

        