#반복문을 제어
# break = 반복문 자체를 종료
# continue = 현재 반복상황을 종료하고 다음 반복 시작으로


for i in range(1,10):
    if i % 3 == 0 :
        print(i)
        continue
        print('3의 배수')
