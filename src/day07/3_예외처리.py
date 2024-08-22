# day07 > 3_예외처리.py
# 예외처리: 프로그램 실행 도중에 발생하는 오류를 다른 실행문으로 처리

num_list = [1, 2, 3]
# num_list[3]  # 예외발생: 존재하지 않는 인덱스

# [1] 예외 처리 방법 1
try:
    # 예외가 발생할 것 같은 코드들
    num_list[3]
except:
    # 예외 발생시 실행되는 코드
    print("index not found")

# [2] 예외 처리 방법 2
try:
    num_list[3]
except IndexError:  # 특정 예외 처리시 예외클래스명 작성
    print("index not found")

# [3] 예외 처리 방법 3
try:
    num_list[3]
except IndexError as e:  # 특정 예외가 발생한 이유를 보고싶을 때 as 예외변수명
    print(e)

# [4] finally: 예외 발생 여부과 상관없이 무조건 실행 e.g. 파일 닫기 등
try:
    num_list[3]
except Exception as e:
    print(e)
finally:
    print("always executed")

# [5] 다중 except
try:  # try 안에서 예외가 발생하면 바로 아래로 넘어가므로 예외처리는 0번 또는 1번 실행된다.
    # print(4/0)
    int("a")
except IndexError as e:  # IndexError 발생 시 코드
    print(e)
except ZeroDivisionError as e:  # ZeroDivisionError 발생 시 코드
    print("ZeroDivide : " + str(e))
except Exception as e:  # 그 외 예외들 발생시, 마지막에 사용
    print("Exception : " + str(e))
