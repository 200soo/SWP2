import time

# Start Game 버튼을 누른 시점부터 Submit을 누르고 성공 판결이 날때까지의 시간 체크
class CheckTime:

    # time모듈로 현재 시각 starttime에 저장
    def startTime(self):
        self.starttime = time.time()

    # starttime - 현재 시각 return
    def endTime(self):
        self.endtime = time.time()
        return int(self.endtime - self.starttime)
