# day12 > 1_selenium.py
# 1. 모듈 가져오기
# from selenium에 느낌표로 또는 설정 - 프로젝트 - 인터프리터 - + 버튼에서 검색
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd

def coffeebean_store(result):
    # 2. webdriver 객체 생성
    wd = webdriver.Chrome()

    # 3. webdriver 객체를 이용한 웹페이지 접속, .get(URL)
    # wd.get("http://hanbit.co.kr")

    # 실습: 커피빈 매장 정보(동적페이지=JS이벤트) zmfhffld
    # 1. 커피빈 웹페이지 연결
    cb_url = "https://www.coffeebeankorea.com/store/store.asp"
    for i in range(1, 20):
        wd.get(cb_url)
        time.sleep(1)
        try:
            # 2. 커피빈 웹페이지의 자바스크립트 함수 호출: .execute_script("JS함수호출")
            wd.execute_script(f"storePop2('{i}')")  # i번 매장
            time.sleep(2)
            # 3. JS 함수가 수행된 페이지의 소스 코드를 저장
            html = wd.page_source
            # 4. BeautifulSoup 객체 생성


            soupCB1 = BeautifulSoup(html, "html.parser")
            # 5. HTML 소스 코드 확인
            print(soupCB1.prettify())

            # 6. 특정 매장 정보 모달창에서 매장 정보 파싱하기
            # 6-1. 매장 지점명
            store_name_h2 = soupCB1.select('div.store_txt > h2')
            print(store_name_h2)  # [<h2>삼성봉은사거리점</h2>]
            store_name = store_name_h2[0].string
            print(store_name)  # 삼성봉은사거리점

            # 6-2 매장 주소
            store_info = soupCB1.select('div.store_txt > table.store_table > tbody > tr > td ')
            print(store_info)
            # [<td> 평일 07:00-22:30 | 주말/공휴일 07:00-22:00</td>, <td>건물뒷편주차장(기계주차식)<br/>평일 최초 30분 2,000원 / 1시간 5,000원 (구매영수증 지참시 30분 2,000원 / 1시간 3,500원)<br/>1시간 초과시 10분당 1,000원 (평일,주말 동일)</td>, <td>서울시 강남구 영동대로 607 1,2층  <!--span class="lot">(서울시 강남구 영동대로 607 1,2층)</span--></td>, <td>02-3443-5618</td>, <td class="best">식약처 인증 위생등급 매우 우수매장</td>, <td class="hallcake">홀케익 당일 수령가능</td>]
            store_address_list = list(store_info[2])
            print(store_address_list)
            # ['서울시 강남구 영동대로 607 1,2층  ', 'span class="lot">(서울시 강남구 영동대로 607 1,2층)</span']
            store_address = store_address_list[0].strip()
            print(store_address)  # 서울시 강남구 영동대로 607 1,2층

            # 6-3 매장 전화번호
            store_phone = store_info[3].string
            print(store_phone)  # 02-3443-5618

            result.append({"name": store_name, "address": store_address, "contact": store_phone})
        except Exception as e:
            print(e)
    return result


def main():
    result = []
    coffeebean_store(result)
    print(result)
    # pandas로 2차원 리스트를 데이터프레임 객체로 생성
    df = pd.DataFrame(result)
    # 데이터프레임 객체를 CSV 파일로 저장
    df.to_csv("csv/커피빈매장목록.csv", mode='w', encoding='utf-8', index=True)

if __name__ == "__main__":
    main()
