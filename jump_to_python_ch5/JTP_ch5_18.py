import math
#가로 200cm 세로 80cm, 되도록 큰 정사각형
length = math.gcd(200, 80)
number = int((200/length) * (80/length))
print('length: ', length, 'number: ', number)