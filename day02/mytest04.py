# 1에서 9 사이의 정수 중 3가지를 중복 없이 랜덤으로 출력하세요
from random import random

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("원래 배열 : {}".format(arr))

temp = arr[0]
arr[0] = arr[1]
arr[1] = temp
print("1과 2만 섞은 후 : {}".format(arr))

for i in range(10):
    rnd = int(random()*9)
    temp = arr[0]
    arr[0] = arr[rnd]
    arr[rnd] = temp
    
print("랜덤으로 섞은 후 : {}".format(arr))
