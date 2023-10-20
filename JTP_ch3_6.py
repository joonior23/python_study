# list comprehension example 홀수만 골라 2를 곱하기

# numbers = [1,2,3,4,5]
# result = []
# for n in numbers:
#   if n % 2 == 1:
#       result.append(n*2)

numbers = [1,2,3,4,5]
result = [num*2 for num in numbers if num%2==1]
print(result)