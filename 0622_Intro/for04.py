arr = range(1, 100+1)
print(list(arr))

#range()함수가 for문 역할을 해줌
#i++은 없음.
#귀납법, 연역법 (고1 교과과정)
sum = 0
for i in arr:
    sum += i
print("sum", sum)
