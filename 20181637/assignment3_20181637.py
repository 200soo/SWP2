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
            record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
            scdb += [record]
        elif parse[0] == 'del': #break 지웠음 / del "이름잘못입력" 했을때 예외처리 안됌
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
            except IndexError:
                print("del \"Name\" 형태로 입력하시오.")
        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'find': #add 하고 find을 하면 안 찾아짐 ㅠㅠ
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        for attr in sorted(p):
                            print(attr + "=" + p[attr], end=' ')
                        print()
                        break
                    else:
                        print("없는 이름입니다.")
                        break
            except IndexError as e:
                print("find \"Name\" 형태로 입력하시오.")
        elif parse[0] == 'inc': #예외처리 실패 ㅠㅠ (인덱스가 아무것도 없을때는 except 넘어가지만 인덱스 하나라도 있으면 오류 x)
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        a = int(p['Score'])
                        a += int(parse[2])
                        p['Score'] = str(a)
            except IndexError as e:\
                print("parse \"Name\" \"Score\" 형태로 입력하시오.")
        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
