limit = 1000
r = 0
num_dict = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
    "20": "twenty",
    "30": "thirty",
    "40": "forty",
    "50": "fifty",
    "60": "sixty",
    "70": "seventy",
    "80": "eighty",
    "90": "ninety",
    "100": "hundred",
    "1000": "thousand",
}
for i in range(1, limit + 1):
    s_num = str(i)
    if 20 < i:
        if len(s_num) == 2:
            two_digits = list(s_num)
            if two_digits[1] != "0":
                ten_digits = two_digits[0] + "0"
                one_digits = two_digits[1]
                word = num_dict[ten_digits] + " " + num_dict[one_digits]
            else:
                word = num_dict[s_num]
        elif len(s_num) == 3:
            three_digits = list(s_num)
            if three_digits[1] == "0" and three_digits[2] == "0":
                hundred_digits = three_digits[0]
                word = num_dict[hundred_digits] + " " + num_dict["100"]
            elif three_digits[2] == "0":
                ten_digits = three_digits[1] + "0"
                word = num_dict[hundred_digits] + " " + \
                    num_dict["100"] + " and " + num_dict[ten_digits]
            else:
                two_digits = three_digits[1] + three_digits[2]
                if 20 < int(two_digits):
                    if three_digits[2] != "0":
                        ten_digits = three_digits[1] + "0"
                        one_digits = three_digits[2]
                        word = num_dict[hundred_digits] + " " + \
                            num_dict["100"] + " and " + \
                            num_dict[ten_digits] + " " + \
                            num_dict[one_digits]
                    else:
                        t = str(i) + ":" + num_dict["100"]
                else:
                    if three_digits[1] == "0":
                        two_digits = three_digits[2]
                    word = num_dict[hundred_digits] + " " + \
                        num_dict["100"] + " and " + num_dict[two_digits]
        elif len(s_num) == 4:
            word = "one " + num_dict[s_num]
    else:
        word = num_dict[s_num]
    r += len(word.replace(" ", ""))
    print(str(i) + ":" + word)

print("Answer:" + str(r))
