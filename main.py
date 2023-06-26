from colorama import Fore, Back, Style

wpawn = [[0, 1], "pawn"]
wpawn1 = [[1, 1], "pawn"]
wpawn2 = [[2, 1], "pawn"]
wpawn3 = [[3, 1], "pawn"]
wpawn4 = [[4, 1], "pawn"]
wpawn5 = [[5, 1], "pawn"]
wpawn6 = [[6, 1], "pawn"]
wpawn7 = [[7, 1], "pawn"]
wcastle = [[0, 0], "castle"]
wknight = [[1, 0], "knight"]
wbishop = [[2, 0], "bishop"]
wking = [[3, 0], "king"]
wqueenn = [[4, 0], "queen"]
wbishop1 = [[5, 0], "bishop"]
wknight2 = [[6, 0], "knight"]
wcastle2 = [[7, 0], "castle"]
bpawn = [[0, 6], "bpawn"]
bpawn1 = [[1, 6], "bpawn"]
bpawn2 = [[2, 6], "bpawn"]
bpawn3 = [[3, 6], "bpawn"]
bpawn4 = [[4, 6], "bpawn"]
bpawn5 = [[5, 6], "bpawn"]
bpawn6 = [[6, 6], "bpawn"]
bpawn7 = [[7, 6], "bpawn"]
bcastle = [[0, 7], "castle"]
bknight = [[1, 7], "knight"]
bbishop = [[2, 7], "bishop"]
bking = [[3, 7], "king"]
bqueen = [[4, 7], "queen"]
bbishop1 = [[5, 7], "bishop"]
bknight2 = [[6, 7], "knight"]
bcastle2 = [[7, 7], "castle"]
count = 0

taken = []
wking_threat = []
bking_threat = []

white = [wcastle, wknight, wbishop, wqueenn, wking, wbishop1, wknight2, wcastle2,
         wpawn, wpawn1, wpawn2, wpawn3, wpawn4, wpawn5, wpawn6, wpawn7]
whitetaken = []
black = [bcastle, bknight, bbishop, bqueen, bking, bbishop1, bknight2, bcastle2,
         bpawn, bpawn1, bpawn2, bpawn3, bpawn4, bpawn5, bpawn6, bpawn7]
blacktaken = []
for x in range(len(white)):
    taken.append(white[x][0])
    whitetaken.append(white[x][0])

for x in range(len(black)):
    taken.append(black[x][0])
    blacktaken.append(black[x][0])


def getpiece(x):
    for a in range(len(white)):
        if (white[a][0]) == x:
            return (white[a])


def badlist():
    test = []
    for i in range(-25, 0):
        for b in range(-1, 25):
            taken.append([i, b])
    for i in range(8, 25):
        for b in range(-1, 25):
            taken.append([b, i])
    for i in range(8, 25):
        for b in range(-1, 25):
            taken.append([i, b])
    for i in range(-25, 0):
        for b in range(-1, 25):
            taken.append([b, i])
    for i in range(-25, 0):
        for b in range(-25, 0):
            taken.append([b, i])


def death(x):
    global wpawn
    global wpawn1
    global wpawn2
    global wpawn3
    global wpawn4
    global wpawn5
    global wpawn6
    global wpawn7
    global wcastle
    global wcastle2
    global wknight
    global wknight2
    global wbishop
    global wbishop1
    global wking
    global wqueenn
    global white
    global bpawn
    global bpawn1
    global bpawn2
    global bpawn3
    global bpawn4
    global bpawn5
    global bpawn6
    global bpawn7
    global bcastle
    global bcastle2
    global bknight
    global bknight2
    global bbishop
    global bbishop1
    global bking
    global bqueen
    global black
    global taken
    global blacktaken
    global whitetaken
    taken.remove(x)
    if x in blacktaken:
        blacktaken.remove(x)
    if x in whitetaken:
        whitetaken.remove(x)
    death = [100, 100]
    if x == wpawn[0]:
        wpawn[0] = [100,100]
    if x == wpawn1[0]:
        wpawn1[0] = death
    if x == wpawn2[0]:
        wpawn2[0] = death
    if x == wpawn3[0]:
        wpawn3[0] = death
    if x == wpawn4[0]:
        wpawn4[0] = death
    if x == wpawn5[0]:
        wpawn5[0] = death
    if x == wpawn6[0]:
        wpawn6[0] = death
    if x == wpawn7[0]:
        wpawn7[0] = death
    if x == wcastle[0]:
        wcastle[0] = death
    if x == wcastle2[0]:
        wcastle2[0] = death
    if x == wknight[0]:
        wknight[0] = death
    if x == wknight2[0]:
        wknight2[0] = death
    if x == wbishop[0]:
        wbishop[0] = death
    if x == wbishop1[0]:
        wbishop1[0] = death
    if x == wking[0]:
        wking[0] = death
    if x == wqueenn[0]:
        wqueenn[0] = death
    if x == bpawn[0]:
        bpawn[0] = death
    if x == bpawn1[0]:
        bpawn1[0] = death
    if x == bpawn2[0]:
        bpawn2[0] = death
    if x == bpawn3[0]:
        bpawn3[0] = death
    if x == bpawn4[0]:
        bpawn4[0] = death
    if x == bpawn5[0]:
        bpawn5[0] = death
    if x == bpawn6[0]:
        bpawn6[0] = death
    if x == bpawn7[0]:
        bpawn7[0] = death
    if x == bcastle[0]:
        bcastle[0] = death
    if x == bcastle2[0]:
        bcastle2[0] = death
    if x == bknight[0]:
        bknight[0] = death
    if x == bknight2[0]:
        bknight2[0] = death
    if x == bbishop[0]:
        bbishop[0] = death
    if x == bbishop1[0]:
        bbishop1[0] = death
    if x == bking[0]:
        bking[0] = death
    if x == bqueen[0]:
        bqueen[0] = death


badlist()


def changeLocation(x, pieces):
    global wpawn
    global wpawn1
    global wpawn2
    global wpawn3
    global wpawn4
    global wpawn5
    global wpawn6
    global wpawn7
    global wcastle
    global wcastle2
    global wknight
    global wknight2
    global wbishop
    global wbishop1
    global wking
    global wqueenn
    global white
    global bpawn
    global bpawn1
    global bpawn2
    global bpawn3
    global bpawn4
    global bpawn5
    global bpawn6
    global bpawn7
    global bcastle
    global bcastle2
    global bknight
    global bknight2
    global bbishop
    global bbishop1
    global bking
    global bqueen
    global black
    global taken
    global blacktaken
    global whitetaken
    if pieces == wpawn:
        taken.remove(getLocation(wpawn))
        taken.append([x[0], x[1]])
        wpawn = [[x[0], x[1]], pieces[1]]

    if pieces == wpawn1:
        taken.remove(getLocation(wpawn1))
        taken.append([x[0], x[1]])
        wpawn1 = [[x[0], x[1]], pieces[1]]

    if pieces == wpawn2:
        taken.remove(getLocation(wpawn2))
        taken.append([x[0], x[1]])
        wpawn2 = [[x[0], x[1]], pieces[1]]
    if pieces == wpawn3:
        taken.remove(getLocation(wpawn3))
        taken.append([x[0], x[1]])
        wpawn3 = [[x[0], x[1]], pieces[1]]

        wpawn3 = [[x[0], x[1]], pieces[1]]
    if pieces == wpawn4:
        taken.remove(getLocation(wpawn4))
        taken.append([x[0], x[1]])
        wpawn4 = [[x[0], x[1]], pieces[1]]
    if pieces == wpawn5:
        taken.remove(getLocation(wpawn5))
        taken.append([x[0], x[1]])
        wpawn5 = [[x[0], x[1]], pieces[1]]
    if pieces == wpawn6:
        taken.remove(getLocation(wpawn6))
        taken.append([x[0], x[1]])
        wpawn6 = [[x[0], x[1]], pieces[1]]
    if pieces == wpawn7:
        taken.remove(getLocation(wpawn7))
        taken.append([x[0], x[1]])
        wpawn7 = [[x[0], x[1]], pieces[1]]
    if pieces == wcastle:
        taken.remove(getLocation(wcastle))
        taken.append([x[0], x[1]])
        wcastle = [[x[0], x[1]], pieces[1]]
    if pieces == wcastle2:
        taken.remove(getLocation(wcastle2))
        taken.append([x[0], x[1]])
        wcastle2 = [[x[0], x[1]], pieces[1]]
    if pieces == wknight:
        taken.remove(getLocation(wknight))
        taken.append([x[0], x[1]])
        wknight = [[x[0], x[1]], pieces[1]]
    if pieces == wknight2:
        taken.remove(getLocation(wknight2))
        taken.append([x[0], x[1]])
        wknight2 = [[x[0], x[1]], pieces[1]]
    if pieces == wbishop:
        taken.remove(getLocation(wbishop))
        taken.append([x[0], x[1]])
        wbishop = [[x[0], x[1]], pieces[1]]
    if pieces == wbishop1:
        taken.remove(getLocation(wbishop1))
        taken.append([x[0], x[1]])
        wbishop1 = [[x[0], x[1]], pieces[1]]
    if pieces == wking:
        taken.remove(getLocation(wking))
        taken.append([x[0], x[1]])
        wking = [[x[0], x[1]], pieces[1]]
    if pieces == wqueenn:
        taken.remove(getLocation(wking))
        taken.append([x[0], x[1]])
        wqueenn = [[x[0], x[1]], pieces[1]]
    temp = list(black)
    for a in temp:

        if a == pieces:
            temp.remove(a)
            a = [[x[0], x[1]], pieces[1]]
            temp.append(a)
    black = temp
    if pieces == bpawn:
        taken.remove(getLocation(bpawn))
        taken.append([x[0], x[1]])
        bpawn = [[x[0], x[1]], pieces[1]]

    if pieces == bpawn1:
        taken.remove(getLocation(bpawn1))
        taken.append([x[0], x[1]])
        bpawn1 = [[x[0], x[1]], pieces[1]]
    if pieces == bpawn2:
        taken.remove(getLocation(bpawn2))
        taken.append([x[0], x[1]])
        bpawn2 = [[x[0], x[1]], pieces[1]]
    if pieces == bpawn3:
        taken.remove(getLocation(bpawn3))
        taken.append([x[0], x[1]])
        bpawn3 = [[x[0], x[1]], pieces[1]]
    if pieces == bpawn4:
        taken.remove(getLocation(bpawn4))
        taken.append([x[0], x[1]])
        bpawn4 = [[x[0], x[1]], pieces[1]]
    if pieces == bpawn5:
        taken.remove(getLocation(bpawn5))
        taken.append([x[0], x[1]])
        bpawn5 = [[x[0], x[1]], pieces[1]]
    if pieces == bpawn6:
        taken.remove(getLocation(bpawn6))
        taken.append([x[0], x[1]])
        bpawn6 = [[x[0], x[1]], pieces[1]]
    if pieces == bpawn7:
        taken.remove(getLocation(bpawn7))
        taken.append([x[0], x[1]])
        bpawn7 = [[x[0], x[1]], pieces[1]]
    if pieces == bcastle:
        taken.remove(getLocation(bcastle))
        taken.append([x[0], x[1]])
        bcastle = [[x[0], x[1]], pieces[1]]
    if pieces == bcastle2:
        taken.remove(getLocation(bcastle2))
        taken.append([x[0], x[1]])
        bcastle2 = [[x[0], x[1]], pieces[1]]
    if pieces == bknight:
        taken.remove(getLocation(bknight))
        taken.append([x[0], x[1]])
        bknight = [[x[0], x[1]], pieces[1]]
    if pieces == bknight2:
        taken.remove(getLocation(bknight2))
        taken.append([x[0], x[1]])
        bknight2 = [[x[0], x[1]], pieces[1]]
    if pieces == bbishop:
        taken.remove(getLocation(bbishop))
        taken.append([x[0], x[1]])
        bbishop = [[x[0], x[1]], pieces[1]]
    if pieces == bbishop1:
        taken.remove(getLocation(bbishop1))
        taken.append([x[0], x[1]])
        bbishop1 = [[x[0], x[1]], pieces[1]]
    if pieces == bking:
        taken.remove(getLocation(bking))
        taken.append([x[0], x[1]])
        bking = [[x[0], x[1]], pieces[1]]
    if pieces == bqueen:
        taken.remove(getLocation(bking))
        taken.append([x[0], x[1]])
        bqueen = [[x[0], x[1]], pieces[1]]

        # print(a)


def getLocation(pieces):
    return pieces[0]


def setLocation(x, pieces):
    global wpawn
    global wpawn1
    global wpawn2
    global wpawn3
    global wpawn4
    global wpawn5
    global wpawn6
    global wpawn7
    global wcastle
    global wcastle2
    global wknight
    global wknight2
    global wbishop
    global wbishop1
    global wking
    global wqueenn
    global white
    global bpawn
    global bpawn1
    global bpawn2
    global bpawn3
    global bpawn4
    global bpawn5
    global bpawn6
    global bpawn7
    global bcastle
    global bcastle2
    global bknight
    global bknight2
    global bbishop
    global bbishop1
    global bking
    global bqueen
    global black
    global taken
    global blacktaken
    global whitetaken

    temp = list(white)
    for a in temp:

        if a == pieces:
            temp.remove(a)
            a = [x[0], x[1]], pieces[1]
            temp.append(a)
    white = temp
    if pieces == wpawn:
        whitetaken.remove(getLocation(wpawn))
        whitetaken.append([x[0], x[1]])
        taken.remove(getLocation(wpawn))
        taken.append([x[0], x[1]])
        wpawn = [[x[0], x[1]], pieces[1]]

    if pieces == wpawn1:
        whitetaken.remove(getLocation(wpawn1))
        whitetaken.append([x[0], x[1]])
        taken.remove(getLocation(wpawn1))
        taken.append([x[0], x[1]])
        wpawn1 = [[x[0], x[1]], pieces[1]]
    if pieces == wpawn2:
        whitetaken.remove(getLocation(wpawn2))
        whitetaken.append([x[0], x[1]])
        taken.remove(getLocation(wpawn2))
        taken.append([x[0], x[1]])
        wpawn2 = [[x[0], x[1]], pieces[1]]
    if pieces == wpawn3:
        whitetaken.remove(getLocation(wpawn3))
        whitetaken.append([x[0], x[1]])
        taken.remove(getLocation(wpawn3))
        taken.append([x[0], x[1]])
        wpawn3 = [[x[0], x[1]], pieces[1]]
    if pieces == wpawn4:
        whitetaken.remove(getLocation(wpawn4))
        whitetaken.append([x[0], x[1]])
        taken.remove(getLocation(wpawn4))
        taken.append([x[0], x[1]])
        wpawn4 = [[x[0], x[1]], pieces[1]]
    if pieces == wpawn5:
        whitetaken.remove(getLocation(wpawn5))
        whitetaken.append([x[0], x[1]])
        taken.remove(getLocation(wpawn5))
        taken.append([x[0], x[1]])
        wpawn5 = [[x[0], x[1]], pieces[1]]
    if pieces == wpawn6:
        whitetaken.remove(getLocation(wpawn6))
        whitetaken.append([x[0], x[1]])
        taken.remove(getLocation(wpawn6))
        taken.append([x[0], x[1]])
        wpawn6 = [[x[0], x[1]], pieces[1]]
    if pieces == wpawn7:
        whitetaken.remove(getLocation(wpawn7))
        whitetaken.append([x[0], x[1]])
        taken.remove(getLocation(wpawn7))
        taken.append([x[0], x[1]])
        wpawn7 = [[x[0], x[1]], pieces[1]]
    if pieces == wcastle:
        whitetaken.remove(getLocation(wcastle))
        whitetaken.append([x[0], x[1]])
        taken.remove(getLocation(wcastle))
        taken.append([x[0], x[1]])
        wcastle = [[x[0], x[1]], pieces[1]]
    if pieces == wcastle2:
        whitetaken.remove(getLocation(wcastle2))
        whitetaken.append([x[0], x[1]])
        taken.remove(getLocation(wcastle2))
        taken.append([x[0], x[1]])
        wcastle2 = [[x[0], x[1]], pieces[1]]
    if pieces == wknight:
        whitetaken.remove(getLocation(wknight))
        whitetaken.append([x[0], x[1]])
        taken.remove(getLocation(wknight))
        taken.append([x[0], x[1]])
        wknight = [[x[0], x[1]], pieces[1]]
    if pieces == wknight2:
        whitetaken.remove(getLocation(wknight2))
        whitetaken.append([x[0], x[1]])
        taken.remove(getLocation(wknight2))
        taken.append([x[0], x[1]])
        wknight2 = [[x[0], x[1]], pieces[1]]
    if pieces == wbishop:
        whitetaken.remove(getLocation(wbishop))
        whitetaken.append([x[0], x[1]])
        taken.remove(getLocation(wbishop))
        taken.append([x[0], x[1]])
        wbishop = [[x[0], x[1]], pieces[1]]
    if pieces == wbishop1:
        whitetaken.remove(getLocation(wbishop1))
        whitetaken.append([x[0], x[1]])
        taken.remove(getLocation(wbishop1))
        taken.append([x[0], x[1]])
        wbishop1 = [[x[0], x[1]], pieces[1]]
    if pieces == wking:
        whitetaken.remove(getLocation(wking))
        whitetaken.append([x[0], x[1]])
        taken.remove(getLocation(wking))
        taken.append([x[0], x[1]])
        wking = [[x[0], x[1]], pieces[1]]
    if pieces == wqueenn:
        whitetaken.remove(getLocation(wqueenn))
        whitetaken.append([x[0], x[1]])
        taken.remove(getLocation(wking))
        taken.append([x[0], x[1]])
        wqueenn = [[x[0], x[1]], pieces[1]]
    temp = list(black)
    for a in temp:

        if a == pieces:
            temp.remove(a)
            a = [[x[0], x[1]], pieces[1]]
            temp.append(a)
    black = temp
    if pieces == bpawn:
        blacktaken.remove(getLocation(bpawn))
        blacktaken.append([x[0], x[1]])
        taken.remove(getLocation(bpawn))
        taken.append([x[0], x[1]])
        bpawn = [[x[0], x[1]], pieces[1]]

    if pieces == bpawn1:
        blacktaken.remove(getLocation(bpawn1))
        blacktaken.append([x[0], x[1]])
        taken.remove(getLocation(bpawn1))
        taken.append([x[0], x[1]])
        bpawn1 = [[x[0], x[1]], pieces[1]]
    if pieces == bpawn2:
        blacktaken.remove(getLocation(bpawn2))
        blacktaken.append([x[0], x[1]])
        taken.remove(getLocation(bpawn2))
        taken.append([x[0], x[1]])
        bpawn2 = [[x[0], x[1]], pieces[1]]
    if pieces == bpawn3:
        blacktaken.remove(getLocation(bpawn3))
        blacktaken.append([x[0], x[1]])
        taken.remove(getLocation(bpawn3))
        taken.append([x[0], x[1]])
        bpawn3 = [[x[0], x[1]], pieces[1]]
    if pieces == bpawn4:
        blacktaken.remove(getLocation(bpawn4))
        blacktaken.append([x[0], x[1]])
        taken.remove(getLocation(bpawn4))
        taken.append([x[0], x[1]])
        bpawn4 = [[x[0], x[1]], pieces[1]]
    if pieces == bpawn5:
        blacktaken.remove(getLocation(bpawn5))
        blacktaken.append([x[0], x[1]])
        taken.remove(getLocation(bpawn5))
        taken.append([x[0], x[1]])
        bpawn5 = [[x[0], x[1]], pieces[1]]
    if pieces == bpawn6:
        blacktaken.remove(getLocation(bpawn6))
        blacktaken.append([x[0], x[1]])
        taken.remove(getLocation(bpawn6))
        taken.append([x[0], x[1]])
        bpawn6 = [[x[0], x[1]], pieces[1]]
    if pieces == bpawn7:
        blacktaken.remove(getLocation(bpawn7))
        blacktaken.append([x[0], x[1]])
        taken.remove(getLocation(bpawn7))
        taken.append([x[0], x[1]])
        bpawn7 = [[x[0], x[1]], pieces[1]]
    if pieces == bcastle:
        blacktaken.remove(getLocation(bcastle))
        blacktaken.append([x[0], x[1]])
        taken.remove(getLocation(bcastle))
        taken.append([x[0], x[1]])
        bcastle = [[x[0], x[1]], pieces[1]]
    if pieces == bcastle2:
        blacktaken.remove(getLocation(bcastle2))
        blacktaken.append([x[0], x[1]])
        taken.remove(getLocation(bcastle2))
        taken.append([x[0], x[1]])
        bcastle2 = [[x[0], x[1]], pieces[1]]
    if pieces == bknight:
        blacktaken.remove(getLocation(bknight))
        blacktaken.append([x[0], x[1]])
        taken.remove(getLocation(bknight))
        taken.append([x[0], x[1]])
        bknight = [[x[0], x[1]], pieces[1]]
    if pieces == bknight2:
        blacktaken.remove(getLocation(bknight2))
        blacktaken.append([x[0], x[1]])
        taken.remove(getLocation(bknight2))
        taken.append([x[0], x[1]])
        bknight2 = [[x[0], x[1]], pieces[1]]
    if pieces == bbishop:
        blacktaken.remove(getLocation(bbishop))
        blacktaken.append([x[0], x[1]])
        taken.remove(getLocation(bbishop))
        taken.append([x[0], x[1]])
        bbishop = [[x[0], x[1]], pieces[1]]
    if pieces == bbishop1:
        blacktaken.remove(getLocation(bbishop1))
        blacktaken.append([x[0], x[1]])
        taken.remove(getLocation(bbishop1))
        taken.append([x[0], x[1]])
        bbishop1 = [[x[0], x[1]], pieces[1]]
    if pieces == bking:
        blacktaken.remove(getLocation(bking))
        blacktaken.append([x[0], x[1]])
        taken.remove(getLocation(bking))
        taken.append([x[0], x[1]])
        bking = [[x[0], x[1]], pieces[1]]
    if pieces == bqueen:
        blacktaken.remove(getLocation(bqueen))
        blacktaken.append([x[0], x[1]])
        taken.remove(getLocation(bking))
        taken.append([x[0], x[1]])
        bqueen = [[x[0], x[1]], pieces[1]]


def move_piece(pieces):
    temp = moves_available(pieces)
    if pieces[1] == "king":
        if pieces in white:
            tempp = kingthreat(wking)
            for i in tempp:
                if i in temp:
                    temp.remove(i)
            if len(temp) == 1 and pieces[0] in tempp:
                print("checkmate, black wins")
            if len(temp) == 1 and pieces[0] not in tempp:
                print("stalemate, tie")
        if pieces in black:
            tempp = kingthreat(bking)
            for i in tempp:
                if i in temp:
                    temp.remove(i)
            if len(temp) == 1 and pieces[0] in tempp:
                print("checkmate, white wins")
            if len(temp) == 1 and pieces[0] not in tempp:
                print("stalemate, tie")
    print("these are your options to move")
    print(temp)
    x = int(input("enter the option number to move "))
    if (temp[x]) in blacktaken or ((temp[x]) in whitetaken) and x != 0:
        print((temp[x]))
        death(temp[x])
    if x != 0:
        print(temp[x])
        setLocation(temp[x], pieces)
    else:
        print("no move selected")


def pawnthreat(pieces):
    choice_move = []
    if pieces in white:
        choice_move.append([pieces[0][0] + 1, pieces[0][1] + 1])
        choice_move.append([pieces[0][0] + 1, pieces[0][1] + 1])
    if pieces in black:
        choice_move.append([pieces[0][0] + 1, pieces[0][1] - 1])
        choice_move.append([pieces[0][0] - 1, pieces[0][1] - 1])
    return choice_move


def moves_available(pieces):
    white = [wcastle, wknight, wbishop, wqueenn, wking, wbishop1, wknight2, wcastle2,
             wpawn, wpawn1, wpawn2, wpawn3, wpawn4, wpawn5, wpawn6, wpawn7]
    black = [bcastle, bknight, bbishop, bqueen, bking, bbishop1, bknight2, bcastle2,
             bpawn, bpawn1, bpawn2, bpawn3, bpawn4, bpawn5, bpawn6, bpawn7]
    choice_move = [["nothing"]]
    if pieces[1] == "pawn":
        if [pieces[0][0] + 1, pieces[0][1] + 1] in blacktaken:
            choice_move.append([pieces[0][0] + 1, pieces[0][1] + 1])
        if [pieces[0][0] - 1, pieces[0][1] + 1] in blacktaken:
            choice_move.append([pieces[0][0] - 1, pieces[0][1] + 1])
        if [pieces[0][0], pieces[0][1] + 1] not in taken:
            choice_move.append([pieces[0][0], pieces[0][1] + 1])
            if pieces[0][1] == 1 and ([pieces[0][0], pieces[0][1] + 2]) not in taken:
                choice_move.append([pieces[0][0], pieces[0][1] + 2])
    if pieces[1] == "bpawn":
        if [pieces[0][0] + 1, pieces[0][1] - 1] in whitetaken:
            choice_move.append([pieces[0][0] + 1, pieces[0][1] - 1])
        if [pieces[0][0] - 1, pieces[0][1] - 1] in whitetaken:
            choice_move.append([pieces[0][0] - 1, pieces[0][1] - 1])
        if [pieces[0][0], pieces[0][1] - 1] not in taken:
            choice_move.append([pieces[0][0], pieces[0][1] - 1])
            if pieces[0][1] == 6 and ([pieces[0][0], pieces[0][1] - 2]) not in taken:
                choice_move.append([pieces[0][0], pieces[0][1] - 2])
    if pieces[1] == "king":

        if pieces in white:
            if ([getLocation(pieces)[0] + 1, getLocation(pieces)[1]]) in blacktaken or (
            [getLocation(pieces)[0] + 1, getLocation(pieces)[1]]) not in taken:
                choice_move.append([getLocation(pieces)[0] + 1, getLocation(pieces)[1]])
            if ([getLocation(pieces)[0] - 1, getLocation(pieces)[1]]) in blacktaken or (
            [getLocation(pieces)[0] - 1, getLocation(pieces)[1]]) not in taken:
                choice_move.append([getLocation(pieces)[0] - 1, getLocation(pieces)[1]])
            if ([getLocation(pieces)[0] - 1, getLocation(pieces)[1] - 1]) in blacktaken or (
            [getLocation(pieces)[0] - 1, getLocation(pieces)[1] - 1]) not in taken:
                choice_move.append([getLocation(pieces)[0] - 1, getLocation(pieces)[1] - 1])
            if ([getLocation(pieces)[0], getLocation(pieces)[1] - 1]) in blacktaken or (
            [getLocation(pieces)[0], getLocation(pieces)[1] - 1]) not in taken:
                choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] - 1])
            if ([getLocation(pieces)[0] + 1, getLocation(pieces)[1] - 1]) in blacktaken or (
            [getLocation(pieces)[0] + 1, getLocation(pieces)[1] - 1]) not in taken:
                choice_move.append([getLocation(pieces)[0] + 1, getLocation(pieces)[1] - 1])
            if ([getLocation(pieces)[0] + 1, getLocation(pieces)[1] + 1]) in blacktaken or (
            [getLocation(pieces)[0] + 1, getLocation(pieces)[1] + 1]) not in taken:
                choice_move.append([getLocation(pieces)[0] + 1, getLocation(pieces)[1] + 1])
            if ([getLocation(pieces)[0], getLocation(pieces)[1] + 1]) in blacktaken or (
            [getLocation(pieces)[0], getLocation(pieces)[1] + 1]) not in taken:
                choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] + 1])
            if ([getLocation(pieces)[0] - 1, getLocation(pieces)[1] + 1]) in blacktaken or (
            [getLocation(pieces)[0] - 1, getLocation(pieces)[1] + 1]) not in taken:
                choice_move.append([getLocation(pieces)[0] - 1, getLocation(pieces)[1] + 1])
        if pieces in black:
            if ([getLocation(pieces)[0] + 1, getLocation(pieces)[1]]) in whitetaken or (
                    [getLocation(pieces)[0] + 1, getLocation(pieces)[1]]) not in taken:
                choice_move.append([getLocation(pieces)[0] + 1, getLocation(pieces)[1]])
            if ([getLocation(pieces)[0] - 1, getLocation(pieces)[1]]) in whitetaken or (
                    [getLocation(pieces)[0] - 1, getLocation(pieces)[1]]) not in taken:
                choice_move.append([getLocation(pieces)[0] - 1, getLocation(pieces)[1]])
            if ([getLocation(pieces)[0] - 1, getLocation(pieces)[1] - 1]) in whitetaken or (
                    [getLocation(pieces)[0] - 1, getLocation(pieces)[1] - 1]) not in taken:
                choice_move.append([getLocation(pieces)[0] - 1, getLocation(pieces)[1] - 1])
            if ([getLocation(pieces)[0], getLocation(pieces)[1] - 1]) in whitetaken or (
                    [getLocation(pieces)[0], getLocation(pieces)[1] - 1]) not in taken:
                choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] - 1])
            if ([getLocation(pieces)[0] + 1, getLocation(pieces)[1] - 1]) in whitetaken or (
                    [getLocation(pieces)[0] + 1, getLocation(pieces)[1] - 1]) not in taken:
                choice_move.append([getLocation(pieces)[0] + 1, getLocation(pieces)[1] - 1])
            if ([getLocation(pieces)[0] + 1, getLocation(pieces)[1] + 1]) in whitetaken or (
                    [getLocation(pieces)[0] + 1, getLocation(pieces)[1] + 1]) not in taken:
                choice_move.append([getLocation(pieces)[0] + 1, getLocation(pieces)[1] + 1])
            if ([getLocation(pieces)[0], getLocation(pieces)[1] + 1]) in whitetaken or (
                    [getLocation(pieces)[0], getLocation(pieces)[1] + 1]) not in taken:
                choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] + 1])
            if ([getLocation(pieces)[0] - 1, getLocation(pieces)[1] + 1]) in whitetaken or (
                    [getLocation(pieces)[0] - 1, getLocation(pieces)[1] + 1]) not in taken:
                choice_move.append([getLocation(pieces)[0] - 1, getLocation(pieces)[1] + 1])
    if pieces[1] == "knight":
        if pieces in white:
            if ([getLocation(pieces)[0] + 1, getLocation(pieces)[1] + 2]) in blacktaken or (
                    [getLocation(pieces)[0] + 1, getLocation(pieces)[1] + 2]) not in taken:
                choice_move.append([getLocation(pieces)[0] + 1, getLocation(pieces)[1] + 2])
            if ([getLocation(pieces)[0] + 1, getLocation(pieces)[1] - 2]) in blacktaken or (
                    [getLocation(pieces)[0] + 1, getLocation(pieces)[1] - 2]) not in taken:
                choice_move.append([getLocation(pieces)[0] + 1, getLocation(pieces)[1] - 2])
            if ([getLocation(pieces)[0] - 1, getLocation(pieces)[1] + 2]) in blacktaken or (
                    [getLocation(pieces)[0] - 1, getLocation(pieces)[1] + 2]) not in taken:
                choice_move.append([getLocation(pieces)[0] - 1, getLocation(pieces)[1] + 2])
            if ([getLocation(pieces)[0] - 1, getLocation(pieces)[1] - 2]) in blacktaken or (
                    [getLocation(pieces)[0] - 1, getLocation(pieces)[1] - 2]) not in taken:
                choice_move.append([getLocation(pieces)[0] - 1, getLocation(pieces)[1] - 2])
            if ([getLocation(pieces)[0] + 2, getLocation(pieces)[1] + 1]) in blacktaken or (
                    [getLocation(pieces)[0] + 2, getLocation(pieces)[1] + 1]) not in taken:
                choice_move.append([getLocation(pieces)[0] + 2, getLocation(pieces)[1] + 1])
            if ([getLocation(pieces)[0] + 2, getLocation(pieces)[1] - 1]) in blacktaken or (
                    [getLocation(pieces)[0] + 2, getLocation(pieces)[1] - 1]) not in taken:
                choice_move.append([getLocation(pieces)[0] + 2, getLocation(pieces)[1] - 1])
            if ([getLocation(pieces)[0] - 2, getLocation(pieces)[1] + 1]) in blacktaken or (
                    [getLocation(pieces)[0] - 2, getLocation(pieces)[1] + 1]) not in taken:
                choice_move.append([getLocation(pieces)[0] - 2, getLocation(pieces)[1] + 1])
            if ([getLocation(pieces)[0] - 2, getLocation(pieces)[1] - 1]) in blacktaken or (
                    [getLocation(pieces)[0] - 2, getLocation(pieces)[1] - 1]) not in taken:
                choice_move.append([getLocation(pieces)[0] - 2, getLocation(pieces)[1] - 1])
        if pieces in black:
            if ([getLocation(pieces)[0] + 1, getLocation(pieces)[1] + 2]) in whitetaken or (
                    [getLocation(pieces)[0] + 1, getLocation(pieces)[1] + 2]) not in taken:
                choice_move.append([getLocation(pieces)[0] + 1, getLocation(pieces)[1] + 2])
            if ([getLocation(pieces)[0] + 1, getLocation(pieces)[1] - 2]) in whitetaken or (
                    [getLocation(pieces)[0] + 1, getLocation(pieces)[1] - 2]) not in taken:
                choice_move.append([getLocation(pieces)[0] + 1, getLocation(pieces)[1] - 2])
            if ([getLocation(pieces)[0] - 1, getLocation(pieces)[1] + 2]) in whitetaken or (
                    [getLocation(pieces)[0] - 1, getLocation(pieces)[1] + 2]) not in taken:
                choice_move.append([getLocation(pieces)[0] - 1, getLocation(pieces)[1] + 2])
            if ([getLocation(pieces)[0] - 1, getLocation(pieces)[1] - 2]) in whitetaken or (
                    [getLocation(pieces)[0] - 1, getLocation(pieces)[1] - 2]) not in taken:
                choice_move.append([getLocation(pieces)[0] - 1, getLocation(pieces)[1] - 2])
            if ([getLocation(pieces)[0] + 2, getLocation(pieces)[1] + 1]) in whitetaken or (
                    [getLocation(pieces)[0] + 2, getLocation(pieces)[1] + 1]) not in taken:
                choice_move.append([getLocation(pieces)[0] + 2, getLocation(pieces)[1] + 1])
            if ([getLocation(pieces)[0] + 2, getLocation(pieces)[1] - 1]) in whitetaken or (
                    [getLocation(pieces)[0] + 2, getLocation(pieces)[1] - 1]) not in taken:
                choice_move.append([getLocation(pieces)[0] + 2, getLocation(pieces)[1] - 1])
            if ([getLocation(pieces)[0] - 2, getLocation(pieces)[1] + 1]) in whitetaken or (
                    [getLocation(pieces)[0] - 2, getLocation(pieces)[1] + 1]) not in taken:
                choice_move.append([getLocation(pieces)[0] - 2, getLocation(pieces)[1] + 1])
            if ([getLocation(pieces)[0] - 2, getLocation(pieces)[1] - 1]) in whitetaken or (
                    [getLocation(pieces)[0] - 2, getLocation(pieces)[1] - 1]) not in taken:
                choice_move.append([getLocation(pieces)[0] - 2, getLocation(pieces)[1] - 1])
    if pieces[1] == "castle":
        if pieces in white:
            print("test")

            for a in range(1, 9):
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1]]) == bking[0]:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1]])
                    choice_move.append([getLocation(pieces)[0] + a + 1, getLocation(pieces)[1]])
                    break
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1]]) in blacktaken:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1]])
                    break
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1]]) in whitetaken:
                    break
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1]]) not in taken:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1]])
                    print(whitetaken)
            for a in range(1, 9):
                if ([getLocation(pieces)[0], getLocation(pieces)[1] + a]) == bking[0]:
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] + a])
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] + a + 1])
                    break
                if ([getLocation(pieces)[0], getLocation(pieces)[1] + a]) in blacktaken:
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] + a])
                    break
                if ([getLocation(pieces)[0], getLocation(pieces)[1] + a]) in whitetaken:
                    break
                if ([getLocation(pieces)[0], getLocation(pieces)[1] + a]) not in taken:
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] + a])
            for a in range(1, 9):
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1]]) == bking[0]:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1]])
                    choice_move.append([getLocation(pieces)[0] - (a + 1), getLocation(pieces)[1]])
                    break
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1]]) in blacktaken:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1]])
                    break
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1]]) in whitetaken:
                    break
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1]]) not in taken:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1]])
            for a in range(1, 9):
                if ([getLocation(pieces)[0], getLocation(pieces)[1] - a]) == bking[0]:
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] - a])
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] - (a + 1)])
                    break
                if ([getLocation(pieces)[0], getLocation(pieces)[1] - a]) in blacktaken:
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] - a])
                    break
                if ([getLocation(pieces)[0], getLocation(pieces)[1] - a]) in whitetaken:
                    break
                if ([getLocation(pieces)[0], getLocation(pieces)[1] - a]) not in taken:
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] - a])

        if pieces in black:
            for a in range(1, 9):
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1]]) == wking[0]:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1]])
                    choice_move.append([getLocation(pieces)[0] + (a + 1), getLocation(pieces)[1]])
                    break
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1]]) in whitetaken:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1]])
                    break
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1]]) in blacktaken:
                    break
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1]]) not in taken:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1]])
            for a in range(1, 9):
                if ([getLocation(pieces)[0], getLocation(pieces)[1] + a]) == wking[0]:
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] + a])
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] + (a + 1)])
                    break
                if ([getLocation(pieces)[0], getLocation(pieces)[1] + a]) in whitetaken:
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] + a])
                    break
                if ([getLocation(pieces)[0], getLocation(pieces)[1] + a]) in blacktaken:
                    break
                if ([getLocation(pieces)[0], getLocation(pieces)[1] + a]) not in taken:
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] + a])
            for a in range(1, 9):
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1]]) == wking[0]:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1]])
                    choice_move.append([getLocation(pieces)[0] - (a + 1), getLocation(pieces)[1]])
                    break
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1]]) in whitetaken:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1]])
                    break
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1]]) in blacktaken:
                    break
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1]]) not in taken:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1]])
            for a in range(1, 9):
                if ([getLocation(pieces)[0], getLocation(pieces)[1] - a]) == wking[0]:
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] - a])
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] - (a + 1)])

                    break
                if ([getLocation(pieces)[0], getLocation(pieces)[1] - a]) in whitetaken:
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] - a])
                    break
                if ([getLocation(pieces)[0], getLocation(pieces)[1] - a]) in blacktaken:
                    break
                if ([getLocation(pieces)[0], getLocation(pieces)[1] - a]) not in taken:
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] - a])
    if pieces[1] == "bishop":
        if pieces in white:
            for a in range(1, 8):
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] + a]) == bking[0]:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1] + a])
                    choice_move.append([getLocation(pieces)[0] + a + 1, getLocation(pieces)[1] + a + 1])
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] + a]) in blacktaken:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1] + a])
                    break
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] + a]) in whitetaken:
                    break
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] + a]) not in taken:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1] + a])
            for a in range(1, 8):
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] + a]) == bking[0]:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1] + a])
                    choice_move.append([getLocation(pieces)[0] - (a + 1), getLocation(pieces)[1] + (a + 1)])
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] + a]) in blacktaken:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1] + a])
                    break
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] + a]) in whitetaken:
                    break
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] + a]) not in taken:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1] + a])
            for a in range(1, 8):
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] - a]) == bking[0]:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1] - a])
                    choice_move.append([getLocation(pieces)[0] + (a + 1), getLocation(pieces)[1] - (a + 1)])
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] - a]) in blacktaken:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1] - a])
                    break
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] - a]) in whitetaken:
                    break
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] - a]) not in taken:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1] - a])
            for a in range(1, 8):
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] - a]) == bking[0]:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1] - a])
                    choice_move.append([getLocation(pieces)[0] - (a + 1), getLocation(pieces)[1] - (a + 1)])
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] - a]) in blacktaken:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1] - a])
                    break
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] - a]) in whitetaken:
                    break
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] - a]) not in taken:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1] - a])
        if pieces in black:
            for a in range(1, 8):
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] + a]) == wking[0]:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1] + a])
                    choice_move.append([getLocation(pieces)[0] + a + 1, getLocation(pieces)[1] + a + 1])
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] + a]) in whitetaken:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1] + a])
                    break
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] + a]) in blacktaken:
                    break
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] + a]) not in taken:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1] + a])
            for a in range(1, 8):
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] + a]) == wking[0]:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1] + a])
                    choice_move.append([getLocation(pieces)[0] - (a + 1), getLocation(pieces)[1] + (a + 1)])
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] + a]) in whitetaken:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1] + a])
                    break
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] + a]) in blacktaken:
                    break
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] + a]) not in taken:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1] + a])
            for a in range(1, 8):
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] - a]) == wking[0]:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1] - a])
                    choice_move.append([getLocation(pieces)[0] + (a + 1), getLocation(pieces)[1] - (a + 1)])
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] - a]) in whitetaken:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1] - a])
                    break
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] - a]) in blacktaken:
                    break
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] - a]) not in taken:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1] - a])
            for a in range(1, 8):
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] - a]) == wking[0]:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1] - a])
                    choice_move.append([getLocation(pieces)[0] - (a + 1), getLocation(pieces)[1] - (a + 1)])
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] - a]) in whitetaken:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1] - a])
                    break
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] - a]) in blacktaken:
                    break
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] - a]) not in taken:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1] - a])
    if pieces[1] == "queen":
        if pieces in white:
            for a in range(1, 8):
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] + a]) == bking[0]:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1] + a])
                    choice_move.append([getLocation(pieces)[0] + a + 1, getLocation(pieces)[1] + a + 1])
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] + a]) in blacktaken:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1] + a])
                    break
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] + a]) in whitetaken:
                    break
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] + a]) not in taken:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1] + a])
            for a in range(1, 8):
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] + a]) == bking[0]:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1] + a])
                    choice_move.append([getLocation(pieces)[0] - (a + 1), getLocation(pieces)[1] + (a + 1)])
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] + a]) in blacktaken:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1] + a])
                    break
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] + a]) in whitetaken:
                    break
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] + a]) not in taken:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1] + a])
            for a in range(1, 8):
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] - a]) == bking[0]:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1] - a])
                    choice_move.append([getLocation(pieces)[0] + (a + 1), getLocation(pieces)[1] - (a + 1)])
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] - a]) in blacktaken:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1] - a])
                    break
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] - a]) in whitetaken:
                    break
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] - a]) not in taken:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1] - a])
            for a in range(1, 8):
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] - a]) == bking[0]:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1] - a])
                    choice_move.append([getLocation(pieces)[0] - (a + 1), getLocation(pieces)[1] - (a + 1)])
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] - a]) in blacktaken:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1] - a])
                    break
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] - a]) in whitetaken:
                    break
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] - a]) not in taken:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1] - a])  ### #
        if pieces in black:
            for a in range(1, 8):
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] + a]) == wking[0]:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1] + a])
                    choice_move.append([getLocation(pieces)[0] + a + 1, getLocation(pieces)[1] + a + 1])
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] + a]) in whitetaken:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1] + a])
                    break
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] + a]) in blacktaken:
                    break
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] + a]) not in taken:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1] + a])
            for a in range(1, 8):
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] + a]) == wking[0]:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1] + a])
                    choice_move.append([getLocation(pieces)[0] - (a + 1), getLocation(pieces)[1] + (a + 1)])
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] + a]) in whitetaken:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1] + a])
                    break
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] + a]) in blacktaken:
                    break
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] + a]) not in taken:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1] + a])
            for a in range(1, 8):
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] - a]) == wking[0]:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1] - a])
                    choice_move.append([getLocation(pieces)[0] + (a + 1), getLocation(pieces)[1] - (a + 1)])
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] - a]) in whitetaken:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1] - a])
                    break
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] - a]) in blacktaken:
                    break
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1] - a]) not in taken:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1] - a])
            for a in range(1, 8):
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] - a]) == wking[0]:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1] - a])
                    choice_move.append([getLocation(pieces)[0] - (a + 1), getLocation(pieces)[1] - (a + 1)])
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] - a]) in whitetaken:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1] - a])
                    break
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] - a]) in blacktaken:
                    break
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1] - a]) not in taken:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1] - a])
        if pieces in white:
            for a in range(1, 9):
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1]]) == bking[0]:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1]])
                    choice_move.append([getLocation(pieces)[0] + a + 1, getLocation(pieces)[1]])
                    break
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1]]) in blacktaken:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1]])
                    break
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1]]) in whitetaken:
                    break
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1]]) not in taken:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1]])
            for a in range(1, 9):
                if ([getLocation(pieces)[0], getLocation(pieces)[1] + a]) == bking[0]:
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] + a])
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] + a + 1])
                    break
                if ([getLocation(pieces)[0], getLocation(pieces)[1] + a]) in blacktaken:
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] + a])
                    break
                if ([getLocation(pieces)[0], getLocation(pieces)[1] + a]) in whitetaken:
                    break
                if ([getLocation(pieces)[0], getLocation(pieces)[1] + a]) not in taken:
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] + a])
            for a in range(1, 9):
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1]]) == bking[0]:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1]])
                    choice_move.append([getLocation(pieces)[0] - (a + 1), getLocation(pieces)[1]])
                    break
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1]]) in blacktaken:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1]])
                    break
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1]]) in whitetaken:
                    break
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1]]) not in taken:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1]])
            for a in range(1, 9):
                if ([getLocation(pieces)[0], getLocation(pieces)[1] - a]) == bking[0]:
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] - a])
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] - (a + 1)])
                    break
                if ([getLocation(pieces)[0], getLocation(pieces)[1] - a]) in blacktaken:
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] - a])
                    break
                if ([getLocation(pieces)[0], getLocation(pieces)[1] - a]) in whitetaken:
                    break
                if ([getLocation(pieces)[0], getLocation(pieces)[1] - a]) not in taken:
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] - a])
        if pieces in black:
            for a in range(1, 9):
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1]]) == wking[0]:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1]])
                    choice_move.append([getLocation(pieces)[0] + (a + 1), getLocation(pieces)[1]])
                    break
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1]]) in whitetaken:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1]])
                    break
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1]]) in blacktaken:
                    break
                if ([getLocation(pieces)[0] + a, getLocation(pieces)[1]]) not in taken:
                    choice_move.append([getLocation(pieces)[0] + a, getLocation(pieces)[1]])
            for a in range(1, 9):
                if ([getLocation(pieces)[0], getLocation(pieces)[1] + a]) == wking[0]:
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] + a])
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] + (a + 1)])
                    break
                if ([getLocation(pieces)[0], getLocation(pieces)[1] + a]) in whitetaken:
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] + a])
                    break
                if ([getLocation(pieces)[0], getLocation(pieces)[1] + a]) in blacktaken:
                    break
                if ([getLocation(pieces)[0], getLocation(pieces)[1] + a]) not in taken:
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] + a])
            for a in range(1, 9):
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1]]) == wking[0]:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1]])
                    choice_move.append([getLocation(pieces)[0] - (a + 1), getLocation(pieces)[1]])
                    break
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1]]) in whitetaken:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1]])
                    break
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1]]) in blacktaken:
                    break
                if ([getLocation(pieces)[0] - a, getLocation(pieces)[1]]) not in taken:
                    choice_move.append([getLocation(pieces)[0] - a, getLocation(pieces)[1]])
            for a in range(1, 9):
                if ([getLocation(pieces)[0], getLocation(pieces)[1] - a]) == wking[0]:
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] - a])
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] - (a + 1)])

                    break
                if ([getLocation(pieces)[0], getLocation(pieces)[1] - a]) in whitetaken:
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] - a])
                    break
                if ([getLocation(pieces)[0], getLocation(pieces)[1] - a]) in blacktaken:
                    break
                if ([getLocation(pieces)[0], getLocation(pieces)[1] - a]) not in taken:
                    choice_move.append([getLocation(pieces)[0], getLocation(pieces)[1] - a])
    return (choice_move)


def kingthreat(king):
    bking_threat = []
    wking_threat = []
    for x in black:
        if x[1] != "bpawn" or x[1] != "king":
            for j in (moves_available(x)):
                if j != ['nothing']:
                    wking_threat.append(j)
        if x[1] == "pawn":
            for j in pawnthreat(x):
                wking_threat.append(j)

    for x in white:
        if x[1] != "pawn" or x[1] != "king":
            for j in (moves_available(x)):
                if j != ['nothing']:
                    bking_threat.append(j)
        if x[1] == "pawn":
            for j in pawnthreat(x):
                bking_threat.append(j)
    if king in black:
        return bking_threat
    if king in white:
        return wking_threat
colorx = 0
colory = 1
def visual():
    global colorx
    global colory

    wpawn.append("Wpawn")
    wpawn1.append("Wpawn1")
    wpawn2.append("Wpawn2")
    wpawn3.append("Wpawn3")
    wpawn4.append("Wpawn4")
    wpawn5.append("Wpawn5")
    wpawn6.append("Wpawn6")
    wpawn7.append("Wpawn7")
    wcastle.append("Wcastle")
    wknight.append("Wknight")
    wbishop.append("Wbishop")
    wking.append("Wking")
    wqueenn.append("Wqueen")
    wbishop1.append("Wbishop1")
    wknight2.append("Wknight2")
    wcastle2.append("Wcastle2")
    bpawn.append("Bpawn")
    bpawn1.append("Bpawn1")
    bpawn2.append("Bpawn2")
    bpawn3.append("Bpawn3")
    bpawn4.append("Bpawn4")
    bpawn5.append("Bpawn5")
    bpawn6.append("Bpawn6")
    bpawn7.append("Bpawn7")
    bcastle.append("Bcastle")
    bknight.append("Bknight")
    bbishop.append("Bbishop")
    bking.append("Bking")
    bqueen.append("Bqueen")
    bbishop1.append("Bbishop1")
    bknight2.append("Bknight2")
    bcastle2.append("Bcastle2")
    white = [wcastle, wknight, wbishop, wqueenn, wking, wbishop1, wknight2, wcastle2,
             wpawn, wpawn1, wpawn2, wpawn3, wpawn4, wpawn5, wpawn6, wpawn7]
    black = [bcastle, bknight, bbishop, bqueen, bking, bbishop1, bknight2, bcastle2,
             bpawn, bpawn1, bpawn2, bpawn3, bpawn4, bpawn5, bpawn6, bpawn7]
    board = []
    for i in range(0,8):
        for b in range(0,8):
                board.append([b,i])
    for i in white:
        if i[0] in board:
            x = board.index(i[0])
            board[x] = i[2]
    for i in black:
        if i[0] in board:
            x = board.index(i[0])
            board[x] = i[2]

    a = 0
    while a < len(board):
        size = len("| [7, 2] |")

        one =  str(board[0+a]) +" | "
        while len(one) < size + 1:

            one = " " + one
        two = str(board[1+a]) +" | "
        while len(two) < size + 1:

            two =   " " + two

        three = str(board[2+a]) +" | "
        while len(three) < size + 1:
            three = " " + three
        four = str(board[3+a]) +" | "
        while len(four) < size + 1:
            four = " " + four
        five = str(board[4+a]) +" | "
        while len(five) < size + 1:
            five = " " + five
        six = str(board[5+a]) +" | "
        while len(six) < size + 1:
            six = " " + six
        seven= str(board[6+a]) +" | "
        while len(seven) < size + 1:
            seven = " " + seven
        eight= str(board[7+a]) +" | "
        while len(eight) < size + 1:
            eight = " " + eight
        if colorx % 2 == 1:
            three += Back.BLACK + Fore.WHITE
            five += Back.BLACK + Fore.WHITE
            two += Fore.BLACK + Back.WHITE
            four += Fore.BLACK + Back.WHITE
            six += Fore.BLACK + Back.WHITE
            eight += Back.BLACK + Fore.WHITE
            one += Back.BLACK + Fore.WHITE
            seven += Back.BLACK + Fore.WHITE
        if colorx % 2 == 0:
            eight += Fore.BLACK + Back.WHITE
            one += Fore.BLACK + Back.WHITE
            two += Back.BLACK + Fore.WHITE
            three += Fore.BLACK + Back.WHITE
            four += Back.BLACK + Fore.WHITE
            five += Fore.BLACK + Back.WHITE
            six += Back.BLACK + Fore.WHITE
            seven += Fore.BLACK + Back.WHITE
        colorx +=1
        #print(colorx)
        print(one + two + three + four + five + six + seven + eight)
        a += 8


visual()
def interface():
    global count
    if count %2 == 0:
        print("white move")
    else:
        print("black move")

    user = input("enter the piece you want to move as seen on the board: ")
    # user = "wpawn"
    if user == "Bpawn":
        move_piece(bpawn)
    if user == "Bpawn1":
        move_piece(bpawn1)
    if user == "Bpawn2":
        move_piece(bpawn2)
    if user == "Bpawn3":
        move_piece(bpawn3)
    if user == "Bpawn4":
        move_piece(bpawn4)
    if user == "Bpawn5":
        move_piece(bpawn5)
    if user == "Bpawn6":
        move_piece(bpawn6)
    if user == "Bpawn7":
        move_piece(bpawn7)
    if user == "Bcastle":
        move_piece(bcastle)
    if user == "Bcastle2":
        move_piece(bcastle2)
    if user == "Bknight":
        move_piece(bknight)
    if user == "Bknight2":
        move_piece(bknight2)
    if user == "Bbishop":
        move_piece(bbishop)
    if user == "Bbishop1":
        move_piece(bbishop1)
    if user == "Bking":
        move_piece(bking)
    if user == "Bqueen":
        move_piece(bqueen)
    if user == "Bpawn":
        move_piece(wpawn)
    if user == "Wpawn1":
        move_piece(wpawn1)
    if user == "Wpawn2":
        move_piece(wpawn2)
    if user == "Wpawn3":
        move_piece(wpawn3)
    if user == "Wpawn4":
        move_piece(wpawn4)
    if user == "Wpawn5":
        move_piece(wpawn5)
    if user == "Wpawn6":
        move_piece(wpawn6)
    if user == "Wpawn7":
        move_piece(wpawn7)
    if user == "Wcastle":
        move_piece(wcastle)
    if user == "Wcastle2":
        move_piece(wcastle2)
    if user == "Wknight":
        move_piece(wknight)
    if user == "Wknight2":
        move_piece(wknight2)
    if user == "Wbishop":
        move_piece(wbishop)
    if user == "Wbishop1":
        move_piece(wbishop1)
    if user == "Wking":
        move_piece(wking)
    if user == "Wqueen":
        move_piece(wqueenn)
    if user == "sWhow":
        print(white)
        print(black)
    if user == "taken":
        print(taken)
    if user != "n":
        count +=1
        visual()
        print(Back.RESET + Fore.RESET)
        interface()



print(interface())
