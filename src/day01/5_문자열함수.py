# 5_문자열함수.py
# 문자열 관련 함수/기능들

# 0) 문자열이 저장된 변수
a = '코딩도 헤매는 만큼 자기 땅이야'

# 1) .count('찾을 문자') : 문자열 내 찾을 문자가 있으면 개수 반환
print(a.count('자'))  # 1, 문자열 내 '자' 문자 개수
print(a.count('가'))  # 0, 존재하지 않는 문자 : 0 반환

# 2) .find('찾을 문자') : 문자가 있으면 그 문자의 위치/인덱스
print(a.find('자'))  # 11, 문자열 내 찾은 문자의 인덱스
print(a.find('가'))  # -1, 존재하지 않으면 -1 (존재하지 않는 인덱스)

# 3) .index('찾을 문자') : 찾을 문자가 있으면 인덱스 반환
print(a.index('자'))  # 11
# print(a.index('가'))  # ValueError : substring not found, 존재하지 않으면 예외발생

# 4) .join('문자열') : 문자열 내 문자 사이사이에 '문자열' 삽입 및 반환
print(','.join(a))  # 코,딩,도, ,헤,매,는, ,만,큼, ,자,기, ,땅,이,야
b = ['자바', '파이썬', 'C', 'JavaScript']
print('<->'.join(b))  # 자바<->파이썬<->C<->JavaScript, 리스트 요소 사이에 특정 문자 삽입해 반환

c = 'AaBbCcDd'
# 5) .upper() : 문자열 내 소문자를 대문자로 치환해서 반환
print(c.upper())  # 'AABBCCDD'
# 6) .lower() : 문자열 내 대문자를 소문자로 치환해서 반환
print(c.lower())  # 'aabbccdd'

# 7) .lstrip() : left strip(), 문자열 왼쪽의 여백 제거
d = '    python    '  # 앞뒤로 공백이 4개 있는 문자열
print(d.lstrip())
# 8) .rstrip() : right strip(), 문자열 오른쪽의 여백 제거
print(d.rstrip())
# 9) .strip() : 문자열 내 양쪽 여백 제거
print(d.strip())

# 10) .replace('기존 문자', '새로운 문자')
# 문자열 내 기존 문자가 있으면 새로운 문자로 치환해서 반환
print(a.replace('코딩', '파이썬'))  # 파이썬도 헤매는 만큼 자기 땅이야

# 11) .split()
# 문자열 내 특정 문자 기준으로 쪼개
print(a.split(" "))  # ['코딩도', '헤매는', '만큼', '자기', '땅이야']
print(a.split(" ")[1])  # 헤메는
print(a.split(" ")[3])  # 자기

# 컴퓨터(파이썬,자바, JS, C 등)에서 문자는 **불변
# 문자열(리터럴), 정수,실수는 **수정이 불가
e = 'Python Program'
e.upper()
print(e)  # Python Program : upper 적용되지 않는다
e.replace("Program", "프로그램")
print(e)  # Python Program : replace 적용되지 않는다

# 새로운 문자열을 변수명에 대입 : 변수가 참조하는 문자열이 변경되었다(O)
e = "파이썬 Program"  # 기존 문자열은 수정되지 않았다
