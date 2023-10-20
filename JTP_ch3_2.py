#1~1000 중 3의 배수의 합
result = 0
i = 1
while i<=1000:
    if i%3==0:
        result+=i
    i+=1
print(result) #166833 출력