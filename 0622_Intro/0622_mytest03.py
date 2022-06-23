#홀/짝을 고르세요. 컴퓨터는 랜덤으로 숫자 돌려서 홀짝 조건 발생 후 출력하기

from random import random

mypick = input("홀/짝?!")
rnd = int(random() * 100)

if rnd%2 == 0 :
    answer = "짝"
else : 
    answer = "홀"

if answer == mypick :
    print("결과 : {}!\nyou win!".format(answer))
else : 
    print("결과 : {}!\nyou lose!".format(answer))

#########################################################

com=""
mine = ""
result = ""

mine = input("홀? 짝?")
rnd = random()
print("rnd", rnd)

if rnd > 0.5:
    com = "홀"
else:
    com = "짝"

if mine == com:
    result = "이김"
else:
    result = "짐"
    
print("com", com)
print("mine", mine)
print("result", result)
