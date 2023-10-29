f1 = open("test.txt",'w')
f1.write("Life is too short")

# f1을 close 하지 않아서 f2가 읽을 수 없음
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())