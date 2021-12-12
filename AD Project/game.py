import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic

from sudoku import SudokuCheck
from mytime import CheckTime
from grid import Grid

# QtDesigner로 만든 사용자 인터페이스 레이아웃 불러오기
layout = uic.loadUiType("UI_sudoku.ui")[0]

# 게임 실행, 동작을 조절하는 코드
class SudokuGame(QDialog, layout):

    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("PyQt Sudoku - SoftwareProjectII team6")
        
        self.grid = Grid()
        self.mytime = CheckTime()
        self.sudoku = SudokuCheck()

        self.gridText = [self.grid_0, self.grid_1, self.grid_2, self.grid_3, self.grid_4, self.grid_5, self.grid_6, self.grid_7, self.grid_8, self.grid_9, 
                         self.grid_10, self.grid_11, self.grid_12, self.grid_13, self.grid_14, self.grid_15, self.grid_16, self.grid_17, self.grid_18, self.grid_19, 
                         self.grid_20, self.grid_21, self.grid_22, self.grid_23, self.grid_24, self.grid_25, self.grid_26, self.grid_27, self.grid_28, self.grid_29, 
                         self.grid_30, self.grid_31, self.grid_32, self.grid_33, self.grid_34, self.grid_35, self.grid_36, self.grid_37, self.grid_38, self.grid_39,
                         self.grid_40, self.grid_41, self.grid_42, self.grid_43, self.grid_44, self.grid_45, self.grid_46, self.grid_47, self.grid_48, self.grid_49,
                         self.grid_50, self.grid_51, self.grid_52, self.grid_53, self.grid_54, self.grid_55, self.grid_56, self.grid_57, self.grid_58, self.grid_59,
                         self.grid_60, self.grid_61, self.grid_62, self.grid_63, self.grid_64, self.grid_65, self.grid_66, self.grid_67, self.grid_68, self.grid_69,
                         self.grid_70, self.grid_71, self.grid_72, self.grid_73, self.grid_74, self.grid_75, self.grid_76, self.grid_77, self.grid_78, self.grid_79,
                         self.grid_80]
    
        # 콜백 함수 구현
        self.Start_pushButton.clicked.connect(self.startGame)
        self.Submit_pushButton.clicked.connect(self.submitClicked)
        self.Hint_pushButton.clicked.connect(self.hintClicked)
        self.gridText[0].textChanged.connect(lambda: self.submitEntered(0)); self.gridText[1].textChanged.connect(lambda: self.submitEntered(1)); self.gridText[2].textChanged.connect(lambda: self.submitEntered(2)); self.gridText[3].textChanged.connect(lambda: self.submitEntered(3)); self.gridText[4].textChanged.connect(lambda: self.submitEntered(4)); self.gridText[5].textChanged.connect(lambda: self.submitEntered(5)); self.gridText[6].textChanged.connect(lambda: self.submitEntered(6)); self.gridText[7].textChanged.connect(lambda: self.submitEntered(7)); self.gridText[8].textChanged.connect(lambda: self.submitEntered(8)); self.gridText[9].textChanged.connect(lambda: self.submitEntered(9))
        self.gridText[10].textChanged.connect(lambda: self.submitEntered(10)); self.gridText[11].textChanged.connect(lambda: self.submitEntered(11)); self.gridText[12].textChanged.connect(lambda: self.submitEntered(12)); self.gridText[13].textChanged.connect(lambda: self.submitEntered(13)); self.gridText[14].textChanged.connect(lambda: self.submitEntered(14)); self.gridText[15].textChanged.connect(lambda: self.submitEntered(15)); self.gridText[16].textChanged.connect(lambda: self.submitEntered(16)); self.gridText[17].textChanged.connect(lambda: self.submitEntered(17)); self.gridText[18].textChanged.connect(lambda: self.submitEntered(18)); self.gridText[19].textChanged.connect(lambda: self.submitEntered(19))
        self.gridText[20].textChanged.connect(lambda: self.submitEntered(20)); self.gridText[21].textChanged.connect(lambda: self.submitEntered(21)); self.gridText[22].textChanged.connect(lambda: self.submitEntered(22)); self.gridText[23].textChanged.connect(lambda: self.submitEntered(23)); self.gridText[24].textChanged.connect(lambda: self.submitEntered(24)); self.gridText[25].textChanged.connect(lambda: self.submitEntered(25)); self.gridText[26].textChanged.connect(lambda: self.submitEntered(26)); self.gridText[27].textChanged.connect(lambda: self.submitEntered(27)); self.gridText[28].textChanged.connect(lambda: self.submitEntered(28)); self.gridText[29].textChanged.connect(lambda: self.submitEntered(29))
        self.gridText[30].textChanged.connect(lambda: self.submitEntered(30)); self.gridText[31].textChanged.connect(lambda: self.submitEntered(31)); self.gridText[32].textChanged.connect(lambda: self.submitEntered(32)); self.gridText[33].textChanged.connect(lambda: self.submitEntered(33)); self.gridText[34].textChanged.connect(lambda: self.submitEntered(34)); self.gridText[35].textChanged.connect(lambda: self.submitEntered(35)); self.gridText[36].textChanged.connect(lambda: self.submitEntered(36)); self.gridText[37].textChanged.connect(lambda: self.submitEntered(37)); self.gridText[38].textChanged.connect(lambda: self.submitEntered(38)); self.gridText[39].textChanged.connect(lambda: self.submitEntered(39))
        self.gridText[40].textChanged.connect(lambda: self.submitEntered(40)); self.gridText[41].textChanged.connect(lambda: self.submitEntered(41)); self.gridText[42].textChanged.connect(lambda: self.submitEntered(42)); self.gridText[43].textChanged.connect(lambda: self.submitEntered(43)); self.gridText[44].textChanged.connect(lambda: self.submitEntered(44)); self.gridText[45].textChanged.connect(lambda: self.submitEntered(45)); self.gridText[46].textChanged.connect(lambda: self.submitEntered(46)); self.gridText[47].textChanged.connect(lambda: self.submitEntered(47)); self.gridText[48].textChanged.connect(lambda: self.submitEntered(48)); self.gridText[49].textChanged.connect(lambda: self.submitEntered(49))
        self.gridText[50].textChanged.connect(lambda: self.submitEntered(50)); self.gridText[51].textChanged.connect(lambda: self.submitEntered(51)); self.gridText[52].textChanged.connect(lambda: self.submitEntered(52)); self.gridText[53].textChanged.connect(lambda: self.submitEntered(53)); self.gridText[54].textChanged.connect(lambda: self.submitEntered(54)); self.gridText[55].textChanged.connect(lambda: self.submitEntered(55)); self.gridText[56].textChanged.connect(lambda: self.submitEntered(56)); self.gridText[57].textChanged.connect(lambda: self.submitEntered(57)); self.gridText[58].textChanged.connect(lambda: self.submitEntered(58)); self.gridText[59].textChanged.connect(lambda: self.submitEntered(59))
        self.gridText[60].textChanged.connect(lambda: self.submitEntered(60)); self.gridText[61].textChanged.connect(lambda: self.submitEntered(61)); self.gridText[62].textChanged.connect(lambda: self.submitEntered(62)); self.gridText[63].textChanged.connect(lambda: self.submitEntered(63)); self.gridText[64].textChanged.connect(lambda: self.submitEntered(64)); self.gridText[65].textChanged.connect(lambda: self.submitEntered(65)); self.gridText[66].textChanged.connect(lambda: self.submitEntered(66)); self.gridText[67].textChanged.connect(lambda: self.submitEntered(67)); self.gridText[68].textChanged.connect(lambda: self.submitEntered(68)); self.gridText[69].textChanged.connect(lambda: self.submitEntered(69))
        self.gridText[70].textChanged.connect(lambda: self.submitEntered(70)); self.gridText[71].textChanged.connect(lambda: self.submitEntered(71)); self.gridText[72].textChanged.connect(lambda: self.submitEntered(72)); self.gridText[73].textChanged.connect(lambda: self.submitEntered(73)); self.gridText[74].textChanged.connect(lambda: self.submitEntered(74)); self.gridText[75].textChanged.connect(lambda: self.submitEntered(75)); self.gridText[76].textChanged.connect(lambda: self.submitEntered(76)); self.gridText[77].textChanged.connect(lambda: self.submitEntered(77)); self.gridText[78].textChanged.connect(lambda: self.submitEntered(78)); self.gridText[79].textChanged.connect(lambda: self.submitEntered(79))
        self.gridText[80].textChanged.connect(lambda: self.submitEntered(80)); 
        
        # 초기화면에서 입력 불가하게 설정
        for k in range(0, 81):
            row, col = k//9, k%9
            self.gridText[k].setReadOnly(True)

        self.hintNum = -1


    # "Start" 버튼에 대한 콜백. grid.py의 class Grid 호출.
    def startGame(self):
        # grid 빈칸으로 초기화
        for k in range(0, 81):
            row, col = k//9, k%9
            self.gridText[k].setText('')
            self.gridText[k].setReadOnly(False)

        # 난이도 확인 후 스도쿠 생성
        if self.Mode_ComboBox.currentText() == 'easy':
            dif = 2
        else:
            dif = 1

        self.grid.createGrid()
        self.grid.createBlank(dif)

        for row in range(0, 9):
            for col in range(0, 9):
                if self.grid.blankGrid[row][col] != 0:
                    num = str(self.grid.blankGrid[row][col])
                    k = row*9+col
                    self.gridText[k].setReadOnly(True)
                    self.gridText[k].setText(num)
                    self.gridText[k].setStyleSheet("background: rgb(233, 233, 233)")

        # time.py의 startTime 호출하여 게임 시작 시간 저장
        self.mytime.startTime()
        # 선택된 빈칸 쓰레기 값으로 초기화
        self.hintNum = 2
        self.Result_Window.setText('Only '+str(self.hintNum)+' hint left')


    # "Hint" 버튼에 대한 콜백. 마지막으로 클릭된 빈칸의 정답을 알려준다
    def hintClicked(self):
        # 게임 시작 전 힌트 사용 불가
        if self.hintNum == -1:
            self.Result_Window.setText('Input Error!')
            return
        # 힌트 2번 사용하면 힌트 사용불가
        elif self.hintNum < 1:
            self.Result_Window.setText('No more hint!')
            return
        # row, col 받아서 에러처리
        row = self.Row_Window.text()
        col = self.Col_Window.text()
        if not (row.isdigit() and col.isdigit()):
            self.Result_Window.setText('Input Error!')
            self.Row_Window.setText('')
            self.Col_Window.setText('')
            return
        row, col = int(row)-1, int(col)-1
        if not ((0 <= row <= 8) and (0 <= col <= 8)):
            self.Row_Window.setText('')
            self.Col_Window.setText('')
            self.Result_Window.setText('Input Error!')
            return
        k = row*9 + col
        if not 0 <= k <= 80:
            return
        if self.grid.blankGrid[row][col] != 0:
            self.Result_Window.setText('Already Entered!')
            return
        num = self.grid.originGrid[row][col]
        self.gridText[k].setText(str(num))
        self.gridText[k].setStyleSheet("background: rgb(233, 233, 233)")
        self.gridText[k].setReadOnly(True)
        self.grid.blankGrid[row][col] = num
        self.hintNum -= 1
        self.Result_Window.setText('Only '+str(self.hintNum)+' hint left')


        
    # "Submit" 버튼에 대한 콜백. 게임 결과 출력.
    def submitClicked(self):
        try:
            # sudoku.py의 finalCheck를 통해 게임 규칙 만족하는지 확인.
            if self.sudoku.finalCheck(self.grid.blankGrid) == True:
                # 성공하면 time.py의 endTime 호출하여 게임 시간 출력.
                timer = str(self.mytime.endTime())
                timer += 'sec'
                self.Result_Window.setText(timer)
                # gridText 수정 불가하게 설정
                for k in range(0, 80):
                    self.gridText[k].setReadOnly(True)
            else:
                self.Result_Window.setText('Try Again!')
        except:
                self.Result_Window.setText('Error!')



    # 숫자가 입력될 경우 sudoku.py의 liveCheck 호출.
    def submitEntered(self, k):
        row, col = k//9, k%9
        self.grid.blankGrid[row][col] = 0
        self.gridText[k].setStyleSheet("background: rgb(255, 255, 255)")
        text = self.gridText[k].text()
        if not text.isdigit():
            if text == '':
                return
            else:
                self.gridText[k].setText('')
                return
        else:
            num = int(text)
            if (1 <= num <= 9):
                # blankGrid에 항목 추가
                if self.sudoku.liveCheck(self.grid.blankGrid, row, col, num) == 1:
                    # 스도쿠 규칙 만족하면 배경 흰색으로
                    self.gridText[k].setStyleSheet("background: rgb(255, 255, 255)")
                else:
                    # 스도쿠 규칙을 만족하지 않으면 빨간 색으로 배경 변화
                    self.gridText[k].setStyleSheet("background: rgb(255, 200, 200)")
                
                self.grid.blankGrid[row][col] = num
            else:
                self.grid.blankGrid[row][col] = 0
                self.gridText[k].setText('')
                self.gridText[k].setStyleSheet("background: rgb(255, 200, 200)")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = SudokuGame()
    game.show()
    sys.exit(app.exec_())