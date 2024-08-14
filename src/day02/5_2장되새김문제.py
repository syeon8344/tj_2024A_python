# 5_2장되새김문제.py
""""""

# Q1
'''
    과목 점수
    국어 80
    영어 75
    수학 55
'''
scores = [80, 75, 55]
average = 0
for score in scores:
    average += score
print(average / 3)
"70.0"

# Q2
num = 13
if num % 2 == 1:
    print(f"{num}은(는) 홀수입니다")
else:
    print(f"{num}은(는) 짝수입니다")

# Q3
pin = "881120-1068234"
yyyymmdd = pin[0:6]
num = pin[7:]
print(yyyymmdd)
print(num)

# Q4
print(pin[7])

# Q5
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

# Q6
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# Q7
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

# Q8
a = (1, 2, 3)
a = (1, 2, 3) + (4,)
print(a)

# Q9
a = dict()
# a[[1]] = 'python'
print(a)
"리스트는 불변값이 아니므로 딕셔너리 키로 사용 불가"

# Q10
a = {'A': 90, 'B': 80, 'C': 70}
result = a.pop('B')
print(a)
print(result)

# Q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

# Q12
a = b = [1, 2, 3]
a[1] = 4
print(b)
"변수는 주소값을 참조하므로 a와 b는 같은 [1, 2, 3] 객체를 참조하고 a[1] = 4로 객체가 [1, 4, 3]이 되어 b도 값이 같이 변한다"
