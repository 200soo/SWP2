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
                print("Try again")

        # del name으로 주어진 name이 같은 모든 사람 레코드 제거
        elif parse[0] == 'del':
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
                    else:
            except:
                print("Try again")

        # find name으로 주어진 name의 사람만 찾아서 출력
        elif parse[0] == 'find':
            try:
                keyName = parse[1]
                findScoreDB(scdb, keyName)
            except:
                print("Try again")

        # inc name amount로 주어진 name의 사람만 찾아서 score를 amount만큼 더해줌
        elif parse[0] == 'inc':
            try:
                keyName = parse[1]
                amount = parse[2]
                incScoreDB(scdb, keyName, amount)
            except:
                print("Try again")

        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)

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
