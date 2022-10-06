# 30. Вычислить число pi c заданной точностью d
# 	  Пример: при d = 0.001,  pi = 3.141. 10^(-1) <= d10 <= 10^(-10)

import math
from math import pi

n = input("d = ")
a = pi
template = '{:.' + str(n) + 'f}'
print(template.format(a))