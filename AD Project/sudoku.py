class SudokuCheck:

    # 숫자가 입력될 때 호출됨. 입력된 수의 스도쿠 규칙 만족 여부 확인
    def liveCheck(self, grid, row, col, num):
        # 행, 열에 같은 숫자 있는지 확인
        for i in range(0, 9):
            if (grid[i][col] == num) or (grid[row][i] == num):
                return False
        # small grid에 같은 숫자 있는지 확인
        row //= 3
        col //= 3
        for i in range(row*3, row*3+3):
            for j in range(col*3, col*3+3):
                if grid[i][j] == num:
                    return False
        return True


    # submit이 입력되면 호출됨.
    def finalCheck(self, grid):
        cnt = [0 for i in range(0, 9)]

        for k in range(0, 81):
            row, col = k//9, k%9
            num = grid[row][col]
            # 입력되지 않은 빈칸이 있을 경우 실패
            if num == 0:
                return False
            cnt[num - 1] += 1
            # 행, 열, small grid에 겹치는 숫자가 있을 경우 실패
            grid[row][col] = 0
            if not SudokuCheck.liveCheck(self, grid, row, col, num):
                return False
            grid[row][col] = 0
        for i in range(0, 9):
            # 1~9가 9번씩 입력되지 않을 경우 실패
            if cnt[i] != 9:
                return False

        # 모든 규칙 만족하면 성공
        return True

