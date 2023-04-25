# -*- coding: utf-8 -*-
"""1.파이썬 기초

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z-s2YvTwDLE4U8wRADEXj3XNp0DCM9w3
"""

print('i want go home')
#중요한 링크
#https://github.com/GEUMAIN
#https://code.juwon.info/problemset.php

"""#띄어쓰기 조심 print는 문장출력 명령어"""

name=input('니 이름은 뭐니?\n')

print(f'안녕,{name}!')

"""# 파이썬에서 변수만들기 쉽다 약속되지 않은 이름을 사용하면 됨"""

age=17
name2='정인서'

print('나는',name2, '이고', age, '살입니다')

a= 5
b=3
print(a%b) #나머지를 구하는 연산자

a=5
b=3
print(a == b) # == 같은거 비교연산자
print(a!=b) #!= 같지 않은가 비교

a=5
b=2
t=b
b=a
a=t
print(a, b)

str= 'hello'
print(str)

#우리반  학생을 저장 (1~10번)
#방법1
s1= '정인서'
s2='홍길동'
#만약 학생이 100명이라면? ==> 100명의 변수가 필요

#하나의 묶음으로 보관 => List (다른 언어에서는 배열 array)
student=['정인서','홍길동', 100] #리스트에 다른 형태의 자료형도 보관가능
print(student[2]) #리스트 번지는 0번지 부터 시작
student.append('가나다')
print(student[3])
#리스트에서 쓸수 있는 기능들은 어떤게 있을까?
#리스트에서 특정항목 삭제
student.remove('홍길동') #값을 삭제
#다시 출력
print(student[1])
student.pop(1) #1번째 항목이 삭제
#다시 출력
print(student[1])

#만약 1번의 이름, 국어, 영어, 정보 성적을 보관
#2번의 이름,국어, 영어, 정보
s1= ['김개똥', 100 , 50 , 70]
s2= ['홍길동', 60 , 70 ,100]
cls= [s1, s2] #리스트 안에 리스트르를 넣을 수 있음 => 2차원 리스트
a1=cls[0] #s1 = 김개똥의 배열
print(a1[1]) #김개똥의 국어 점수
print(cls[0][1])
#배열과 리스트가 같을까? => 배열은 크기가 고정=변경불가, 리스트는 변할 수 있다

#여기만 실행하면 안됨
#type(변수)=변수의 타입(자료의 형태를 출력)
print(type(cls))
num=3.14
print(type(num))

#사용자 입력
#첫번째 방법
print('이름을 입력하세요')
name= input() #입력하기 기능
#또는 name = input('이름을 입력하세요')
#print('안녕', name)
#print('안녕'+name)
print(f'hello {name}') #F로 시작하는 포맷팅을 이용해서 변수를 안에 표현할 수 있음

#리스트에서 관해서... 문자열
#string=문자열
str='hello world'
print(str[4]) #['h', 'e' 'l' ......] 저장되고 있음
print(len(str)) # len() 기능은 문자의 길이를 출력

list=[1,2,3,4,5] #배열의 길이를 알 수 있을까?
print(len(list))

#반복문 - 반복된 작업을 쉽게
#상황 - 리스트 = [0, 0, 0, 0, 0,.....] => 100칸 생성
#list = [0,0 ... 0] 또는,
#list = [] list.append(0) 추가하기 100번

#반복 명령어 for, while
#for = 제한된 횟수 만큼 반복
#k= 반복하면서 사용할 변수
#range(범위) 0~범위-1 까지
for k in range(2,5): #2부터 5~1까지
#:표시는 중괄호 시작이랑 같은 뜻
#안에 들여쓰기를 했음.
  print(k) #k는 0~9까지 변신
  print('반복중')

#100개의 리스트 배열을 만들고 [0,2,4,6....] 순서로 값을 초기화
#배열의 항목을 추가하는 명령어 append
list=[]
for n in range(0,200,2):
  #list.append(n*2)
  list.append(n)



print(list)

year=int(input()) #윤년 과제
if (year%4==0 and year%100!=0) or year%400 ==0:
    print(1)
else:
    print(0)

#for는 반복문 => 똑같은 작업을 할 수 있도록 횟수를 지정하는 반복문
#입력하는 단의 구구단 출력
#예) 3입력 ==> 3*1=3 .... 3*9=27
n=input('숫자를 입력하세요')
#print(n*3) #in-put으로 받은 값은 문자로 처리됨
k=int(n) #int타입=정수값으로 변경
print(k*3)
## ==>> n=int(input('숫자입력'))

#진짜 입력 받은 숫자를 가지고 구구단 만들기
#입력하는 단의 구구단 출력
n=int(input('숫자를 입력하세요')) #내가 원하는 숫자입력
for k in range(1,10): #1~10 전까지 = 1~9 #콜론: 붙이도록
  #print(n,"*",k,"=",n*k)
  print(f'{n}*{k}={n*k}')

#1~ 입력수 n 까지 369게임 (n=2~9)
#3,6,9에는 대문자 X를 출력
#그리고 숫자마다 공백

# 0 사용시 입려을 숫자로 받기
#1부터 입력수 까지 출력 => for문 필요
# 3,6,9 인지 검사를 하여 X로 변환
A=int(input('숫자를 입력하세요'))
for b in range(1,A+1):
  #1부터 K까지 나옴

  #if 조건: => 참인지 검사
  # 참이라면 수행할 내용
  #if A가 3이랑 같은가
  if b == 3 :  #등호를 하나만 쓰면,   <-  복사,      == 비교하는것
    #들여쓰기 조심
    print('X')
  else:  #그 밖에  if와 같이 사용됨. if는 혼자 쓸수 있지만, else 혼자 사용 불가
    #들여쓰기 조심
    if b == 6 :
      print('X')
    else:
      if b == 9:
        print('X')
      else:
        print(b)

A=int(input('숫자'))

for i in range(1,A+1):
  #만약 3으로 나누어 떨어지는가 == 나머지가 0인가
  # % = 나머지를 구하는 연산자 => 10 % 3 =1
  if i==3 or i==6 or i==9:
    print('X', end=' ')
  else:
    print(i, end=' ')

#if 문 복습 for 문과 연계
#if = 조건반사 = 만약 조건이 참여만 수행할 내용 작성
a=5
#a가 5보다 크다면 "큰수" 출력
if a>5: #콜론 표시의 주의
#콜론 다음에는 현재보다 들여쓰기 (탭)
  print('큰수')
  print('입니다.')
###차이점
if a>5:
  print('큰수')
print('입니다')

if a>5:
  print('큰수')
else: #else = '그 밖에' 참이 아닌 경우는 전부 이쪽으로 오게됨.
  print('작은수')

#내가 생각한 숫자 맞추기
#10번의 기회동안 숫자를 맞춤
#10번의 기회 -> 10번동안 입력을 받아야겠음
#10번동안 -> 10번 반복 -> for문 필요
#입력받음 -> input() 필요
#내가 입력한 숫자가 맞는 검사(만약 일치하나???) -> if문 필요
#10번 반복할 동안 검사를 매번 수행 -> for 문 안에서 입력도 받고, 검사도 하고

ans = 15 #정답
#10번 반복
for i in range(10):
  num = int(input('정답은?'))
  #ans랑 num이랑 같은가
  if ans==num:
    print('정답')
  else:
    print('오답!')

#내가 생각한 숫자 맞추기
#10번의 기회동안 숫자를 맞춤
#10번의 기회 -> 10번동안 입력을 받아야겠음
#10번동안 -> 10번 반복 -> for문 필요
#입력받음 -> input() 필요
#내가 입력한 숫자가 맞는 검사(만약 일치하나???) -> if문 필요
#10번 반복할 동안 검사를 매번 수행 -> for 문 안에서 입력도 받고, 검사도 하고

ans = 15 #정답
#10번 반복
for i in range(10):
  num = int(input('정답은?'))
  #ans랑 num이랑 같은가
  if ans==num:
    print('정답')
  else:
    #틀린 숫자만 오는 경우
    #또 검사
    if ans> num:
      print('UP')
    else:
      print('DOWN')

#내가 생각한 숫자 맞추기
#10번의 기회동안 숫자를 맞춤
#10번의 기회 -> 10번동안 입력을 받아야겠음
#10번동안 -> 10번 반복 -> for문 필요
#입력받음 -> input() 필요
#내가 입력한 숫자가 맞는 검사(만약 일치하나???) -> if문 필요
#10번 반복할 동안 검사를 매번 수행 -> for 문 안에서 입력도 받고, 검사도 하고
#파이썬 랜덤 값 1~100까지
import random
#ans=15
ans =random.randint(1,100) #정답
#10번 반복
for i in range(10):
  num = int(input('정답은?'))
  #ans랑 num이랑 같은가
  if ans==num:
    print('정답!')
    #빠져나가기 -> 파이썬에서 반복문 빠져나가기
    break
    #else 아래에 if를 또 쓰자니 번거로움.
  elif ans > num:
    print('UP')
  else:
    print('DOWN')
print('정답은')
print(ans)

#파이썬 랜덤 값 1~100까지
import random
a=random.randint(1,100)
print(a)

for i in range(100):
    num = int(input())

print("\u250C\u252C\u2510\n")
print("\u251C\u253C\u2524\n")
print("\u2514\u2534\u2518\n")

print('#include <stdio.h>')
print('int main()')
print('{')
print('  printf("Hello World\\n");')
print('}')

#숫자를 입력받기 기능 => n이라고 하자
#1부터 n까지 반복 => for
#반복하면서 나오는 숫자가 짝수 인지 검사 %2==0
#합 구하기 => 합을 보관하는 변수 sum을 만들자
n=int(input())
sum=0
for i in range(1,n+1):
#i가 1~n까지 값이 들어옴
#i가 짝수인지 판단
  if i%2==0:
#sum에다 i를 누적 => 누적한다는 것은 현재sum에 k를 추가=>sum에 보관
    sum=sum+i
#반복이 끝났음
print(sum)
#n=int(input())
#sum=0

#for i in range(2,n+1,2):
  #if i%2==0:
    #sum=sum+i
#print(sum)

n=int(input())
sum=0 #합계
if n%2!=0:
  n=n-1 #n을 마지막 짝수로 만듬
  mid= int(n/2)-1
else:
 mid= int(n/2)+1
sum = ((n+2) * int(n/4)) + mid
print(sum)

#가위1 바위2 보3

me=int(input('너는 뭐 낼래? 가위1 바위2 보3'))
com=int(input('컴퓨터는 뭐 낼래? 가위1 바위2 보3')) # 가위를 냈다고 하자

#나의 컴의 비교를 해서 승, 패, 무승부를 출력!
if me == com:
  print('무승부')
#내가 이기는 경우
#나==1 컴==3,나==2 컴==1 나==3 컴==2
#elif (me ==1 and com == 3) or (me ==2 and com==1) or (me ==3 and com==2):#또는 2번째 또는 3번째
#elif (me-com==-2) or (me-com==1):
elif (me-com%3==1):
  print('이겼습니다')
else:
  print('졌습니다')

"""if else
if elif
if elif else

elif, else 단독으로 쓰일 수는 없음

or = 둘 중 하나만 만족해도 참
and = 둘 다 만족해도 참
=> 논리 연산자(참, 거짓)

bool = 참 거짓을 보관하는 타입
int k=숫자 하나 보관
char k=문자 하나만 보관
"""

# 1이 입력되면 0, 0이 입력되면 1로 출력하는 프로그램 만들자
n=(input()) #문자로서 입력
#if n ==1: #n은 문자값이므로 문자1과 숫자1은 다름
if n == '1': #문자 '1'
  print('0')
else:
  print('1')

n=int(input())
print(1-n)

#for문과 배열을 섞어보자
#배열 = 리스트 => 변수의 집합 => 여러개의 변수를 묶어서 보관
#그럼 어떻게 안에 있는 자료를 접근할 수 있을까?? => 주소

lt=[] #빈 리스트를 만들기
#리스트 관련된 명령어 알기
#lt. => 점을 찍으면 사용할 수 있는 명령어가 나옴
# http://wikidocs.net/14
lt.append(1) #뒤에 추가
lt.append(10)
lt.insert(1, 5) #(번지, 추가할 값), 리스트는 0번지 부터 출발
lt.insert(0,20) #[20,1,5,10]

#1번지에 있는 1을 삭제
lt.remove(1) #삭제할때는 주소번지만 이용해서 삭제
print(lt)

#[0,10,20,30,40,50 .... 1000] 인 배열을 만들자
# 0 번지에 0, 1번지에 10, 3번지 30, ... n번지 n*10
lt=[]
#for 변수 k in 범위(리스트를 써도 되고,range() 이용)
for k in range(0,1001,10):
  lt.append(k)  
print(lt)

#pos=lt.index(40) #값을 찾아보고 있으면 해당 번지를 출력
arr_str='hello word'
pos=arr_str.find('w')
print(pos)

str='hello world' #문자열도 리스트로 다룰 수 있음
print(str[6])
print(str.index('w'))
#문자열에서는 find 명령어도 사용할 수 있음
print(str.find('w'))
#find는 찾지 못하면 오류대신 -1를 출력
print(str.find('t'))



#리스트에서 index를 쓰지않고 해당 위치 변환

a=[1,2,3,4,4,4,7] #크기 고정
size=len(a) #a 배열의 길이, a.length 아님...(자바에서 이렇게)
find=int(input())
#for문을 이용 => a의 크기 만큼 반복검사
for k in range(size):
  #a[k]야 find를 같음?
  if a[k]== find:
    print(k)
    break

#a에서 쓸 수 있는 기능
#pos=a.index(4)
#print(pos)


###결과###
#4입력 => 3(번지) 출력

#마지막부터 값 찾기
#hint range의 활용
a=[0,1,2,3,4,5,6,7,8,9]
size=len(a)
find=int(input())
#range(5) 0~4까지
#range(1,5) 1~4까지
#range(1,10,2) 1~9까지 2씩 증가
#10부터 1까지 1씩 감소 => range(11,1,-1)
#for k in range(size-1,-1,-1):
  #if a[k]==find:
  #  print(k)
 #   break

for k in range(size):
  #0번지 => 9 만들기
  pos = size - 1 - k  #=0일때 #10-1-k=>9-0=9번지 찾기
  if a[pos] == find:
    print(pos)
    break

#n=[1,3,5,7,76,8,3,1,2,3,54]
n=['jan','feb','mar','apr','may','june','july']
#range(10)= [0,1,2,3,4,5,6,7,8,9]
for k in n: #in 다음에는 range만 가능한게 아님. 범위를 가지고 있는
  print(k)

#반복문

#조건이 참인 동안 반복
k=0
while k < 5:
  print(k)
  k=k+1

print('byebye')
print(k)

#패스워드를 검사하자 비번이 맞을 때 까지 반복

#비번이 틀렸을 대 반복

pw='1234' #문자 1234

my=input('패스워드를 입력하세요')

#비번이 틀렸을 때 반복 pw=my같지 않을때
while pw != my: #!는 부정의 의미
  my=input('패스워드를 입력하세요')

print('welcome')

pw = '1234'

#무조건 반복하다가 조건이 맞으면 탈출(break)

while True:
  my=input('비번입력')
  if my == pw:
    print('로그인에 성공하였습니다')
    break
  if my != pw:
    print('틀렸습니다 다시 입력해주세요')
    continue

#값을 보관 하기
#- 변수를 사용 -
#a= 1 <= 오른쪽에서 왼쪽으로 복사
#저장되는 것에 종류가 있을까?=자료형(숫자,문자, 참/거짓...), 자료의 형태를 저장하지 않음

#-만약, 24명의 학생을 보관하려고 함. 변수가 몇개 필요하지?=>24개 필요 => 너무 많음 => 한번에 관리할 수 없을까?
#-리스트: 변수들의 집합, 모임(리스트(배열))..., 튜플, 딕셔너리, 집합)
#-a[0] =1  #a리스트의 0번지에 1을 저장
#-번지에 꼭 숫자가 들어가야 할까? => 아니다. => 변수가 들어갈 수 있음(숫자인 변수)
#-arr=1 it[arr]=1 #it리스트의 1번지에 1이 들어감 it[1]
#-리스트의 크기는 변함, 항목을 추가할 수도 있고, 뺄 수도 있음
#-항목을 추가하는 append, remove
#기능을 사용하기
#-파이썬에서 만든 기능을 사용
#-명령어() 의 형태
#=print)), append(), len(), input(), int()
#-기능을 만들어서 사용할 수 있음, def:

#-print, print() 은 다른말
#문법
#-반복문:같은 작업을 여러번 반복시키는 명령
#-for: 일정 범위 만큼 반복
#- 예) 10번 반복해X => 0~9만큼 반복해
#for 사용할 변수 in range(10): #사용할 변수의 0~9까지 적용
#range() 활용
#-rage(10): 0~9, range(5,10): 5~9 range(3,10,2): 3~9, 2씩 증가
#-# 10, 0 ,1씩 감소(=-1씩 증가)
#-while: 조건이 참일 동안 계속 반복
#- 들여쓰기 조심

#리스트와 for를 사용해보자
#리스트를 만드는데 [0,1,2,3,4] 가 보관된 리스트 만들기
lt=[] #아무것도 없는 리스트 , append이용해 추가
size=int(input('크기를 입력하세요'))
for k in range(0,size): #k는 0~size-1까지 보관
  #들여쓰기 조심
  lt.append(k)
print(lt)

ans = 'q'
while ans != 'Q':
  ans=input('Q를 입력하면 종료합니다.')

#숫자 하나를 입력받고, 그 숫자부터 1까지 출력
n = int(input('숫자입력'))
while n >= 1: # n > 0
  print(n)
  n=n-1 # n -= 1

#숫자를 하나 입력받아서 입력 수 부터 100까지 반복
n = int(input('숫자입력'))
while n < 101:
  print(n)
  n = n+1

