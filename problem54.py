
# T～Aの置き換え
def specialNumChange(list):
    changeList = []
    for i in list:
        if 'T' in i:
            i = i.replace('T', '10')
        elif 'J' in i:
            i = i.replace('J', '11')
        if 'Q' in i:
            i = i.replace('Q', '12')
        if 'K' in i:
            i = i.replace('K', '13')
        if 'A' in i:
            i = i.replace('A', '14')
        changeList.append(i)
    return changeList
# ロイヤルフラッシュかのチェック
def checkRoyalFlush(list):
    numberList = ["10", "11", "12", "13", "14"]
    suit = ""
    for i in list:
        if suit == "":
            suit = i[-1]
        elif suit != i[-1]:
            return False
        if len(i) < 3:
            return False
        else:
            checkNum = i[0] + i[1]
            if checkNum not in numberList:
                return False
    return True

# ストレートフラッシュかのチェック
def checkStraightFlush(list):
    suit = ""
    numListTmp = []
    for i in list:
        if suit == "":
            suit = i[-1]
        elif suit != i[-1]:
            return False
        numStr = i.replace(i[-1], "")
        numListTmp.append(int(numStr))
    numList = sorted(numListTmp)
    check = 0
    for i in numList:
        if check == 0:
            check = i
        elif check + 1 != i:
            return False
        check = check + 1
    return True
# フラッシュかのチェック
def checkFlush(list):
    suit = ""
    for i in list:
        if suit == "":
            suit = i[-1]
        elif suit != i[-1]:
            return False
    return True
# ストレートかのチェック
def checkStraight(list):
    check = ""
    count = 1
    for i in list:
        numStr = i.replace(i[-1], "")
        if check == "":
            check = numStr
        elif check == numStr:
            count = count + 1
    if count == 5:
        return True
    else:
        return False

# フォーカードかのチェック
def checkFourCards(list):
    check = ""
    count = 1
    for i in list:
        numStr = i.replace(i[-1], "")
        if check == "":
            check = numStr
        elif check == numStr:
            count = count + 1
    if count == 4:
        return True
    else:
        return False

# フルハウスかのチェック
def checkFullHouse(list):
    numList = []
    if checkThreeCards(list):
        for i in list:
            numStr = i.replace(i[-1], "")
            numList.append(numStr)
        for i in numList:
            if numList.count(i) == 3:
                numList.remove(i)
                numList.remove(i)
                numList.remove(i)
        if numList[0] == numList[1]:
            return True
        else:
            return False
    else:
        return False
# スリーカードかのチェック
def checkThreeCards(list):
    check = ""
    count = 1
    for i in list:
        numStr = i.replace(i[-1], "")
        if check == "":
            check = numStr
        elif check == numStr:
            count = count + 1
    if count == 3:
        return True
    else:
        return False

# ツーペアかのチェック
def checkTwoPair(list):
    numList = []
    count = 0
    for i in list:
        numStr = i.replace(i[-1], "")
        numList.append(numStr)

    for n in range(0, 5):
        numCount = 0
        for m in range(0, 5):
            if n != m:
                if numList[n] == numList[m]:
                    numCount = numCount + 1
        if numCount == 1:
            count = count + 1
    if count == 4:
        return True
    else:
        return False

# ワンペアかのチェック
def checkOnePair(list):
    check = ""
    count = 0
    for i in list:
        numStr = i.replace(i[-1], "")
        if check == "":
            check = numStr
        elif check == numStr:
            count = count + 1
    if count == 2:
        return True
    else:
        return False

def checkRole(list):
    if checkRoyalFlush(list):
        return 1
    if checkStraightFlush(list):
        return 2
    if checkFourCards(list):
        return 3
    if checkFullHouse(list):
        return 4
    if checkFlush(list):
        return 5
    if checkStraight(list):
        return 6
    if checkThreeCards(list):
        return 7
    if checkTwoPair(list):
        return 8
    if checkOnePair(list):
        return 9
    return 10
if __name__ == '__main__':
    with open('p054_poker.txt') as f:
        for line in f:
            player1Rank = 0
            player2Rank = 0
            player1CardList = []
            player2CardList = []
            cardList = line.replace("\n", "").split(" ")
            for i in range(0, 5):
                player1CardList.append(cardList[i])
            for j in range(5, 10):
                player2CardList.append(cardList[j])
            player1CardList = specialNumChange(player1CardList)
            player2CardList = specialNumChange(player2CardList)
            player1Rank = checkRole(player1CardList)
            player2Rank = checkRole(player2CardList)
            if player1Rank == player2Rank:
                print(player1CardList)
                print(player2CardList)
            elif player1Rank < player2Rank:
                print("player1 win")
            else:
                print("player2 win")
