# day 07 > 5_내장함수.py
# 파이썬 배포본에 같이 들어있는 함수들 : 라이브러리
# import 필요없다,

# 1. abs(숫자) : 절댓값
print(f"절댓값 : {abs(3)}, {abs(-3)}, {abs(1.2)}")

# 2. all(리스트/튜플/문자열/딕셔너리/집합) : 모두 참이면 참 반환
# 데이터들의 참과 거짓 -> day02 bool 참고
print(f"{all([1, 2, 3])}, {all([1, 2, 3, 0])}, {all([])}")  # T, F, T // all([]) True : 0인 원소가 0개이므로(없으므로) True

# 3. any(리스트/튜플/문자열/딕셔너리/집합) : 하나라도 참이면 참 반환
print(f"{any([1, 2, 3])}, {any([1, 2, 3, 0])}, {any([])}")  # T, T, F // any([]) False : 0 이상인 원소가 없으므로 False

# 4. char(유니코드): 유니코드 숫자를 문자로 반환
print(f"{chr(97)},{chr(44032)}")  # a, 가

# 5. dir(객체): 해당 객체가 가지는 변수나 함수를 보여주는 함수
print(f"{dir([])}, {dir({})}")

# 6. divmod(a, b): a를 b로 나눈 몫과 나머지를 튜플로 반환
print(divmod(7, 3))  # 몫 : 2, 나머지 : 1 (2,1)

# 7. enumerate(리스트/튜플,문자열) : 인덱스 값을 포함한 객체를 반환
for i, name in enumerate(['body', 'foo', 'bar']):  # 인덱스, 값
    print(i, name)

# 8. eval(문자열로 구성된 코드): 문자열을 코드로 실행한 값 반환
print(eval('1+2'))  # => 1 + 2 => 3
print(eval("'hi' + 'a'"))  # hia
print(eval('divmod(4,3)'))  # (1, 1)


# 9. filter(함수, 데이터): 첫번째 인수로 함수, 두번째 인수로 데이터를 받아 결과가 참인 것만 묶어 반환
def positive(x):
    return x > 0


data = [1, -3, 2, 0, -5, 6]
result = filter(positive, data)
print(list(result))  # list(): 리스트 타입으로 반환하는 함수
# 람다식 함수, lambda 매개변수들 : 실행문
# 간단한 함수를 간결하게 사용
print(list(filter(lambda x: x > 0, data)))  # return이 없어도 결과값이 반환된다 [1, 2, 6]
add = lambda a, b: a + b
print(add(3, 5))  # 8
filter(lambda x: x > 0, data)  # JS: data.filter( x => x > 0)

# 10. map(함수, 데이터): 함수와 데이터를 인수로 받아 전체 데이터를 함수를 적용해 map 객체로 반환, 리스트로 타입변환 가
print(list(map(lambda x: x * 2, data)))  # [2, -6, 4, 0, -10, 12]

# 11. hex: 정수 -> 16진수
print(hex(234))
print(hex(255))

# 12. id(객체): 입력받은 객체의 고유 주솟값(레퍼런스) 반환
a = 3
print(id(a))  # 140724318046712, 같은 객체를 가리킨다
print(id(3))  # 140724318046712

# 13. input([안내문]): 사용자 입력을 받는다
# i = input("input : ")  # 'input : '안내문 출력, 입력값을 i 변수명으로 저장
# print(i)  # 입력한 값 출력

# 14. int(숫자 문자열/실수/정수): 정수 형태로 반환 (정수 -> 정수)
print(int(3.141592))  # 3
print(int("12345"))  # 12345
print(int(1234))  # 1234
# 14-1. int('radix진수', radix): n진수로 표현된 값을 10진수로 변환해서 반환
print(int('110011011', 2))  # 411
print(int('fffaacbc', 16))  # 4294618300

# 15. isinstance(객체, 클래스): 입력받은 객체가 입력받은 클래스의 인스턴스인지 True/False
# class Person(): pass
# a = Person()
# print(isinstance(a, Person))  # True
# b = 3
# print(isinstance(b, Person))  # False

# 16. len(요소): 요소의 전체 길이 반환
print(len("python"))  # 6
print(len([1, 2, 3, 4, 5]))  # 5

# 17. list(iterable): 반복 가능한 데이터를 받아 리스트로 반환
print(list("python"))  # ['p', 'y', 't', 'h', 'o', 'n']
print(list((1, 2, 3, 4)))  # [1, 2, 3, 4]

# 18. max(iterable): 반복 가능한 데이터를 받아 최댓값 반환, 문자열은 유니코드 값으로 비교
print(max([1, 2, 3, 4]))  # 4
print(max("Python"))  # y

# 19. min(iterable): 반복 가능한 데이터를 받아 최솟값 반환, 문자열은 유니코드 값으로 비교
print(min([1, 2, 3, 4]))  # 1
print(min("Python"))  # P

# 20. oct(정수): 정수를 8진수로
print(oct(12245))  # 0o27725

# 21. open(파일명 [, 모드]): 모드 기본값: 읽기('r'), 파일 객체를 만들어 반환
# 'w' = 쓰기, 'r' = 읽기, 'a' = 내용 추가, 'b' = 바이너리 모드, 'x' = 파일 생성후 쓰기모드
# f = open("파일명.확장자", "r")

# 22. ord(문자): 문자의 유니코드 값
print(ord('힣'))  # 55203
print(ord('a'))  # 97

# 23. pow(x, y): x의 y제곱
print(pow(2, 7))  # 128
print(pow(10, 5))  # 100000

# 24. range([시작,] 끝 [,단계]): 입력받은 숫자에 해당하는 범위 값을 iterable로 만들어 반환, 끝 숫자 직전까지
print(list(range(5)))  # 0,1,2,3,4  # 5는 미포함
print(list(range(1, 5)))  # 1,2,3,4
print(list(range(1, 5, 2)))  # 1,3  # 2칸씩 거리

# 25. round(실수 [, 이하 자리에서 반올림]): 숫자를 입력받아 반올림, 둘째 매개변수는 n번째 자리까지 반올림(선택)
print(round(3.1415))  # 3
print(round(3.1415, 2))  # 3.14, 2번째 자리까지 반올림

# 26. sorted(iterable): 데이터를 정렬한 후 결과를 리스트로 반환
print(sorted((1, 3, 2, 5)))  # [1, 2, 3, 5]
print(sorted("zbwcwsa"))  # ['a', 'b', 'c', 's', 'w', 'w', 'z']
print(sorted([5, 3, 1, 2]))  # [1, 2, 3, 5]

# 27. str(object): 문자열 형태로 객체 반환
print(str(123))  # '123'
print(str((1, 2, 3)))  # '(1, 2, 3)'

# 28. sum(iterable): 반복가능한 데이터의 입력 데이터의 합 반환
print(sum([123, 213]))  # 336
print(sum((1, 2, 3, 4)))  # 10

# 29. tuple(iterable): iterable(반복가능한 데이터)을 튜플로 바꾸어 리턴, 튜플이면 복사
print(tuple('abc'))  # ('a', 'b', 'c')
print(tuple([1, 2, 3]))  # (1, 2, 3)
# print(tuple(123))  # TypeError: 'int' object is not iterable

# 30. type(객체): 입력한 값의 자료형을 알려준다
print(type('abc'))  # <class 'str'>
print(type([1, 2, 3]))  # <class 'list'>

# 31. zip(data, data1, data2...): 동일한 갯수의 데이터를 가진 데이터들을 한줄씩 묶어서 튜플 리스트로 반환
# zip(d1, d2, d3) -> [(d1[0], d2[0], d3[0]), (d1[1], d2[1], d3[1]), (d1[2], d2[2], d3[2])]
print(list(zip((1, 2, 3), [4, 5, 6], [1, 2, 3])))  # [(1, 4, 1), (2, 5, 2), (3, 6, 3)]
