#Life is too short
#you need java
f = open('test.txt', 'r')
body = f.read()
f.close()
body = body.replace('java', 'python')
print(body)
f = open('test.txt', 'w')
f.write(body)
f.close()