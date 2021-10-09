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
            record = {'Name' : parse[1], 'Age' : parse[2], 'Score' : parse[3]}
            scdb += [record]
        elif parse[0] == 'del':
            try:
                scdb = [p for p in scdb if p['Name'] != parse[1]]
            except IndexError:
                print("del \"Name\" 형태로 입력하시오.")
        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'find':
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        for attr in sorted(p):
                            print(attr + "=" + p[attr], end=' ')
                        print()
            except IndexError as e:
                print("find \"Name\" 형태로 입력하시오.")
        elif parse[0] == 'inc':
            try:
                for p in scdb:
                    if int(parse[2]) > 0:
                        if p['Name'] == parse[1]:
                            a = int(p['Score'])
                            a += int(parse[2])
                            p['Score'] = str(a)
            except IndexError as e:
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
