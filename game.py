import sys
# import PyQt5.QtWidgets
from sudoku import SudokuCheck
from time import CheckTime
from grid import Grid

# 사용자 인터페이스 레이아웃 생성
class Layout:

# Layout과 상태 표시줄을 포함하는 메인 윈도우
class mainWindow:

    # "Start Game" 버튼에 대한 콜백. grid.py의 class Grid 호출.
    def startGame(self):
        # Layout 설정에서 고정 숫자와 blank의 Layout 재설정
        # time.py의 startTime 호출하여 게임 시작 시간 저장

    # "Submit" 버튼에 대한 콜백. 게임 결과 출력.
    def submitClicked(self):
        # sudoku.py의 finalCheck를 통해 게임 규칙 만족하는지 확인.
        if SudokuCheck.finalCheck == True:
            # 성공하면 time.py의 endTime 호출하여 게임 시간 출력.
            timer = time.endTime
            print(timer)

    # 숫자가 입력될 경우 sudoku.py의 liveCheck 호출.
    def submitEntered(self):
        # 스도쿠 규칙을 만족하지 않으면 빨간 색으로 배경 변화