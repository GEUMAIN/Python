#bubble sort
num = [6,4,3,2,1,8,9,5,7]
cnt = 0
swap = 0
for k in range(len(num)):
    #len(num) -1 => 9 * 8 = 72회
    #len(num) - (k+1) => 9 * 8 / 2 = 36회

    for i in range (len(num) - (k+1) ):
        cnt = cnt +1
        if num[i] > num[i+1]: #나와 나 다음을 비교해서 다음이 크다면 바꾸기
            swap = swap + 1
            t = num[i]
            num[i] = num[i+1]
            num[i+1] = t
print(num)
print(cnt)
print(swap)
