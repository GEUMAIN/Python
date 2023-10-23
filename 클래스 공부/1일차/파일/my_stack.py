# 나의 스택 클래스
class MyStack:
    
    #클래스 변수로 선언하면, 클래스들은 공유되고같이 변경이 됨.
    # list = [] ##저장하는 곳 #같이 변경이 됨.
    # size = 0
    # 클래스를 사용할 때 매개변수에는 self가 꼭 들어감
    def __init__(self, size):#파이썬에서 쓰는 생성자 약속
        self.size = size #클래스 변수로 self.size를 선언한 적이 없지만 self.size는 나만 쓰는 변수가 됨
        self.list = []
        #나만 스는 list변수를 선언
    def push(self, value):
        if len(self.list) > self.size:
            return False
        else :
            self.list.append(value)
            #self는 클래스에서 선언한 변수 사용
            return True

    def pop(self):
        if len(self.list) < 1 :
            return False
        else:
            self.list.pop()
            return True

    def view(self):
        return self.list