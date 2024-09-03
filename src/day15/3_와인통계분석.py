# day15 > 3_와인통계분석.py
# 목표: 와인 속성을 분석하여 품질 등급을 예측하기
import pandas as pd

# [1] 데이터 수집: winequality-red.csv & winequality-white.csv

# [2] 데이터 준비
# [2-1] csv 파일의 열 구분자를 ;에서 ,로 바꾸기

# read_csv 속성에서 구분자 설정하기: sep="구분자" 기본값은 ","
# header=숫자: 숫자 행을 열 이름으로 지정, 기본값은 0
red_df = pd.read_csv("csv/winequality-red.csv", sep=";", engine="python", header=0)
white_df = pd.read_csv("csv/winequality-white.csv", sep=";", engine="python", header=0)
print(red_df)
print(white_df)
red_df.to_csv("csv/red_wine_quality.csv", mode='w', index=False)
white_df.to_csv("csv/white_wine_quality.csv", mode='w', index=False)

# [2-2] 데이터 병합하기: 레드와인과 화이트와인의 데이터
print(red_df.head())  # .head(): 데이터프레임 위에서부터 5개 행 출력
# 1. 열 추가: 0번째(첫번째) 열에 type 열 이름으로 red 값들을 추가
red_df.insert(0, column='type', value="red")
print(red_df.head())
print(red_df.shape)  # .shape: 행의 갯수와 열의 개수 (1599, 13), .shape[0]: 행 개수, .shape[1]: 열 개수
# 2.
print(white_df.head())
white_df.insert(0, column='type', value="white")
print(white_df.shape)  # (4898, 13)
# 3. 데이터프레임 합치기: pd.concat([Df1, Df2])
wine = pd.concat([red_df, white_df])
print(wine.shape)
# 4. 합친 와인 데이터프레임을 CSV로 저장
wine.to_csv("csv/wine.csv", index=False)

# [3] 데이터 탐색
# 1. 데이터프레임 기본 정보 출력
print(wine.info())
# 2. 기술 통계
wine.columns = wine.columns.str.replace(" ", "_")  # 열 이름의 공백을 _로 치환
print(wine.head())
# 기술 통계 표시: .describe() = count, mean, std표준편차, min, 25%백분율, 50%, 75%, max
print(wine.describe())
print(wine.describe()['quality'])  # 와인의 등급 통계
print(wine.describe()['quality'].round(5).to_list())  # 와인 등급의 통계 계산결과 리스트

print(wine['quality'].unique())  # [5 6 7 4 8 3 9]
print(wine.quality.unique())  # [5 6 7 4 8 3 9]  -> 레이블명에 특수문자가 있으면 대괄호 + 따옴표 버전 사용 필요.
print(sorted(wine.quality.unique()))  # 와인 등급의 중복값 제거 후 정렬 [3 4 5 6 7 8 9]

print(wine['quality'].value_counts())  # 특정 열 기준으로 count한 결과를 Series로 반환
print(wine.quality.value_counts().to_json())  # {"6":2836,"5":2138,"7":1079,"4":216,"8":193,"3":30,"9":5}, 등급 점수: 갯수
# [4] 데이터 모델링
# 1. .groupby('기준 그릅 열이름')['속성명']
# type 속성으로 그룹해  quality 속성의 기술 통계 구하기
print(wine.groupby('type')['quality'].describe())
# 2. type 속성으로 그룹해서  quality 속성의 평균
print(wine.groupby('type')['quality'].mean())
# 2. type 속성으로 그룹해서  quality 속성의의 표준편차
print(wine.groupby('type')['quality'].std())
# 2. type 속성으로 그룹해서  quality 평균, 표준편차
print(wine.groupby('type')['quality'].agg(['mean', 'std']))

#####################################################################

# [1] t-test
# 원인변수(독립변수): 레드와인, 화이트와인 (명목형 변수)
# 결과변수(종속변수): quality(등급), (연속형 변수)

# 1. 모듈 호출
from scipy import stats

# 2. 두 집단 표본 만들기
# wine = pandas DataFrame, .loc[조건, 출력할 열]
# print(wine.loc[wine['type'] == 'red', 'quality'])
# type열의 값이 red인 행의 quality
레드와인등급 = wine.loc[wine['type'] == 'red', 'quality']
화이트와인등급 = wine.loc[wine['type'] == 'white', 'quality']

# 3. t-test
t_score, p_value = stats.ttest_ind(레드와인등급, 화이트와인등급, equal_var=False)
print(t_score)  # -10.149363059143164: 두번째 집단 평균이 높다, 평균적으로 10.14 차이
print(p_value)  # 8.168348870049682e-24: e-숫자 -> 소수 부분 자릿수
if t_score < 0.05:
    print("해당 가설은 유의미하다")
else:
    print("해당 가설은 무의미하다")

# [2] 회귀 분석 (다중 선형 회귀분석)
# 1. 모듈 호출
from statsmodels.formula.api import ols, glm
# 2. 회귀모형수식(독립변수, 종속변수를 구성하는 방식/공식: 종속변수명 ~ 독립변수1 + 독립변수2...)
# 종속변수(등급): 연속성, 독립변수(나머지 변수): 연속성
regression_formula = "quality ~ fixed_acidity + volatile_acidity + citric_acid + residual_sugar + chlorides + free_sulfur_dioxide + total_sulfur_dioxide + density + pH + sulphates + alcohol"
# 3. ols(선형 회귀 모델): ols(회귀모형수식, data=표본),
# ols: Ordinary Least Squares최소 제곱법: 근사적으로 구하려는 해와 실제 해의 오차의 제곱의 합이 최소가 되는 해를 구하는 방법
# .fit()으로 완성된 선형회귀모델 ols()을 실행해서 변수에 저장
regression_result = ols(regression_formula, data=wine).fit()
print(regression_result.summary())

"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                quality   R-squared:                       0.292
Model:                            OLS   Adj. R-squared:                  0.291
Method:                 Least Squares   F-statistic:                     243.3
Date:                Tue, 03 Sep 2024   Prob (F-statistic):               0.00
Time:                        12:53:14   Log-Likelihood:                -7215.5
No. Observations:                6497   AIC:                         1.445e+04
Df Residuals:                    6485   BIC:                         1.454e+04
Df Model:                          11                                         
Covariance Type:            nonrobust                                         
========================================================================================
                           coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------------
Intercept*              55.7627     11.894      4.688      0.000      32.447      79.079
fixed_acidity(독립변수)   0.0677      0.016      4.346      0.000       0.037       0.098
volatile_acidity        -1.3279      0.077    -17.162      0.000      -1.480      -1.176
citric_acid             -0.1097      0.080     -1.377      0.168      -0.266       0.046
residual_sugar           0.0436      0.005      8.449      0.000       0.033       0.054
chlorides               -0.4837      0.333     -1.454      0.146      -1.136       0.168
free_sulfur_dioxide      0.0060      0.001      7.948      0.000       0.004       0.007
total_sulfur_dioxide    -0.0025      0.000     -8.969      0.000      -0.003      -0.002
density                -54.9669     12.137     -4.529      0.000     -78.760     -31.173
pH                       0.4393      0.090      4.861      0.000       0.262       0.616
sulphates                0.7683      0.076     10.092      0.000       0.619       0.917
alcohol                  0.2670      0.017     15.963      0.000       0.234       0.300
==============================================================================
Omnibus:                      144.075   Durbin-Watson:                   1.646
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              324.712
Skew:                          -0.006   Prob(JB):                     3.09e-71
Kurtosis:                       4.095   Cond. No.                     2.49e+05
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.49e+05. This might indicate that there are
strong multicollinearity or other numerical problems.

* Intercept: 절편, (모든) 독립변수가 0일때 종속변수의 예측값 (X=0일때 Y 예측값)
                           coef    std err          t      P>|t|      [0.025      0.975]
alcohol                  0.2670      0.017     15.963      0.000       0.234       0.300

- coef: 회귀계수 coefficient, 알콜(iv)과 등급(dv) 관계 해석: # 알콜이 1단위 증가할때마다 등급이 0.267 증가한다는 예측
- std err: 표준 오차
- t: t테스트 통계량
- P>|t|: t테스트 p값, 0.05 미만이므로 검증 효과가 있다
- [0.025    0.975]: 앞 뒤 2.5%를 버리고 사이에 존재하면 신뢰할 수 있는 구간
"""
