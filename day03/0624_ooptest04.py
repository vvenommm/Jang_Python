from day03.ooptest02 import SeungJe


sj = SeungJe()
print(sj.money)
print(sj.cnt_hair)
print(sj.nuclear)
sj.copycopy(1)
sj.stress(50)
sj.ssorau(20)
print(sj.cnt_hair)
print(sj.money)
print(sj.nuclear)

#스크립트 언어이기 때문에 import한 파일을 쭉 읽어들인 후에 본 파일을 실행. 그래서 두번씩 실행됨
#그래서 클래스 만든 후 확인해보고 싶으면 main에서 따로 실행해줘야 다른 파일이 import할 때 실행되지 않음.
