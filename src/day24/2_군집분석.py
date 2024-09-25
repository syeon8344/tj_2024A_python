# day24 > 2_군집분석.py
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples
from sklearn.preprocessing import StandardScaler
# [1] 데이터 수집
# https://archive.ics.uci.edu/dataset/352/online+retail 에서 Online Retail.xlsx -> Online_Retail.xlsx
# df_retail = pd.read_excel("UCI_online_retail/Online_Retail.xlsx")
# df_retail.to_csv("UCI_online_retail/Online_Retail.csv")  # 빠른 읽기속도를 위해 csv로 변환 후 읽어들임
df_retail = pd.read_csv("UCI_online_retail/Online_Retail.csv")
# print(df_retail.head())
# print(df_retail.info())
"""
RangeIndex: 541909 entries, 0 to 541908
Data columns (total 8 columns):
 #   Column       Non-Null Count   Dtype         
---  ------       --------------   -----         
 0   InvoiceNo    541909 non-null  object        
 1   StockCode    541909 non-null  object        
 2   Description  540455 non-null  object        
 3   Quantity     541909 non-null  int64         
 4   InvoiceDate  541909 non-null  datetime64[ns]
 5   UnitPrice    541909 non-null  float64       
 6   CustomerID   406829 non-null  float64       
 7   Country      541909 non-null  object        
dtypes: datetime64[ns](1), float64(2), int64(1), object(4)
"""
# [2] 데이터 정제
# CustomerID를 정수형으로, Quantity 또는 UnitPrice가 음수인 행들과 CustomerID가 없는 행들 제외
# 1. 오류 데이터 정제
df_retail = df_retail[df_retail["Quantity"] > 0]
df_retail = df_retail[df_retail["UnitPrice"] > 0]
df_retail = df_retail[df_retail["CustomerID"].notnull()]
# 2. 자료형 변환
df_retail["CustomerID"] = df_retail["CustomerID"].astype(int)
# print(df_retail.info())
# print(df_retail.isnull().sum())
# print(df_retail.shape)  # (397884, 8)
# 3. 중복값 제거
df_retail.drop_duplicates(inplace=True)
# print(df_retail.shape)  # 중복값 제외된 수치 (392692, 8)
# 4. 분석 DataFrame 생성 및 확인
df_value_counts = pd.DataFrame([{"Product": len(df_retail["StockCode"].value_counts()),
                                 "Transaction": len(df_retail["InvoiceNo"].value_counts()),
                                 "Customer": len(df_retail["CustomerID"].value_counts())}], index=["counts"])
# print(df_value_counts)
"""
        Product  Transaction  Customer
counts     3665        18532      4338
"""
# print(df_retail["Country"].value_counts())  # 고객 국적 확인
# 5. 주문 금액 칼럼 추가
df_retail["SaleAmount"] = df_retail["UnitPrice"] * df_retail["Quantity"]
print(df_retail.head())  # 작업된 DF 확인
# 6. CustomerID로 묶어 열 조건에 맞춰 df_customer 생성
# df_customer 생성시 옵션
aggregations = {
    "InvoiceNo": "count",  # 주문번호는 count
    "SaleAmount": "sum",  # 총 금액
    "InvoiceDate": "max"  # 제일 최근 주문날짜
}
df_customer = df_retail.groupby("CustomerID").agg(aggregations)
df_customer.rename(columns={"InvoiceNo": "Freq", "InvoiceDate": "ElapsedDays"}, inplace=True)
print(df_customer.head())  # 생성된 DF 확인
# 7. 마지막 주문 후 지난 날짜 데이터 생성
df_customer["ElapsedDays"] = datetime.datetime(2011, 12, 10) - pd.to_datetime(df_customer["ElapsedDays"])
df_customer["ElapsedDays"] = df_customer["ElapsedDays"].dt.days + 1
print(df_customer.head())  # ElapsedDays 생성된 DF 확인
# 8. 데이터 분포 확인
fig, ax = plt.subplots()
ax.boxplot([df_customer["Freq"], df_customer["SaleAmount"], df_customer["ElapsedDays"]], sym="bo")
plt.xticks([1, 2, 3], ["Freq", "SaleAmount", "ElapsedDays"])
plt.show()
# 9. 로그 함수 적용으로 데이터 분포 조정
df_customer["Freq_log"] = np.log1p(df_customer["Freq"])
df_customer["SaleAmount_log"] = np.log1p(df_customer["SaleAmount"])
df_customer["ElapsedDays_log"] = np.log1p(df_customer["ElapsedDays"])
print(df_customer.head())
fig, ax = plt.subplots()
ax.boxplot([df_customer["Freq_log"], df_customer["SaleAmount_log"], df_customer["ElapsedDays_log"]], sym="bo")
plt.xticks([1, 2, 3], ["Freq_log", "SaleAmount_log", "ElapsedDays_log"])
plt.show()

# [3] 분석 모델 구축
# 1. 정규분포 스케일된 x_features
scaler = StandardScaler()
x_features = df_customer[["Freq_log", "SaleAmount_log", "ElapsedDays_log"]].values
x_features_scaled = scaler.fit_transform(x_features)
# 엘보 방법으로 클러스터 개수 K 구하기
distortions = []
for i in range(1, 11):
    kmeans_i = KMeans(n_clusters=i, random_state=777)
    kmeans_i.fit(x_features_scaled)
    distortions.append(kmeans_i.inertia_)
plt.plot(range(1, 11), distortions, marker="o")
plt.xlabel("Number of clusters")
plt.ylabel("Distortion")
plt.show()  # k 후보군: 3, 4, 5

# 2. 위에서 구한 K 클러스터 값으로 모델 생성
kmeans = KMeans(n_clusters=3, random_state=777)
# 모델 학습 및 결과
y_labels = kmeans.fit_predict(x_features_scaled)
df_customer["Cluster"] = y_labels
print(df_customer.head())