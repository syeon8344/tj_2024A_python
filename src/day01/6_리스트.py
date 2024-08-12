# 6_리스트.py
# 여러 자료들을 하나의 자료로 묶은 형태
# 어떤 자료형이던 포함 가능

# 1) 리스트 타입 형태
# 변수명 = [요소1, 요소2, 요소3...]
odd = [1, 3, 5, 7, 9]
print(odd)

a = []
print(a)

b = [1, 2, 3]
print(b)

c = ['life', 'is', 'too', 'short']
print(c)

d = [1, 2, 'life', 'is']
print(d)

e = [1, 2, ['life', 'is']]
print(e)

# 2) 리스트 인덱싱 및 슬라이싱
studentList = ['유재석', '강호동', '신동엽', '서장훈']

# 인덱싱 : 인덱스 이용한 요소 추출
# [0]  [1]  [2]  [3]
# [-4] [-3] [-2] [-1]
print(studentList)  # ['유재석', '강호동', '신동엽', '서장훈']
print(studentList[0])  # 유재석
print(studentList[1])  # 강호동
print(studentList[3])  # 서장훈
# print(studentList[4])  # 예외발생, IndexError : index out of range
print(studentList[-1])  # 서장훈
print(studentList[-3])  # 강호동
print(studentList[-4])  # 유재석

# 슬라이싱 : 인덱스를 이용한 요소들 추출
print(studentList[0:2])  # ['유재석', '강호동'], 0에서 2 직전까지
print(studentList[0:3])  # ['유재석', '강호동', '신동엽'], 0에서 3 직전까지
print(studentList[:4])  # ['유재석', '강호동', '신동엽', '서장훈'], 0에서 4 직전까지 전부
print(studentList[2:])  # ['신동엽', '서장훈'], 2부터 끝까지
print(studentList[:])  # ['유재석', '강호동', '신동엽', '서장훈'] 모두 생략시 전체출력
print(studentList[0:4:1])  # ['유재석', '강호동', '신동엽', '서장훈'], 요소 하나씩 증감
print(studentList[0:4:2])  # ['유재석', '신동엽'], 요소 두칸씩 증감
print(studentList[-1:-5:-1])  # ['서장훈', '신동엽', '강호동', '유재석'], 역순으로 한칸씩
print(studentList[-1:-5:-2])  # ['서장훈', '강호동'], 역순으로 두칸씩

# 3) 리스트 연산
# [list1] + [list2] = [list]
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)  # [1, 2, 3, 4, 5, 6]

# [list1] * 반복수 = [list1, list1, list1 ... ]
c = a * 3
print(c)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# len([list]) = 리스트의 요소 개수
print(len(a))  # 3

# 4) 리스트내 요소의 값 수정, 리스트명[수정할인덱스] = 새로운 값
a[1] = 4
print(a)  # [1, 4, 3]

# 5) 리스트 내 요소 삭제, del 리스트명[인덱스]
del a[1]
print(a)  # [1, 3]
del b[1:]
print(b)  # 인덱스 1부터 마지막까지 삭제, [4]

# 6) 리스트 관련 함수들
# 1. .append(elem) : 리스트의 마지막에 값 추가
a = [1, 2, 3]
a.append(4)
print(a)  # [1, 2, 3, 4]

# 2. .insert(index, value) : 리스트 특정 인덱스에 요소 추가 (원래 있던 요소들은 뒤로 밀려난다)
a.insert(0,6)
print(a)  # [6, 1, 2, 3, 4]

# 3. .remove(value) : 리스트에 특정 값이 있으면 삭제
a.remove(1)
print(a)  # [6, 2, 3, 4]
# a.remove(1)  # ValueError: list.remove(x): x not in list
# print(a)

# 4. .pop() : 가장 마지막 값 삭제
#    .pop(index) : 특정 위치의 요소 삭제
a.pop()
print(a)  # [6, 2, 3]
a.pop(1)
print(a)  # [6, 3]

# 5. .count(요소값) : 리스트에 해당 요소값이 몇개 들어있는지 반환
a = [1,2,3,1]
print(a.count(1))  # 2, 해당 요소값이 두개

# 6. .index(찾을요소값) : 리스트의 해당 찾을 요소값이 존재하는 인덱스 반환
print(a.index(1))  # 0, 리스트 내 1의 위치는 0 반환 ( 가장 먼저 검색되는 index만 반환)

# 7. .extend(리스트) : 해당 리스트를 뒤에 합치기
b = [4, 5]
a.extend(b)
print(a)  # [1, 2, 3, 1, 4, 5]

# 8. .sort() : 해당 리스트 요소들을 오름차순 정렬
a.sort()
print(a)  # [1, 1, 2, 3, 4, 5]

# 9. .reverse() : 순서를 앞뒤로 뒤집기
a.reverse()
print(a)  # [5, 4, 3, 2, 1, 1]
