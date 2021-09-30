import pickle

dbfilename = 'test3_4.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            try:
                record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
                scdb += [record]
            except:
                print("잘못된 입력입니다.")

        elif parse[0] == 'find':
            try:
                keyName = parse[1]
                findScoreDB(scdb, keyName)
            except:
                print("잘못된 입력입니다.")

        elif parse[0] == 'inc':
            #name에 score을 amout만큼 더함
            try:
                keyName = parse[1]
                amout = parse[2]
                incScoreDB(scdb, keyName, amout)
            except:
                print("잘못된 입력입니다.")

        elif parse[0] == 'del':
            try:
                for person in scdb:
                    if person['Name'] == parse[1]:
                        scdb.remove(person)
                    else:
                        continue
            except:
                print("잘못된 입력입니다.")

        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)

        elif parse[0] == 'quit':
            break

        else:
            print("Invalid command: " + parse[0])


#작동 시 호출하는 함수
def showScoreDB(scdb, keyname):
    for person in sorted(scdb, key=lambda person: person[keyname]):
        outScoreDB(person)
        print()

def findScoreDB(scdb, keyName):
    for person in scdb:
        if person['Name'] == keyName:
            outScoreDB(person)
        else:
            continue
        print()

def incScoreDB(scdb, keyName, amout):
    for person in scdb:
        if person['Name'] == keyName:
            person['Score'] = str(int(person['Score']) + int(amout))
        else:
            continue


#출력용 함수: 코드리뷰 이후 수정한 내용(반복제외)
def outScoreDB(person):
    for attr in sorted(person):
        print(attr + "=" + person[attr], end=' ')




#실행장소
scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
