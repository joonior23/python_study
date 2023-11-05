import itertools
import random

name = ['김승현', '김진호', '강춘자', '이예준', '김현주']
work = ['청소', '빨래', '설거지']

from random import shuffle
from itertools import zip_longest
random.shuffle(name)
result = itertools.zip_longest(name, work, fillvalue='휴식')
print(list(result))