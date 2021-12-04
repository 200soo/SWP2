<사용한 모듈>
PyQt5.QtWidgets
PyQt5.uic
random
datetime
time


<요구사항 수집, 분석>

- 백트래킹 알고리즘을 이용하여 grid 생성
  https://semtax.tistory.com/50

- random을 이용하여 81개 중 45개의 blank grid 선택
  한 행에서 5개씩 랜덤 선택하는 방식
  초기 고정 숫자가 저장된 2차원 리스트 생성

- layout 생성
  blank로 처리된 애들만 접근가능하도록 layout 생성해야함. blank는 흰색. 고정 숫자는 회색으로 처리.
  QLineEdit 사용. textChanged()와 returnPressed() 사용
  한 자리 숫자만 받아야함. 1~9

- 입력된 숫자 처리
  1~9가 입력되면 입력된 숫자를 2차원 리스트에 저장.
  같은 숫자를 찾아서 스도쿠 규칙을 만족하는지 확인. (같은 행, 열인지 확인, 같은 small grid인지 확인(x%3, y%3))
  규칙 만족 안하면 빨간색으로 칸 색상 변경

- submit 버튼
  사용자가 submit 버튼을 입력하면 모든 숫자가 스도쿠 규칙을 만족하는지 확인.
  입력 되지 않은 빈칸이 있다. => 실패
  1~9가 9번씩 입력되지 않았다. => 실패
  행, 열, small grid에 겹치는 숫자가 있다. => 실패
  규칙 모두 만족 => 성공

 - 타이머
  게임 시작할 때 입력 받고 submit 눌려서 성공이면 시간 return

- 게임 성공하면 스도쿠 숫자 변경 불가능


<소프트웨어 구조 설계>

- grid.py
  class Grid : Start Game이 눌리면 스도쿠 퍼즐의 기본 grid 생성
      def promising : 빈칸에 들어갈 수 있는 숫자 후보 리턴
      def dfs : DFS를 이용하여 그리드 인덱스가 9~80인 위치의 숫자 생성
      def createGrid : 스도쿠 게임 규칙을 만족하는 9x9 숫자 grid 생성
      def createBlank : 기본 grid에서 사용자에게 Blank로 보여질, 사용자가 맞추어야 하는 숫자 blank 선택

- game.py
  class SudokuGame : 게임 실행, 동작을 조절하는 코드
      def __init__(self) : 레이아웃 초기화, 콜백 함수 설정
      def startGame(self) : "Start Game" 버튼에 대한 콜백. grid.py의 class Grid 호출.
      def submitClicked(self) : "Submit" 버튼에 대한 콜백. 게임 결과 출력.
      def submitEntered(self, k) : 숫자가 입력될 경우 sudoku.py의 liveCheck 호출.

- mytime.py
  class CheckTime : Start Game 버튼을 누른 시점부터 Submit을 누르고 성공 판결이 날때까지의 시간 체크
      def startTime : time모듈로 현재 시각 starttime에 저장
      def endTime : 현재 시각 - 시작 시간 초 단위 return

- sudoku.py => 스도쿠 그리드를 불러와야 하므로 메모리 손해 -> grid.py에 통합
  class SudokuCheck : 스도쿠 규칙 확인
      def liveCheck : 숫자가 입력될 때 호출됨. 입력된 수의 스도쿠 규칙 만족 여부 확인
      def finalCheck : 입력되지 않은 빈칸이 있을 경우 return False
     		  1~9가 9번씩 입력되지 않을 경우 return False
    		  행, 열, small grid에 겹치는 숫자가 있을 경우 return False
     		  모든 규칙 만족하면 return True

<구현 상세 설계>


<코딩>


<단위 테스트>


<시스템 통합>


<통합 테스트>



