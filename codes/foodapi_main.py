# 프로토타입을 이용하여 이를 코드로 만들기

from bs4 import BeautifulSoup
import requests
# research_year = input("당신은 몇 년도에 조사한 것을 보여주고 싶습니까?")
# maker_name = input("당신은 어느 회사 음식이 궁금합니까?")
# desc_kor = input("당신은 품목 중 어떤 메뉴가 궁금합니까?")


food_url = "http://openapi.foodsafetykorea.go.kr/api/4d74d83cd263493aa1b6/I2790/xml/8001/9000"
response = requests.get(food_url)
soup = BeautifulSoup(response.text, "lxml")
print(soup)