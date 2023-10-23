# 나의 스택 클래스
class MyStack:
    list = [] ##저장하는 곳
    size = 0
    # 클래스를 사용할 때 매개변수에는 self가 꼭 들어감
    def __init__(self, size):#파이썬에서 쓰는 생성자 약속
        self.size = size

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