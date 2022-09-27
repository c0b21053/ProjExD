import random

m = "問題"
i = random.randint(0,2)
ans0 = ["ますお","マスオ","ますおさん","マスオさん"]
ans1 = ["わかめ","ワカメ"]
ans2 = ["おい","甥","おいっこ","甥っ子"]
kaitou = "出直してこい"
def syutudai(i):
    if i == 0:
        m = "サザエさんの旦那の名前は？"
    elif i == 1:
        m = "カツオの妹の名前は？"
    else:
        m = "タラオはカツオから見てどんな関係？"
    
    return m

def kaitou(i):
    a = input()
    if i == 0:
        if a in ans0:
            kaitou = "正解！！！"
    elif i == 1:
        if a in ans1:
            kaitou = "正解！！！"
    else:
        if a in ans2:
            kaitou = "正解！！！"

syutudai(i)
kaitou(i)
