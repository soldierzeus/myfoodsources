# 프로토타입을 이용하여 이를 코드로 만들기

# BeautifulSoup, request 모듈을 이용해서 데이터 xml원본 추출하기
from bs4 import BeautifulSoup
import requests

# 식품영양성분분석 장치를 실행시키는 동시에 사람들이 원하는 선택항목 보여주기
print("안녕하세요, 식품영양성분을 분석해주는 장치입니다!")
research_year = input("당신은 몇 년도에 조사한 것을 보여주고 싶습니까?")    # 조사한 년도 추출하기
product = int(input("당신이 알고 싶은 식품들 중 무엇을 알고 싶습니까? \
[1] 농.축산물	[2] 수산물	[3] 가공식품	[4] 음식"))                      # 식품 항목 선택하기

if product == 3:
    group_name1 = int(input("가공식품중 어떤 종류의 식품을 원합니까? \
        [1] 과자류, 빵류 또는 떡류 [2] 농산가공식품류 [3] 당류 [4] 동물성가공식품류 [5] 두부류 또는 묵류 \
        [6] 면류 [7] 벌꿀 및 화분가공품류 [8] 빙과류 [9] 수산가공식품류 [10] 식용유지류 [11] 식육가공품 및 포장육 \
        [12] 알가공품류 [13] 유가공품 [14] 음료류 [15] 장기보존식품 [16] 장류 [17] 잼류 [18] 절임류 또는 조림류 [19] 조미식품 \
        [20] 주류 [21] 코코아가공품류 또는 초콜릿류 [22] 특수용도식품 [23] 기타식품류"))
    if group_name1 == 1:
        maker_name = input("어느 과자 음식 회사를 고르고 싶습니까? \
            [1] 엔에프에스 [2] 산골농장 [3] 남향푸드또띠아 [4] 라이스비 [5] 명품정항우케잌 \
            [6] ")             # 회사 이름 선택하기
    elif group_name1 == 2:
        
    elif group_name1 == 3:
        
    elif group_name1 == 4:
        
    elif group_name1 == 5:
        
    elif group_name1 == 6:
        
    elif group_name1 == 7:
        



desc_kor = input("당신은 품목 중 어떤 메뉴가 궁금합니까?")


food_url = "http://openapi.foodsafetykorea.go.kr/api/4d74d83cd263493aa1b6/I2790/xml/8001/9000"
response = requests.get(food_url)
soup = BeautifulSoup(response.text, "lxml")
print(soup)