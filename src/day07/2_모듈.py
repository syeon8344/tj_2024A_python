# day07 > 2_모듈.py

# [1] import 모듈이름:
import mod1
print(mod1.add(3,4))  # 모듈명.함수명()

# [2] from 모듈명 import 함수명, 함수명
from mod1 import sub
print(mod1.sub(4,3))

# [3] from 모듈명 import *
from mod1 import *
sub(3,4)

# [4]
import mod2  # 모듈명.변수명 등등 모듈명을 써줘야 한다
print(mod2.PI)

a = mod2.Math()
print(a)  # <mod2.Math object at 0x000001B4C432D4F0>
print(a.solv(5))  # 78.5398

print(mod2.add(3, 4))  # 7

from mod2 import Math, PI  # from까지 쓰면 모듈명을 쓸 필요가 없다
print(PI)  # 3.141592 <-> mod2.PI
b = Math()
print(b)  # <mod2.Math object at 0x0000021D6FF7D820>


# [5]
from src.day06.Task6 import NameAge
person = NameAge()
print(person)  # <mod2.Math object at 0x000001F3FCC6DA60>
