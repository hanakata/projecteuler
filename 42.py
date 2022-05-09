
# 三角数チェック
def triangularNumberCheck(num):
    for i in range(1, num):
        tnum = i * (i + 1) / 2
        if tnum > num:
            return False
        elif tnum == num:
            return True
    return True

# 各文字列のアルファベットを全て加算
def wordToNumbers(word):
    n = 0
    char_list = list(word)
    for c in char_list:
        n += ord(c) - 64
    return n

if __name__ == '__main__':
    ans = 0
    with open('p042_words.txt') as f:
        word = f.read()
        word_list = word.replace('"', '').split(',')
    for word in word_list:
        if triangularNumberCheck(wordToNumbers(word)):
            ans += 1
    print(f'ans:{ans}')
