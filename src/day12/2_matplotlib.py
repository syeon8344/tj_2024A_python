# day12 > 2_matplotlib.py
# matplotlib: 파이썬에서 데이터를 시각화해주는 패키지
# 데이터 분석결과를 시각화하여 직관적으로 이해하기 위해 사용
# 선 차트, 원형 차트, 바 차트, 히스토그램, 산점도 등등 지원

# [1] 모듈 가져오기
# import matplotlib에 느낌표로 또는 설정 - 프로젝트 - 인터프리터 - + 버튼에서 검색
# 또는 터미널에서 pip install matplotlib
import matplotlib

# [2] matplotlib 버전 확인
print(matplotlib.__version__)  # 3.9.2

# [3] pyplot 모듈 가져오기
import matplotlib.pyplot as plt


# [4] 라인 플롯 차트
# 1. 차트에 표시할 데이터 샘플 준비
x = [2016, 2017, 2018, 2019, 2020]
y = [350, 410, 520, 695, 543]

# 2. 라인플롯(선 차트)에 x축, y축 지정해서 라인플롯 생성
plt.plot(x, y)
# 3. 차트 제목 지정: .title("타이틀명")
plt.title('Annual Sales')
# 4. x축 레이블(가로축 제목) 설정: .xlabel("이름")
plt.xlabel('year')
# 5. y축 레이블(세로축 제목) 설정: .ylabel("이름")
plt.ylabel('sales')
# 6. 차트 실행
plt.show()

# [5] 바 차트
# 1. 샘플 데이터
y1 = [350, 410, 520, 695]
y2 = [200, 250, 385, 350]
x = range(len(y1))  # 0 ~ y1리스트의 길이만큼
# 2. x축, y축을 지정해서 바 차트 생성, width: 바 너비, color: 색상, bottom: 이중 바 그래프일 때 아래 값
plt.bar(x, y1, width=0.7, color="blue")
plt.bar(x, y2, width=0.7, color='red', bottom=y1)
# 3. 차트 제목
plt.title('Quarterly Sales')
# 4. x축 레이블
plt.xlabel('Quarters')
# 5. y축 레이블
plt.ylabel('sales')
# 6. 눈금 이름 리스트 생성
xlabels = ['first', 'second', 'third', 'fourth']
plt.xticks(x, xlabels, fontsize=10)  # x축 눈금 옵션
# 7. 범례(막대 구분 이름 표시)
plt.legend(['chairs', 'desks'])
# 8. 차트표시
plt.show()

# [6] 산점도: x축과 y축의 값 관계를 시각화, 각 데이터의 두 변수의 값을 x축, y축에 대응시켜 점으로 표현
# 1. 데이터
import random
x = [random.random() for i in range(100)]  # 50개의 요소를 난수(0~1)로 생성하여 리스트 생성
print(x)
y = [random.random() for i in range(100)]  # 50개의 요소를 난수(0~1)로 생성하여 리스트 생성
print(y)
# 2. 산점도 차트 생성
plt.scatter(x, y)
# 3. 차트 표현
plt.show()