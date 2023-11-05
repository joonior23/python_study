import random
def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    print(number)
    return data

data = list(range(1,46))
for i in range(6):
    random_pop(data)