class Animal:
    def __init__(self):
        print("생성자")
        
    def aging(self):
        print("일반함수")
    
    #가비지 컬렉터와 같음
    def __del__(self):
        print("소멸자")
    
    #toString과 같음
    def __str__(self):
        return "babo"
    
    
a = Animal()
a.aging()
print(a)
