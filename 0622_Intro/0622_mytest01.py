"""
    첫 숫자를 입력하시오
    두번째 숫자 입력
    두 수의 합은 n입니다.
"""

from tkinter.tix import INTEGER


a = input("숫자를 입력하세요")
b = input("숫자를 또 입력하세요")
c = int(a) + int(b)
print("두 수의 합은 " + str(c) +"입니다.")
