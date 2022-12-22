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
            [1] (유) 대현물산 [2] (유) 돌코리아 [3] (유) 선한물산 [4] (주) 대두식품 [5] (주) 바로 [6] (주) 선인 [7] (주) 씨더블유인터내셔널 [8] (주) 지와이커머스 [9] (주) 청우식품 [10] (주) 195에프앤비 [11] (주) 7번가사람들 [12] (주) 가가대소 [13] (주) 가또케익 [14] (주) 가렛코리아 [15] (주) 가미엔 [16] (주) 가온누리코퍼레이션 [17] (주) 가주유통 [18] (주) 가토코 [19] (주) 감성베이크 [20] (주) 감자스위트 [21] (주) 개미식품 [22] (주) 건강마을 [23] (주) 건영비앤에프 [24] (주) 건영제과 [25] (주) 겐츠 베이커리 [26] (주) 겐츠 베이커리 제2공장 [27] (주) 고구려통상 [28] (주) 고궁 [29] (주) 고메베이글 [30] (주) 고메베이글제2공장 [31] (주) 고을 [32] (주)교토마블 [33] (주) 굿투베이크 [34] (주) 규리인터내셔날 [35] (주) 그녀의빵공장 [36] (주) 글로델 [37] (주) 글로벌와이케이 [38] (주) 글로빅 [39] (주) 금강비앤에프 [40] (주) 금촌베이커리 [41] (주) 금풍제과 [42] (주) 끄레몽에프엔비 [43] (주) 나투라스 [44] 남건푸드 [45] (주) 남원맛부각 [46] (주)내추럴푸드텍 [47] (주) 네이처텍 [48] (주) 네추럴에프앤피 [49] (주) 네추럴에프앤피 2공장 [50] (주) 네추럴웨이 [51] (주) 놀부명과 [52] (주) 농심 [53] (주) 농업법인쿱도우 [54] (주) 농업회사법인 구례삼촌 [55] (주) 뉴팜 [56] (주) 다담 [57] (주) 다옴베이크 [58] (주) 다우에프에스 [59] (주) 다인명가 [60] (주) 다인인터내셔널 [61] (주) 닥터브레드 [62] (주) 달미인 [63] (주) 대도F&D [64] (주) 대봉식품 [65] (주) 대산인터내셔널 [66] (주) 대산후드 [67] (주) 대영그로브 [68] (주) 대영그로브 [69] (주) 대영지에프 [70] (주)대웅 [71] (주) 대조에프앤비 [72] (주) 대화엠피 [73] (주) 더뉴토리 [74] (주) 더브라운베이커리 [75] (주) 더비 [76] (주) 더오엠글로벌 [77] (주) 더케이홀딩스 [78] (주) 더페이지원 [79] (주) 더하이 [80] (주) 동화 [81] (주) 동화씨앤에프 [82] (주) 두라푸드 [83] (주) 디스커버리코리아 [84] (주) 디앤푸드 [85] (주) 디에이치푸드농업회사법인 [86] (주)디엔비 [87] (주)디엔이스코리아 [88] (주)디저트앤 [89] (주)디저트키친 [90] (주)딤섬 [91] (주)떡파는 사람들 [92] (주) 뚜또 [93] (주)뜨리에 [94] (주)라붐팩토리 [95] (주)라온씨앤비 [96] (주)라이스플레이 [97] (주)래딕스글로비즈 [98] (주) 랜시 [99] (주) 레오글로벌 [100] (주) 레인메이커스트레이딩 \
            [101] (주)로뎀푸드 [102] (주)로만 [103] (주)루시카토 [104] (주)루시카토 제2공장 [105] (주)류충현약용버섯 [106] (주)리더스에프에스 [107] (주)마늘향기 [108] (주) 만천네이처푸드 [109] (주)맘모스제과 [110] (주) 맛고을식품 [111] (주) 메가마트 [112] (주) 메이드인제주 [113] (주) 명도물산 [114] (주) 명성식품 [115] (주) 명품정항우케익 [116] (주) 모노링크 [117] (주) 모닝듀에프엔비 [118] 모모 [119] (주) 몸과맘 [120] (주) 몽돌빵 [121] (주) 미누스토리 [122] (주) 미미미 [123] (주) 미송엔터프라이즈 [124] (주) 미진바이오 [125] (주) 미향약품 [126] (주) 밀갸또 [127] (주) 바람에프앤비 [128] (주) 바로군 [129] (주) 바른길 [130] (주) 바른유통 [131] (주) 바른푸드 [132] (주) 바오밥 [133] (주) 바이오로제트 [134] (주) 바이오믹스테크 [135] (주) 백두에프앤에스 [136] (주) 백두에프엠 [137] (주) 베비에르에프앤비(F&B) [138] (주) 베이글코리아 [139] (주) 베이크플러스 [140] (주) 벨리푸드 [141] (주) 보나비 [142] (주) 보나비 아티지움 [143] (주) 보라티알 [144] (주) 보람비티 [145] (주) 보부아이앤에프 [146] (주) 본비반트 [147] (주) 볼드인터내셔널 [148] (주) 브니엘월드 [149] (주) 브라운스토리 [150] (주) 브레드플랜트 [151] (주) 브레드필 [152] (주) 블랑제리코팡 [153] (주) 블루에프앤비 [154] (주) 비씨디클러스터 [155] (주) 비에스타 [156] (주) 비에이치델리 [157] (주) 비엔푸드 [158] (주) 비오팜 [159] (주) 비케이알코리아 [160] (주) 빙그레 [161] (주) 빨간화덕푸드 [162] (주) 빵명가 [163] (주) 사옹원 [164] (주) 산과들에 [165] (주) 살루스 [166] (주) 삼경물산 [167] (주) 삼경에프에스 [168] (주) 삼경프라자 [169] (주) 삼광식품 [170] (주) 삼아인터내셔날 [171] (주) 삼양사 [172] (주) 삼원트레이드 [173] (주) 삼진씨앤에프 [174] (주) 새로 [175] (주) 새롬식품 [176] (주) 새안글로벌 [177] (주) 샤니 [178] (주) 서래푸드 [179] (주) 서석앤에프 [180] (주) 서울제과 [181] (주) 서울쿠키컴퍼니 [182] (주) 서주 2공장 [183] (주) 서흥 [184] (주) 서흥 오송2공장 [185] (주) 선양평택공장 [186] (주) 선인 [187] (주) 성민에프에스 [188] (주) 성민에프에스 [189] (주) 성신비엔에프 [190] (주) 성신푸드 [191] (주) 성일무역 [192] (주) 성진에프에스 [193] (주) 성호제과 [194] (주) 세미원푸드 [195] (주) 세종바이오팜 [196] (주) 세종에브리푸드 [197] (주) 셀러스푸드 [198] (주) 소이빈델리 [199] (주) 솔루션푸드 [200] (주) 쇼콜라이삭 \
            [201] (주) 술이홀제과 [202] (주) 스위트코리아 [203] (주) 스위트필 [204] (주) 스윗니모코리아 [205] (주) 스칸딕 프라자 [206] (주) 스타드레이딩 [207] (주) 시그마인터내셔날 [208] (주) 신라명과 [209] (주) 신선에프앤브이 [210] (주) 신성티엔에프 [211] (주) 신세계푸드 [212] (주) 신세계푸드 김포공장 [213] (주) 신세계푸드 메인주방 [214] (주) 신세계공장 오산공장 [215] (주) 신세계공장 천안공장 [216] (주) 신우통상예 [217] (주)신화팝빌리지 [218] (주) 신흥물산 [219] (주) 신흥물산 2공장 [220] (주) 신흥식품 [221] (주) 쌀과자마을 [222] (주) 쌍인진천공장 [223] (주) 씨믹스 [224] (주) 씨알푸드 [225] (주) 씨앤미 [226] (주) 씨에스아이팩토리 [227] (주) 씨엔비위즈 [228] (주) 씨엔에스푸드시스템 [229] (주) 씨엔푸드 [230] (주) 씨지에스 에프앤비 [231] (주) 씨케이하우스 [232] (주) 아띠인터내셔널 [233] (주) 아람 [234] (주) 아리랑지에프 [235] (주) 아셀푸드 [236] (주) 아오스 [237] (주) 아우레이트 [238] (주) 아워홈 [239] (주) 아이배냇경포푸드 [240] (주) 아이이케이 [241] (주) 아이푸드넷 [242] (주) 아인츠푸드 [243] (주) 아인츠푸드 성남공장 [244] (주) 아프로푸드 [245] (주) 안스 [246] (주) 안신 [247] (주) 안흥밀바람푸드 [248] (주) 알찬식품 [249] (주) 알탠토 [250] (주) 앰브로스에이엠 [251] (주) 앰퍼샌드 [252] (주) 엄마사랑 [253] (주) 에그앤씨드 [254] (주) 에그앤씨드 진천공장 [255] (주) 에스델리 [256] (주) 에스디생명공학 건강식품사업부문 [257] (주) 에스디씨 [258] (주) 에스디씨2공장 [259] (주) 에스디푸드 [260] (주) 에스씨디글로벌 [261] (주) 에스씨케이통상 [262] (주) 에스씨코리아 [263] (주) 에스앤케이글로벌 [264] (주) 에스엘에스 [265] (주) 에스엠에스무역 [266] (주) 에스엠팜 [267] (주) 에스오엠 에프앤아이 [268] (주) 에스지글로벌 [269] (주) 에스트라  [270] (주) 에스파냐 [271] (주) 에이뷰 [272] (주) 에이비피홀딩스 [273] (주) 에이스엠앤티 [274] (주) 에이치디푸드 [275] (주) 에이치알엘 [276] (주) 에이치푸드 [277] (주) 에취알에스 [278] (주) 에코에프엔비 [279] (주) 에코제이푸드 [280] (주) 에프씨웍스 [281] (주) 에프앤지코리아 [282] (주) 엔에프에스 [283] (주) 엔제이 [284] (주) 엘가 [285] (주) 엘에프 푸드 [286] (주) 엘케이푸드 [287] (주) 엠디에스코리아 [288] (주) 엠에스씨(MSC) [289] (주) 엠케이푸드원 [290] (주) 여리수에프엔씨 [291] (주) 영남코프레이션 [292] (주) 영인코퍼레이션 [293] (주) 오뗄 이천지점 [294] (주) 오리온 제2익산공장 [295] (주) 오리온 제3익산공장 [296] (주) 오리온 제5청주공장 [297] (주) 오리온제4청주공장 [298] (주) 오성물산코리아 [299] (주) 오손도손 [300] (주) 오에스아이무역 \
            [301] (주) 오페라베이커리 [302] (주) 오행생식 [303] (주) 옥두식품 [304] (주) 온맘푸드 [305] (주) 옵스 [306] (주) 와이디에스 [307] (주) 와이앤비푸드농업회사법인 [308] (주) 와이엔씨 [309] (주) 우나트라 [310] (주) 우농 [311] (주) 우래식품 [312] (주) 우리식품 [313] (주) 우말인터프라이시스 [314] (주) 우양 [315] (주) 우양(청양공장) [316] (주) 원일바이오 [317] (주) 월드푸드 [318] (주) 웰팜코리아 [319] (주) 위아더월드 [320] (주) 위앤코리아 [321] (주) 유기농산 [322] (주) 유니온트리 [323] (주) 유담 [324] (주) 유로베이크 [325] (주) 유비콘스 [326] (주) 유스마일 [327] (주) 유앤아이엔젤스 [328] (주) 유유헬스케어 [329] (주) 이대명과 [330] (주) 이델리에프씨 [331] (주) 이랜드이츠 가산월드점 [332] (주) 이레우리밀 [333] (주) 이로운베이커리 [334] (주) 이마트 [335] (주) 이성당 서수공장 [336] (주) 이앤엘푸드 [337] (주) 이엔아이 에프앤비 [338] (주) 인클루시브 인터내셔널 [339] (주) 인터웰푸드시스템 [340] (주) 일성씨엠에스 [341] (주) 일신국제무역 [342] (주) 일영피엔씨 [343] (주) 임실치즈에프엔비 [344] (주) 자은도 [345] (주) 자이언트 [346] (주) 자인 [347] (주) 자임에프앤비 [348] (주) 재호식품 [349] (주) 전주제과 [350] (주) 제원인터내쇼날 [351] (주) 제이디코리아 [352] (주) 제이앤비식품 본사공장 [353] (주) 제이앤이 아산공장 [354] (주) 제이에프앤비플러스 [355] (주) 제이케이글로벌 [356] (주) 제일훼밀리 [357] (주) 젠푸드 [358] (주) 조이푸드 [359] (주) 중원명가유통 [360] (주) 쥬비스푸드 [361] (주) 지바이알 [362] (주) 지앤원 [363] (주) 지에스바이오 [364] (주) 지에프에스인터내셔널 [365] (주) 지우코포레이션 [366] (주) 지웰 [367] (주) 지이디통상 [368] (주) 지지푸드 [369] (주) 진더스 [370] (주) 진성앤푸드원 [371] (주) 진우식품 [372] (주) 참맛 [373] (주) 천년애푸드 [374] (주) 천하코퍼레이션 [375] (주) 청담식품 [376] (주) 청아냉동식품 [377] (주) 청아냉동식품 제2공장 [378] (주) 청아식품 [379] (주) 청우식품 [380] (주) 초코사이버 [381] (주) 초코텍 [382] (주) 최고유통 [383] (주) 캐니스 [384] (주) 커피빈푸드 [385] (주) 케이비엠푸드 [386] (주) 케이씨크린트래이딩 [387] (주) 케이지앤에프 [388] (주) 코레드 인터내쇼날 [389] (주) 코롬방제과 [390] (주) 코리아헬스바이오 [391] (주) 코스모스 [392] (주) 코스모스제과 [393] (주) 코스트코코리아 [394] (주) 코이스라 [395] (주) 코타서비스 [396] (주) 콤비타코리아 [397] (주) 쿠키아 [398] (주) 쿡앤조이인터내셔널 [399] (주) 큐케이씨 \
            [400] (주) 크라운제과 [401] (주) 크라운제과 아산공장 [402] (주) 크라운제과진천공장 [403] (주) 크래프트하인즈코리아 [404] (주) 크리에잇하우스 [405] (주) 키즈웰 [406] (주) 타르틴코리아 [407] (주) 탐라식품 [408] (주) 탑포인트인터내셔널 [409] (주) 태광웰푸드 [410] (주) 태향 [411] (주) 테이트 제2공장 [412] (주) 토탈에프앤비 [413] (주) 톰볼라 [414] (주) 투데이 [415] (주) 트라이콤무역 [416] (주) 티비엠 [417] (주) 티엔농산 [418] (주) 티엔푸드 3공장 [419] (주) 티엠지홀딩스 [420] SHINKINEDO GROUP INC [421] (주) 티엠지홀딩스 [422] (주) 파리크라상 [423] (주) 파리크라상 신공장 [424] (주) 파리크라상인천CK [425] (주) 파리크라상제주공장 [426] (주) 파미유 [427] (주) 파코트레이딩 [428] (주) 파티시에 김영모 [429] (주) 팜크로스 [430] (주) 팜팩토리스푼베이커리 [431] (주) 팡마니 [432] (주) 퍼시머너리 [433] (주) 페이퍼플랜 성남공장 [434] (주) 포비브라이트 을지로점 [435] (주) 푸드빌 [436] (주) 푸드코아 [437] (주) 푸디스 [438] (주) 풀만 [439] (주) 풍년제과본사(제1공장) [440] (주) 풍년제과본사제2공장 [441] (주) 풍림푸드 ")             # 회사 이름 선택하기
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