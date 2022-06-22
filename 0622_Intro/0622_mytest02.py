#입력받은 두 수 사이의 숫자들은 합 구하기
a = input("숫자 첫번째 출력")
b = input("숫자 두번째 출력")

aa = int(a)
bb = int(b)

arr = range(aa, bb+1)
sum = 0

for i in arr:
    sum += i
print("{}에서 {}까지의 모든 숫자의 합은 {}입니다.".format(aa, bb, sum))
