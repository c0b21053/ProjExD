import random
import datetime

num_alpha = 26
q_alphaNum = 10
lost_alphaNum = 2
try_num = 2

def syutudai():
    print("対象文字：")
    qus = [random.randint(1,num_alpha) for i in range(q_alphaNum)]
    for a in qus:
        print(chr(a+64), end=" ") 
    print()
    lost_qus = random.sample(qus,8)
    for b in lost_qus:
        print(chr(b+64), end=" ")
    print()
    kaitou(qus,lost_qus)


def kaitou(a,b):
    for i in b:
        a.remove(i)
    ans = input("欠損文字はいくつあるでしょうか？")
    if ans == "2":
        print("正解です。それでは、具体的に欠損文字を一つずつ入力してください。")
        while True:
            ans1 = input("一つ目の文字を入力してください")
            if ord(ans1)-64 in a:
                n = ord(ans1)-64
                a.remove(n)
                ans2 = input("二つ目の文字を入力してください")
                if ord(ans2)-64 in a:
                    print("正解です！")
                    break
                else:
                    print("不正解です。またチャレンジしてください")
                    continue
    else:
        print("不正解です。またチャレンジしてください。")
      
if __name__ == "__main__":
    syutudai()