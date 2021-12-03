import sys
import random


# Start Game이 눌리면 스도쿠 퍼즐의 기본 grid 생성
class Grid:

    # 빈칸에 들어갈 수 있는 숫자 후보 리턴
    def promising(self, x, y):
        numbers = [i+1 for i in range(9)]
        # 행, 열에 있는 숫자 제거
        for k in range(9):
            if self.originGrid[x][k] in numbers:
                numbers.remove(self.originGrid[x][k])
            if self.originGrid[k][y] in numbers:
                numbers.remove(self.originGrid[k][y])
        # small grid에 있는 숫자 제거
        x //= 3
        y //= 3
        for i in range(x*3, x*3+3):
            for j in range(y*3, y*3+3):
                if self.originGrid[i][j] in numbers:
                    numbers.remove(self.originGrid[i][j])
        return numbers

    # DFS를 이용하여 그리드 인덱스가 9~80인 위치의 숫자 생성
    def dfs(self, k):
        # 재귀 멈추는 신호가 들어오면 멈추도록 설정
        if self.terminateFlag == True:
            return True

        # 9X9 그리드 범위를 넘으면 재귀 멈춤
        if k > 80:
            self.terminateFlag = True
            return True

        # 9~80 인덱스를 행, 렬로 변환
        row, col = k//9, k%9
        
        prom = Grid.promising(self, row, col)
        # 가능한 숫자가 없을 경우 False 리턴하여 상위 이동
        if not prom:
            return False
        # 빈칸에 들어갈 숫자를 무작위로 섞어 일정한 패턴이 나오지 않도록 설정
        random.shuffle(prom)

        for num in prom:
            self.originGrid[row][col] = num
            if not Grid.dfs(self, k+1):
                self.originGrid[row][col] = 0
            else :
                return True

        return False


    # 스도쿠 게임 규칙을 만족하는 9x9 숫자 grid 생성
    def createGrid(self):
        self.terminateFlag = False

        # 스도쿠 1~9열 0으로 초기화
        self.originGrid = [[0 for j in range(0, 9)] for i in range(0, 9)]

        # 스도쿠 1열 랜덤하게 생성
        self.initNum = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(self.initNum)

        for i in range(9):
            self.originGrid[0][i] = self.initNum[i]

        # 2~9열 스도쿠 생성
        Grid.dfs(self, 9)


    # 기본 grid에서 사용자에게 Blank로 보여질, 사용자가 맞추어야 하는 숫자 blank 선택
    def createBlank(self, difficult):
        self.blankGrid = [[0 for j in range(0, 9)] for i in range(0, 9)]
        for row in range(0, 9):
            for col in range(0, 9):
                # difficult 1~3으로 설정하여 blank 개수 조절
                if random.randint(0, difficult) == 0:
                    self.blankGrid[row][col] = self.originGrid[row][col]
