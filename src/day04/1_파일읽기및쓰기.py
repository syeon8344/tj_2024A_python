# 1_파일읽기및쓰기.py

# 1) 파일 생성하기 : open(파일명, 열기모드)
# 열기모드 : r = 읽기 전용, w = 쓰기(이미 존재시 내용 전체삭제), a = 파일 끝에 내용 추가
# 파일 열기 : 파일객체변수.open([파일경로]파일명, 열기모드)
# 파일 닫기 : 파일객체변수.close()
# 1. 파일 열기
f = open('새파일.txt', 'w')  # 쓰기 모드의 파일 객체를 반환하는 함수
print(f)
# 2. 파일 닫기
f.close()

# 2) 파일을 쓰기 모드로 열어 내용을 작성하기, 파일객체변수.write(내용물)
f = open("./fileTest/새파일.txt", 'w')  # 해당 경로의 파일을 쓰기모드로 열어 객체 반환
# 쓰기
for i in range(1, 11):  # 1~11미만까지, 1~10까지 반복
    # 들여쓰기 주의
    data = f'{i}번째 줄입니다.\n'
    # 파일에 내용 쓰기
    f.write(data)
f.close()

# 3) 파일을 읽는 여러가지 방법
# 1. .readline() : 파일의 첫번째 줄을 읽어오는 함수
f = open("./fileTest/새파일.txt", 'r')  # 해당 경로의 파일을 읽기모드로 열어 객체 반환
line = f.readline()  # 1번째 줄입니다.
print(line)
while True:  # 무한루프
    line = f.readline()  # 한줄씩 읽어내려간다
    if not line:  # 읽어온 문자가 공백이면
        break  # 무한루프 종료
    print(line.rstrip())  # 아니면 읽어온 문자 출력 ( rstrip() : 문자열 오른쪽 \n 제거)
f.close()  # 파일 닫기

# 2. .readlines() : 파일 한줄씩 요소로 읽어 리스트로 반환
f = open("./fileTest/새파일.txt", 'r')
lines = f.readlines()
print(lines)
print("\n.readlines() for loop")
for line in lines:  # 리스트 요소를 하나씩 반복변수에 대입해서 반복처리
    line = line.strip()
    print(line)
f.close()  # 파일 닫기

# 3. .read() : 파일 내용 전체를 문자열로 반환하는 함수
f = open("./fileTest/새파일.txt", 'r')
data = f.read()  # 파일 내 내용 전체를 문자열로 읽어온다
print("\n.read()")
print(data)
f.close()  # 파일 닫기

# 4. 파일 객체와 for문
# 파일 객체는 기본적으로 for문과 함께 사용하여 줄 단위로 읽을 수 있다.
f = open("./fileTest/새파일.txt", 'r')
for str in f:  # 파일 객체내 한줄씩 반복변수에 대입해 반복처
    print(str)
f.close()

# 4) 파일에 새로운 내용 추가
f = open("./fileTest/새파일.txt", 'a')  # 추가모드로 파일 객체 반환
for val in range(11,20):  # 11~20미만, 11~19까지
    data = f'{val}번째 줄입니다.\n'
    f.write(data)  # 파일에 내용 쓰기
f.close()

# 5) with 자료 as 파일객체변수 : with절에서 자원을 얻어 사용하고 *반납
# 파일은 열고 나면 항상 닫아야 한다.
# with ... as 를 쓰면 해당 자료를 변수에 대입하고 with가 끝나면 변수 자동 초기화
with open("foo.txt", 'w') as f:
    # open된 파일을 f변수에 대입하고 with가 끝나면 f변수 초기화, close()
    f.write("Life is too short, you need python")
# 폴더 내 foo.txt 생성됨
