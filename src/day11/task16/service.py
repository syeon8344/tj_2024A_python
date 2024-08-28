# day11 > task16 > service.py
# import
from bs4 import BeautifulSoup
import pandas as pd
import json
from urllib import request

# 2. 경력별 공고수 등록 및 숫자 계산
per_experience = []  # 경력 이름들
number_experience = []  # 각 경력 이름들의 인덱스에 맞게 숫자 증가
# 2. 학력별 공고수 등록 및 숫자 계산
per_education = [] # 학력별 이름들
number_education = [] # 각 경력 이름들의 인덱스에 맞게 숫자 증가


def get_jobkorea(keyword):
    print("get_jobkorea")
    result = []
    for page in range(1, 6):  # page = 1 ~ 189
        print("page", page)
        if keyword == "":
            url = f"https://www.jobkorea.co.kr/Search/?stext=java&tabType=recruit&Page_No={page}"
        else:
            url = f"https://www.jobkorea.co.kr/Search/?stext={keyword}&tabType=recruit&Page_No={page}"
        print(url)
        '''
            회사명: <article class="list"> -> <div class="list-section-corp"> -> <a>
            공고명:
            경력 
            학력 
            계약유형 
            지역
            채용기간
        '''
        resp = request.urlopen(url)
        if resp.getcode() == 200:
            print("200")
            corp_names = []
            article_names = []
            experiences = []
            educations = []
            work_types = []
            regions = []
            times = []
            soup = BeautifulSoup(resp.read(), "html.parser")
            corp_name = soup.select(".list > article > div > a")  # 회사명
            print(corp_name)
            for corp in corp_name:
                corp_names.append(corp.string.strip())
                print(corp_names)
            article_name = soup.select(".information-title > a")  # 공고명
            for name in article_name:
                article_names.append(name.text.strip().replace("\"", ""))
            information = soup.select(".chip-information-group")

            for info in information[:20]:  # 레코드 하나의 <li>들
                print(info)
                lis = []
                for li in info.select("li"):
                    lis.append(li.string.strip())
                if len(lis) < 5:
                    processed_experience = info.select("li")[0].string.strip()
                    experiences.append(processed_experience)
                    if processed_experience not in per_experience:
                        per_experience.append(processed_experience)
                        number_experience.append(1)
                    else:
                        number_experience[per_experience.index(processed_experience)] += 1
                    educations.append(".")
                    work_types.append(info.select("li")[1].string.strip())
                    regions.append(info.select("li")[2].string.strip())
                    times.append(info.select("li")[3].string.strip())
                else:
                    processed_experience = info.select("li")[0].string.strip()
                    experiences.append(processed_experience)
                    if processed_experience not in per_experience:
                        per_experience.append(processed_experience)
                        number_experience.append(1)
                    else:
                        number_experience[per_experience.index(processed_experience)] += 1
                    processed_education = info.select("li")[1].string.strip()
                    educations.append(processed_education)
                    if processed_education not in per_education:
                        per_education.append(processed_education)
                        number_education.append(1)
                    else:
                        number_education[per_education.index(processed_education)] += 1

                    work_types.append(info.select("li")[2].string.strip())
                    regions.append(info.select("li")[3].string.strip())
                    times.append(info.select("li")[4].string.strip())
            # zip() 함수로 페이지당 검색된 항목들을 인덱스마다 튜플로 묶는다
            page_tuples = list(zip(corp_names, article_names, experiences, educations, work_types, regions, times))
            for record in page_tuples:  # 각 튜플을 딕셔너리로 변환해서 최종 결과 리스트에 넣는다.
                row = {"corp_name": record[0], "article_name": record[1], "experience": record[2],
                       "education": record[3], "work_type": record[4], "region": record[5], "time": record[6]}
                result.append(row)
            print(page)
        else:
            print("error")
    return result


def list_to_csv(result):
    df = pd.DataFrame(result)
    df.columns = ["회사명", "공고명", "경력", "학력", "계약유형", "지역", "채용기간"]
    print(df)
    df.to_csv("잡코리아검색기록.csv", encoding="utf-8", mode="w")
    return True


def read_csv(file_name):
    df = pd.read_csv(f"{file_name}.csv", encoding="utf-8", engine="python", index_col=0)
    json_result = df.to_json(orient="records", force_ascii=False)
    result_json = json.loads(json_result)

    return result_json


def get_education_stats():
    education_dict = []

    education_stat = list(zip(per_education, number_education))
    for stat in education_stat:
        education_dict.append({"name": stat[0], "number": stat[1]})

    return education_dict


def get_experience_stats():
    experience_dict = []

    experience_stat = list(zip(per_experience, number_experience))
    for stat in experience_stat:
        experience_dict.append({"name": stat[0], "number": stat[1]})

    return experience_dict


if __name__ == "__main__":
    # list_to_csv(get_jobkorea())
    print(get_jobkorea())