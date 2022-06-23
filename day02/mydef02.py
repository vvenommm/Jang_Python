def showDan(dan):
    for i in range(1, 9+1):
        # print(int(dan) * i)
        print("{} * {} = {}".format(dan, i, int(dan)*i))
    pass #에러 방지

for i in range(1, 10):
    print("{}단".format(i))
    showDan(i)
