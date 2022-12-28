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
            [1] (유) 대현물산 [2] (유) 돌코리아 [3] (유) 선한물산 [4] (주) 대두식품 [5] (주) 바로 [6] (주) 선인 [7] (주) 씨더블유인터내셔널 [8] (주) 지와이커머스 [9] (주) 청우식품 [10] (주) 195에프앤비 [11] (주) 7번가사람들 [12] (주) 가가대소 [13] (주) 가또케익 [14] (주) 가렛코리아 [15] (주) 가미엔 [16] (주) 가온누리코퍼레이션 [17] (주) 가주유통 [18] (주) 가토코 [19] (주) 감성베이크 [20] (주) 감자스위트 [21] (주) 개미식품 [22] (주) 건강마을 [23] (주) 건영비앤에프 [24] (주) 건영제과 [25] (주) 겐츠 베이커리 [26] (주) 겐츠 베이커리 제2공장 [27] (주) 고구려통상 [28] (주) 고궁 [29] (주) 고메베이글 [30] (주) 고메베이글제2공장 [31] (주) 고을 [32] (주)교토마블 [33] (주) 굿투베이크 [34] (주) 규리인터내셔날 [35] (주) 그녀의빵공장 [36] (주) 글로델 [37] (주) 글로벌와이케이 [38] (주) 글로빅 [39] (주) 금강비앤에프 [40] (주) 금촌베이커리 [41] (주) 금풍제과 [42] (주) 끄레몽에프엔비 [43] (주) 나투라스 [44] 남건푸드 [45] (주) 남원맛부각 [46] (주)내추럴푸드텍 [47] (주) 네이처텍 [48] (주) 네추럴에프앤피 [49] (주) 네추럴에프앤피 2공장 [50] (주) 네추럴웨이 [51] (주) 놀부명과 [52] (주) 농심 [53] (주) 농업법인쿱도우 [54] (주) 농업회사법인 구례삼촌 [55] (주) 뉴팜 [56] (주) 다담 [57] (주) 다옴베이크 [58] (주) 다우에프에스 [59] (주) 다인명가 [60] (주) 다인인터내셔널 [61] (주) 닥터브레드 [62] (주) 달미인 [63] (주) 대도F&D [64] (주) 대봉식품 [65] (주) 대산인터내셔널 [66] (주) 대산후드 [67] (주) 대영그로브 [68] (주) 대영그로브 [69] (주) 대영지에프 [70] (주)대웅 [71] (주) 대조에프앤비 [72] (주) 대화엠피 [73] (주) 더뉴토리 [74] (주) 더브라운베이커리 [75] (주) 더비 [76] (주) 더오엠글로벌 [77] (주) 더케이홀딩스 [78] (주) 더페이지원 [79] (주) 더하이 [80] (주) 동화 [81] (주) 동화씨앤에프 [82] (주) 두라푸드 [83] (주) 디스커버리코리아 [84] (주) 디앤푸드 [85] (주) 디에이치푸드농업회사법인 [86] (주) 디엔비 [87] (주) 디엔이스코리아 [88] (주) 디저트앤 [89] (주) 디저트키친 [90] (주)딤섬 [91] (주) 떡파는 사람들 [92] (주) 뚜또 [93] (주) 뜨리에 [94] (주) 라붐팩토리 [95] (주)라온씨앤비 [96] (주)라이스플레이 [97] (주)래딕스글로비즈 [98] (주) 랜시 [99] (주) 레오글로벌 [100] (주) 레인메이커스트레이딩 [101] (주) 로뎀푸드 [102] (주) 로만 [103] (주) 루시카토 [104] (주) 루시카토 제2공장 [105] (주) 류충현약용버섯 [106] (주)리더스에프에스 [107] (주)마늘향기 [108] (주) 만천네이처푸드 [109] (주) 맘모스제과 [110] (주) 맛고을식품 [111] (주) 메가마트 [112] (주) 메이드인제주 [113] (주) 명도물산 [114] (주) 명성식품 [115] (주) 명품정항우케익 [116] (주) 모노링크 [117] (주) 모닝듀에프엔비 [118] 모모 [119] (주) 몸과맘 [120] (주) 몽돌빵 [121] (주) 미누스토리 [122] (주) 미미미 [123] (주) 미송엔터프라이즈 [124] (주) 미진바이오 [125] (주) 미향약품 [126] (주) 밀갸또 [127] (주) 바람에프앤비 [128] (주) 바로군 [129] (주) 바른길 [130] (주) 바른유통 [131] (주) 바른푸드 [132] (주) 바오밥 [133] (주) 바이오로제트 [134] (주) 바이오믹스테크 [135] (주) 백두에프앤에스 [136] (주) 백두에프엠 [137] (주) 베비에르에프앤비(F&B) [138] (주) 베이글코리아 [139] (주) 베이크플러스 [140] (주) 벨리푸드 [141] (주) 보나비 [142] (주) 보나비 아티지움 [143] (주) 보라티알 [144] (주) 보람비티 [145] (주) 보부아이앤에프 [146] (주) 본비반트 [147] (주) 볼드인터내셔널 [148] (주) 브니엘월드 [149] (주) 브라운스토리 [150] (주) 브레드플랜트 [151] (주) 브레드필 [152] (주) 블랑제리코팡 [153] (주) 블루에프앤비 [154] (주) 비씨디클러스터 [155] (주) 비에스타 [156] (주) 비에이치델리 [157] (주) 비엔푸드 [158] (주) 비오팜 [159] (주) 비케이알코리아 [160] (주) 빙그레 [161] (주) 빨간화덕푸드 [162] (주) 빵명가 [163] (주) 사옹원 [164] (주) 산과들에 [165] (주) 살루스 [166] (주) 삼경물산 [167] (주) 삼경에프에스 [168] (주) 삼경프라자 [169] (주) 삼광식품 [170] (주) 삼아인터내셔날 [171] (주) 삼양사 [172] (주) 삼원트레이드 [173] (주) 삼진씨앤에프 [174] (주) 새로 [175] (주) 새롬식품 [176] (주) 새안글로벌 [177] (주) 샤니 [178] (주) 서래푸드 [179] (주) 서석앤에프 [180] (주) 서울제과 [181] (주) 서울쿠키컴퍼니 [182] (주) 서주 2공장 [183] (주) 서흥 [184] (주) 서흥 오송2공장 [185] (주) 선양평택공장 [186] (주) 선인 [187] (주) 성민에프에스 [188] (주) 성민에프에스 [189] (주) 성신비엔에프 [190] (주) 성신푸드 [191] (주) 성일무역 [192] (주) 성진에프에스 [193] (주) 성호제과 [194] (주) 세미원푸드 [195] (주) 세종바이오팜 [196] (주) 세종에브리푸드 [197] (주) 셀러스푸드 [198] (주) 소이빈델리 [199] (주) 솔루션푸드 [200] (주) 쇼콜라이삭 [201] (주) 술이홀제과 [202] (주) 스위트코리아 [203] (주) 스위트필 [204] (주) 스윗니모코리아 [205] (주) 스칸딕 프라자 [206] (주) 스타드레이딩 [207] (주) 시그마인터내셔날 [208] (주) 신라명과 [209] (주) 신선에프앤브이 [210] (주) 신성티엔에프 [211] (주) 신세계푸드 [212] (주) 신세계푸드 김포공장 [213] (주) 신세계푸드 메인주방 [214] (주) 신세계공장 오산공장 [215] (주) 신세계공장 천안공장 [216] (주) 신우통상예 [217] (주)신화팝빌리지 [218] (주) 신흥물산 [219] (주) 신흥물산 2공장 [220] (주) 신흥식품 [221] (주) 쌀과자마을 [222] (주) 쌍인진천공장 [223] (주) 씨믹스 [224] (주) 씨알푸드 [225] (주) 씨앤미 [226] (주) 씨에스아이팩토리 [227] (주) 씨엔비위즈 [228] (주) 씨엔에스푸드시스템 [229] (주) 씨엔푸드 [230] (주) 씨지에스 에프앤비 [231] (주) 씨케이하우스 [232] (주) 아띠인터내셔널 [233] (주) 아람 [234] (주) 아리랑지에프 [235] (주) 아셀푸드 [236] (주) 아오스 [237] (주) 아우레이트 [238] (주) 아워홈 [239] (주) 아이배냇경포푸드 [240] (주) 아이이케이 [241] (주) 아이푸드넷 [242] (주) 아인츠푸드 [243] (주) 아인츠푸드 성남공장 [244] (주) 아프로푸드 [245] (주) 안스 [246] (주) 안신 [247] (주) 안흥밀바람푸드 [248] (주) 알찬식품 [249] (주) 알탠토 [250] (주) 앰브로스에이엠 [251] (주) 앰퍼샌드 [252] (주) 엄마사랑 [253] (주) 에그앤씨드 [254] (주) 에그앤씨드 진천공장 [255] (주) 에스델리 [256] (주) 에스디생명공학 건강식품사업부문 [257] (주) 에스디씨 [258] (주) 에스디씨2공장 [259] (주) 에스디푸드 [260] (주) 에스씨디글로벌 [261] (주) 에스씨케이통상 [262] (주) 에스씨코리아 [263] (주) 에스앤케이글로벌 [264] (주) 에스엘에스 [265] (주) 에스엠에스무역 [266] (주) 에스엠팜 [267] (주) 에스오엠 에프앤아이 [268] (주) 에스지글로벌 [269] (주) 에스트라  [270] (주) 에스파냐 [271] (주) 에이뷰 [272] (주) 에이비피홀딩스 [273] (주) 에이스엠앤티 [274] (주) 에이치디푸드 [275] (주) 에이치알엘 [276] (주) 에이치푸드 [277] (주) 에취알에스 [278] (주) 에코에프엔비 [279] (주) 에코제이푸드 [280] (주) 에프씨웍스 [281] (주) 에프앤지코리아 [282] (주) 엔에프에스 [283] (주) 엔제이 [284] (주) 엘가 [285] (주) 엘에프 푸드 [286] (주) 엘케이푸드 [287] (주) 엠디에스코리아 [288] (주) 엠에스씨(MSC) [289] (주) 엠케이푸드원 [290] (주) 여리수에프엔씨 [291] (주) 영남코프레이션 [292] (주) 영인코퍼레이션 [293] (주) 오뗄 이천지점 [294] (주) 오리온 제2익산공장 [295] (주) 오리온 제3익산공장 [296] (주) 오리온 제5청주공장 [297] (주) 오리온제4청주공장 [298] (주) 오성물산코리아 [299] (주) 오손도손 [300] (주) 오에스아이무역 [301] (주) 오페라베이커리 [302] (주) 오행생식 [303] (주) 옥두식품 [304] (주) 온맘푸드 [305] (주) 옵스 [306] (주) 와이디에스 [307] (주) 와이앤비푸드농업회사법인 [308] (주) 와이엔씨 [309] (주) 우나트라 [310] (주) 우농 [311] (주) 우래식품 [312] (주) 우리식품 [313] (주) 우말인터프라이시스 [314] (주) 우양 [315] (주) 우양(청양공장) [316] (주) 원일바이오 [317] (주) 월드푸드 [318] (주) 웰팜코리아 [319] (주) 위아더월드 [320] (주) 위앤코리아 [321] (주) 유기농산 [322] (주) 유니온트리 [323] (주) 유담 [324] (주) 유로베이크 [325] (주) 유비콘스 [326] (주) 유스마일 [327] (주) 유앤아이엔젤스 [328] (주) 유유헬스케어 [329] (주) 이대명과 [330] (주) 이델리에프씨 [331] (주) 이랜드이츠 가산월드점 [332] (주) 이레우리밀 [333] (주) 이로운베이커리 [334] (주) 이마트 [335] (주) 이성당 서수공장 [336] (주) 이앤엘푸드 [337] (주) 이엔아이 에프앤비 [338] (주) 인클루시브 인터내셔널 [339] (주) 인터웰푸드시스템 [340] (주) 일성씨엠에스 [341] (주) 일신국제무역 [342] (주) 일영피엔씨 [343] (주) 임실치즈에프엔비 [344] (주) 자은도 [345] (주) 자이언트 [346] (주) 자인 [347] (주) 자임에프앤비 [348] (주) 재호식품 [349] (주) 전주제과 [350] (주) 제원인터내쇼날 [351] (주) 제이디코리아 [352] (주) 제이앤비식품 본사공장 [353] (주) 제이앤이 아산공장 [354] (주) 제이에프앤비플러스 [355] (주) 제이케이글로벌 [356] (주) 제일훼밀리 [357] (주) 젠푸드 [358] (주) 조이푸드 [359] (주) 중원명가유통 [360] (주) 쥬비스푸드 [361] (주) 지바이알 [362] (주) 지앤원 [363] (주) 지에스바이오 [364] (주) 지에프에스인터내셔널 [365] (주) 지우코포레이션 [366] (주) 지웰 [367] (주) 지이디통상 [368] (주) 지지푸드 [369] (주) 진더스 [370] (주) 진성앤푸드원 [371] (주) 진우식품 [372] (주) 참맛 [373] (주) 천년애푸드 [374] (주) 천하코퍼레이션 [375] (주) 청담식품 [376] (주) 청아냉동식품 [377] (주) 청아냉동식품 제2공장 [378] (주) 청아식품 [379] (주) 청우식품 [380] (주) 초코사이버 [381] (주) 초코텍 [382] (주) 최고유통 [383] (주) 캐니스 [384] (주) 커피빈푸드 [385] (주) 케이비엠푸드 [386] (주) 케이씨크린트래이딩 [387] (주) 케이지앤에프 [388] (주) 코레드 인터내쇼날 [389] (주) 코롬방제과 [390] (주) 코리아헬스바이오 [391] (주) 코스모스 [392] (주) 코스모스제과 [393] (주) 코스트코코리아 [394] (주) 코이스라 [395] (주) 코타서비스 [396] (주) 콤비타코리아 [397] (주) 쿠키아 [398] (주) 쿡앤조이인터내셔널 [399] (주) 큐케이씨 [400] (주) 크라운제과 [401] (주) 크라운제과 아산공장 [402] (주) 크라운제과진천공장 [403] (주) 크래프트하인즈코리아 [404] (주) 크리에잇하우스 [405] (주) 키즈웰 [406] (주) 타르틴코리아 [407] (주) 탐라식품 [408] (주) 탑포인트인터내셔널 [409] (주) 태광웰푸드 [410] (주) 태향 [411] (주) 테이트 제2공장 [412] (주) 토탈에프앤비 [413] (주) 톰볼라 [414] (주) 투데이 [415] (주) 트라이콤무역 [416] (주) 티비엠 [417] (주) 티엔농산 [418] (주) 티엔푸드 3공장 [419] (주) 티엠지홀딩스 [420] SHINKINEDO GROUP INC [421] (주) 티엠지홀딩스 [422] (주) 파리크라상 [423] (주) 파리크라상 신공장 [424] (주) 파리크라상인천CK [425] (주) 파리크라상제주공장 [426] (주) 파미유 [427] (주) 파코트레이딩 [428] (주) 파티시에 김영모 [429] (주) 팜크로스 [430] (주) 팜팩토리스푼베이커리 [431] (주) 팡마니 [432] (주) 퍼시머너리 [433] (주) 페이퍼플랜 성남공장 [434] (주) 포비브라이트 을지로점 [435] (주) 푸드빌 [436] (주) 푸드코아 [437] (주) 푸디스 [438] (주) 풀만 [439] (주) 풍년제과본사(제1공장) [440] (주) 풍년제과본사제2공장 [441] (주) 풍림푸드 [442] (주) 플람스코리아 [443] (주) 피엔디서비스 [444] (주) 피자코리아 [445] (주) 피터팬식품 [446] (주) 피티제이코리아 [447] (주) 핀브레드 [448] (주) 핀컴퍼니 [449] (주) 하늘처럼 [450] (주) 하늘푸드제2공장 [451] (주) 하루노유키 [452] (주) 하림산업 함열식품1공장 [453] (주) 하버마린 [454] (주) 하이델코리아 [455] (주) 한국골드메달 [456] (주) 한국라이스바이오 [457] (주) 한국씨엔에스팜 [458] (주) 한국전통문화사업단 [459] (주) 한국푸드본 정관공장 [460] (주) 한맥홈푸드 [461] (주) 한미식품 [462] (주) 한미양행 [463] (주) 한샘식품 [464] (주) 한스제과 [465] (주) 한일제과 [466] (주) 한진식품 [467] (주) 한진휴에프 [468] (주) 해오름식품 [469] (주) 해중실업 [470] (주) 허브큐어 [471] (주) 헤스텍 [472] (주) 현대그린푸드 [473] (주) 현대그린푸드 베이커리공장 [474] (주) 현대에프앤비 [475] (주) 현우 [476] (주) 혜성제과 [477] (주) 호가푸드시스템 [478] (주) 호남샤니 [479] (주) 호연 [480] (주) 홍두당 [481] (주) 화과방 [482] (주) 화성한과 [483] (주) 훼밀리인터내셔날 [484] (주) 휴럼 [485] (주) 휴온스내츄럴 [486] (주) 흥국에프엔비 [487] (합) 햇살나눔 [488] 훕훕베이글 [489] CFC [490] CJ 씨푸드(주) [491] HANDMADE(핸드메이드) [492] IKG코리아 [493] JS푸드 [494] M&F [495] RBNF(알비내츄럴식품) [496] S.N.FOOD(에스.엔.푸드) [497] 가나식품공업사 [498] 가배만쥬 [499] 가야전통식품 [500] 가토미작 \
            [501] 감프롱 [502] 강릉 B&C [503] 강희만쌀과자 [504] 건영푸드 [505] 경기제과 [506] 경화당제과 [507] 고도 경주빵 [508] 고려식품 [509] 고려은단헬스케어 [510] 고려인삼연구(주) [511] 고창지역자활센터 고인돌청정두부 [512] 공감코퍼레이션 [513] 광덕산호두과자전문점 [514] 광양빵 [515] 광일제과 [516] 광주제과 [517] 강릉B&C(BREADS&CAKES) [518] 교토마블 [519] 구스F&B(주) 3공장 [520] 구안산업(주) [521] 구인제과 [522] 국제제과 [523] 국제제과(주) [524] 굿 앤 푸드 [525] 궁전제과(주)광주1공장 [526] 그랑피아프 [527] 그린나래 [528] 그린베이크 [529] 그린식품(주) [530] 그린에프앤비 [531] 그린원푸드 [532] 그린제과 [533] 그림같은빵집 [534] 극동에치팜(주) [535] 글래머러스펭귄베이크샵 [536] 글로벌푸드 마트 [537] 금덕푸드 [538] 금성식품 [539] 금호제과 [540] 기운찬식품 [541] 기원씨앤비 [542] 길상무역 [543] 김인경푸드 [544] 김종하과자공방 [555] 김춘련호두명가 [556] 김포파주인삼농협인삼가공공장 [557] 깊은숲속행복한식품 [558] 깐깐제과 [559] 꼬랑지마카롱 [560] 꽃동네학교 [561] 꿈에서본들 [562] 나란히식품 [563] 나이스제과 [564] 나준베이커리 [565] 나진제과 [566] 나폴레옹 과자점 [567] 나폴레옹 베이커리 유통(주) [568] 나폴레옹베이커리 [569] 나폴레옹제과 [570] 남서울제과 [571] 남원김부각 협동조합 [572] 남원혼불부각 [573] 남일제과 [574] 남해유자농장 [575] 남향푸드또띠아(주) [576] 넛쯔공방 [577] 네슬레코리아유한책임회사 [578] 네오브리즈 [579] 네이처퓨어코리아주식회사 [580] 노리타 [581] 노비스바이오(주) [582] 노아베이커리 성수공장 [583] 농심캘로그(주) [584] 농업법인 세정미가(주) [585] 농업법인(주)윷가네 [586] 농업회사 법인 자연가(유)2공장 [587] 농업회사 법인 주식회사 상복명과원 [588] 농업회사법인 (주)담양한과명진식품 [589] 농업회사법인 (주)수진식품 [590] 농업회사법인 (주)파밍하우스 [591] 농업회사법인 괴산잡곡농산 유한회사 [592] 농업회사법인 김태경우리밀베이커리(주) [593] 농업회사법인 김태경우리밀베이커리(주)2공방 [594] 농업회사법인 김포농식품(주) [595] 농업회사법인 더라이스 주식회사 [596] 농업회사법인 더함 주식회사 [597] 농업회사법인 리뉴얼라이프(주) [598] 농업회사법인 만나씨이에이(주) [599] 농업회사법인 명성제분(주) [600] 농업회사법인 미소 주식회사 [601] 농업회사법인 밀원본가안흥찐빵 주식회사 [602] 농업회사법인 산들해(주) [603] 농업회사법인 양양오색한과(주) 포월공장 [604] 농업회사법인 에스알씨청보리주식회사 [605] 농업회사법인오리온농협 주식회사 [606] 농업회사법인 유기농비건(주) [607] 농업회사법인 유한회사 피오레 [608] 농업회사법인 이장님닷컴(주) [609] 농업회사법인 자이안트팜농장유한회사 [610] 농업회사법인 조은제과 주식회사 [611] 농업회사법인 주식회사 내안에 자연 [612] 농업회사법인 주식회사 내츄럴엔 [613] 농업회사법인 주식회사 마크로드제과 [614] 농업회사법인 주식회사 블랙푸드 [615] 농업회사법인 주식회사 탁촌장 [616] 농업회사법인 주식회사 한농 [617] 농업회사법인 팔당한솔식품 주식회사 [618] 농업회사법인 하나식품(주) [619] 농업회사법인 한세상(주) [620] 농업회사법인(주)계란공장 [621] 농업회사법인(주)광양매화빵 [622] 농업회사법인(주)더더 [623] 농업회사법인(주)두레촌 [624] 농업회사법인(주)싱싱 [625] 농업회사법인(주)키큰아이 [626] 농업회사법인(주)토종스토리 [627] 농업회사법인(주)팜테크 [628] 농업회사법인(주)한국라이스텍 [629] 농업회사법인맛정주식회사 [630] 농업회사법인무성건강식품연구소(주) [631] 농업회사법인운향농원주식회사 [632] 농업회사법인주식회사 명천물산 [633] 농업회사법인주식회사 명천물산 [634] 농업회사법인주식회사 보리담은 [635] 농업회사법인주식회사 팜팩토리 [636] 농업회사법인주식회사곰두레 [637] 농업회사법인주식회사네이처오다 [638] 농업회사법인주식회사우리쌀베이커리 [639] 농업회사법인주식회사천년누리 [640] 농업회사법인주식회사헵시바F&B [641] 농업회사법인즐거운주식회사 [642] 눈비산농산 영농조합법인 [643] 뉴베이커리 [644] 뉴트리디언 [645] 다다에스엠 주식회사 [646] 다다에스엠 주식회사 [647] 다모식품 [648] 다미아일품(주) [649] 다산식품 [650] 다솔푸드 [651] 다솜에프앤비 [652] 다원식품 [653] 다원식품(주) [654] 다이식품 [655] 다이식품 제2공장 [656] 다인상사 [657] 다이식품 제2공장 [658] 다인상사 [659] 다인식품 [660] 다현에프앤비(F&B) [661] 다흠영농조합법인 [662] 닥터오트커코리아 유한회사 [663] 단석가찰보리빵 [664] 달곰씨앤에프 [665] 달리는농장 [666] 달음협동조합 [667] 달콤한상상 주식회사 [668] 닮은협동조합 [669] 담양죽순영농조합법인 [670] 대경식품 [671] 대광에프에스 [672] 대림종합식품 [673] 대방수산(주) [674] 대복 [675] 대빵식품 [676] 대상인터내셔널 [677] 대성무역 [678] 대성제과 [679] 대신농산(주)2공장 [680] 대영식품 [681] 대영식품(주) [682] 대영식품2공장 [683] 대영식품주식회사 [684] 대원정식품 [685] 대진유통 [686] 대한제분(주) [687] 대한통합무역 [688] 대한푸드텍(주) 2공장 [689] 대호한과 [690] 더다경 [691] 더바른 [692] 더벨로 [693] 더본푸드 [694] 더브레드블루 [695] 더식품 [696] 더업코리아(the up korea) [697] 더존식품 주식회사 [698] 데이크리에이티브(주) [699] 데일리푸드 [700] 데코리아제과(주) [701] 도마에프앤비주식회사 [702] 도울바이오푸드영농조합법인 [703] 도제식빵 [704] 돌담푸드 [705] 동국산업 주식회사 [706] 동산식품 [707] 동산제과 [708] 동서제과 [709] 동성식품 [710] 동심제과 [711] 동아오츠카(주) [712] 동아제과 [713] 동양식품 [714] 동진바이오농업회사법인(주) [715] 동화상사 [716] 두두담 [717] 두레농산 [718] 두리두리식품 [719] 두리식품 [720] 두리하나다울 [721] 두스프랑스 [722] 두씨밀레 [723] 두영푸드 [724] 두호식품 [725] 드림푸드 빵굽네 [726] 들래미협동조합 [727] 디에스에프씨(주) [728] 디엠지(DMZ)해마루식품 [729] 디저트 단디 [730] 떡메마을협동조합 [731] 떡메식품 [732] 똘레랑스 [733] 뜸부기식품 주식회사 [734] 라바테라 커피 [735] 라이온제과 [736] 라이프업 [737] 라이프제과 [738] 랑카 코리아 [739] 레꼴두스 [740] 레인보우팜(주)농업회사법인 [741] 로얄제과(주) [742] 로투스베이커리즈코리아 주식회사 [743] 로티보이인터내셔날코리아 주식회사 [744] 로플로플 [745] 롯데쇼핑(주)롯데마트사업본부 [746] 롯데제과(주) [747] 롯데제과(주) 부산공장 [748] 롯데제과(주) 수원공장 [749] 롯데제과(주)증평공장 [750] 롯데푸드(주) [751] 르구르망 주식회사 [752] 르까도드마비 [753] 리리식품 [754] 리앤바라크 [755] 리치몬드 과자점 [756] 리치식품 [757] 리치코리아 유한회사 [758] 리치코리아유한회사 [759] 마늘빵집 [760] 마들렌제주 [761] 마라나타 [762] 마루티앤씨(주) [763] 마망갸또 1공장 [764] 마망갸또 2공장 [765] 마밀랜드산골식품 [766] 마산제과 [767] 마시와 [768] 마이코 인터내셔널(방아다리) [769] 마이코 인터내셔널(방아다리) [770] 마카레 협동조합 [771] 마켓랩 [772] 마틴브라워코리아천안지점 [773] 마포구립장애인직업재활센터(수아밀) [774] 막스(MAX) [775] 만나꿀빵 [776] 맘모스식품 [777] 맘스쌀과자 [778] 맘스케이크 주식회사 [779] 맛드린식품 [780] 맛사랑식품 [781] 매스컴퍼니 주식회사 [782] 매일식품 [783] 매일유업(주) 청양공장 [784] 매일유업(주)평택CK [785] 매크로통상(주) [786] 맥아당청주공장 [787] 명류당 [788] 명성제과 [789] 명인제과 [790] 명일제과 [791] 명품푸드 [792] 명희봉밀 [793] 모퉁이쿠키 [794] 몬셀코리아 [795] 몬셀코리아 경기센터 [796] 몬셀코리아 양산지점 [797] 몽상클레르 코리아 [798] 몽샹디저트 [799] 무인양품(주) [800] 문경새재빵마을 [801] 미가방 유한회사 [802] 미가식품 [803] 미가푸드 [804] 미광식품 [805] 미꼬 [806] 미나티 [807] 미다솜 주식회사 [808] 미담제과 [809] 미담푸드 [810] 미드미통상 [811] 미듬영농조합법인(제3공장) [812] 미라클센터 [813] 미래제과 [814] 미래직업재활원 양산순쌀빵 [815] 미랜드 산업 [816] 미미식품 [817] 미성식품 [818] 미성패밀리(주) [819] 미성패밀리주식회사 [820] 미소머금고영농조합법인 [821] 미송 웰푸드 [822] 미잠미과 [823] 미찌푸드 주식회사 [824] 미호미 [825] 믹스앤매치 [826] 밀도 씨케이 [827] 바스락(주) [828] 바이오에프이주식회사 [829] 박가당 [830] 밤뜨래영농조합법인 2공장 [831] 배드매드브레드 [832] 배정열 베이커리 [833] 베스베니(주) [834] 베스트 푸드 [835] 베스트엠엔피 [836] 베이커리이음 [837] 베이커스딜라이트 [838] 벤스쿠키코리아 [839] 보강에프에스 [840] 보령누룽지과자 [841] 보리가득 [842] 보리마을 [843] 보스톤홀딩스(주) [844] 본정초콜릿(주) [845] 봄이네 [846] 봉메식품 [847] 부국 에프앤씨 [848] 부농푸드 [849] 브레드팜 [850] 브레젤르 [851] 브린츠명과 [852] 비건포레스트 [853] 비룡유기농 영농조합법인 [854] 비알코리아(주)김해농장 [855] 비알코리아(주)대구생산점 [856] 비알코리아(주)신탄진공장 [857] 비알코리아(주)안양공장 [858] 비알코리아(주)제주생산점 [859] 비에이치무역 [860] 비케이씨코퍼레이션(주) [861] 빅푸드시스템 [862] 빌그린(VilGreen) [863] 빛가을르빵 [864] 빛과소금 [865] 빠니니코리아(주) [866] 빨강콩(주) [867] 빵굼터협동조합 [868] 빵드밀(주) [869] 빵부자 [870] 사랑의일터(사랑의베이커리) [871] 산내마을 [872] 산타푸드 [873] 산포농연 [874] 살렘마을 협동조합 [875] 삼교농원 [876] 삼보인터내셔날 [877] 삼성식품 [878] 삼양사 [879] 삼양식품(주)원주공장 [880] 삼영사 [881] 삼진식품 [882] 상수당 [883] 상일식품(주) [884] 상일제과주식회사 [885] 상하농원(유)빵공방 [886] 새싹발아통밀빵 [887] 생제비제빵소 [888] 생활개선회농산물가공사업단영농법인 [889] 서영이앤티(주) [890] 서울국제식품 주식회사 [891] 서울브레드 [892] 서울식품공업(주) [893] 서울제과 [894] 서주제과(주) [895] 서주제과(주)3공장 [896] 서촌옛날통밀빵 [897] 서피란 [898] 서해안 푸드 [899] 서현식품 [900] 선미식품 [901] 선영글로벌 [902] 선영식품 [903] 설고 [904] 설공 [905] 성미제과 [906] 성부식품 [907] 성연식품주식회사 [908] 성장 [909] 성찬식품 [910] 성희무역(주) [911] 세라글로벌 주식회사 [912] 세린식품(주) [913] 세미식품 [914] 세준 [915] 솜사탕빵공장 [916] 솜사탕일연구소 주식회사 [917] 솜인터내셔널(주) [918] 쇼콜리디아 [919] 수예당 [920] 숲 [921] 슈가레인(Sugarrain) [922] 스위트밀(주) [923] 스위트스페이스(주) [924] 스위티코리아 주식회사(Sweetie Corea Co., Ltd) [925] 스타에프앤비 [926] 스타원주식회사 [927] 스타원주식회사 [928] 시골생활건강식품 [929] 신경주빵 [930] 신광제과 [931] 신사당제과점 [932] 신명식품 [933] 신성제과 [934] 신정푸드(주) [935] 신한식품 주식회사 [936] 신화당제과 [937] 신흥F&D(에프앤디) [938] 신흥식품 [939] 신흥제과 [940] 쌀로만식품 [941] 쌀로만제과 [942] 쌀로만푸드 [943] 쌍지뜰 [944] 썬푸드 [945] 씨엔에이치에프에스(주) [946] 씨엔알트레이딩 [947] 씨제이제일제당(주)진천BLOSSOM CAMPUS [948] 씨제이푸드빌주식회사 [949] 씨지에스푸드(CGS FOOD) [950] 씨튼장애인직업재활센터 씨튼베이커리 [951] 아기랑 [952] 아뜰리에 프랭크 [953] 아라한 [954] 아름식품 [955] 아린에프앤비(ARIN F&B) [956] 아미트레이딩 [957] 아미푸드 [958] 아성식품 [959] 아세아식품 [960] 아우어로스팅 [961] 아이누리 [962] 아이리치베이커리 [963] 아이배냇(주) [964] 아이보리식품영농조합법인 [965] 아이스제과 [966] 아이앤디푸드 [967] 아인당 [968] 아자개영농조합법인 [969] 아테네 식품서비스 [970] 안단테데이어리코리아 [971] 안동고을탁촌장 영농조합법인 [972] 안흥댁 안흥찐빵 [973] 안흥식품 [974] 알뜨랑농원 [975] 알프레스코 [976] 앙팡드봉봉 [977] 애덕의집보호작업장(소울베이커리) [978] 애플디저트팩토리 [979] 앨리스가든 [980] 양유 클라우드 키친 [981] 양지 [982] 양지제과 [983] 어린왕자식품 [984] 에덴제과 [985] 에듀인터내셔날 [986] 에바다푸드시스템 [987] 에스엔제이 글로벌 [988] 에스엘비코리아(주) [989] 에스와이 글로벌 [990] 에스케이내추럴팜(주) [991] 에스피엘주식회사 [992] 에쓰푸드(주) [993] 에이스식품 [994] 에이앤인니푸드 [995] 에이에프인터내셔널 주식회사 [996] 에이엠트레이드 [997] 에이원식품 [998] 에이치에스에프 [999] 에이치엔웨이 [1000] 에이케이무역 주식회사 \
            [1001] 에이펙셀(주) [1002] 에코무역 [1003] 에코푸드(주) 1공장 [1004] 에코푸드제2공장 [1005] 에프와이지주식회사 괴산공장지점 [1006] 엔와이푸드 [1007] 엔젤비엔디 [1008] 엘리시온 [1009] 엘브이에스랩(라보카) [1010] 엠스푸드주식회사 [1011] 엠에스바이오텍(주)제2공장 [1012] 엠엠씨케이 [1013] 엠즈씨드 주식회사 [1014] 엠큐네트웍스(주) [1015] 엠큐브인터내셔날 [1016] 여리수 [1017] 여뭄식품 [1018] 연곡제과 [1019] 연화T&F [1020] 열두광주리영농조합법인 [1021] 영농조합법인 물댄동산 [1022] 영농조합법인 산골농장 [1023] 영농조합법인 참농부들 [1024] 영농조합법인 푸드인완주 마더쿠키 [1025] 영농조합법인 푸른초장 [1026] 영농조합법인제주감귤과자 [1027] 영동제과 [1028] 영베이커리 [1029] 영양제과(주) [1030] 영주농업회사법인주식회사 [1031] 영진식품 [1032] 영푸드시스템(주) [1033] 영푸드시스템(주)오창공장 [1034] 영흥식품(주) [1035] 예그린 [1036] 예미담 [1037] 예스통상(주) [1038] 옐로우팩토리 [1039] 오가네 참부각 [1040] 오가닉 어스 [1041] 오가닉마스디저트 [1042] 오가닉집 [1043] 오룡식품 [1044] 오붐(주) [1045] 오에스케이(OSK) [1046] 오클라코리아유한회사 [1047] 오키드인더스트리 [1048] 옥산인터내셔널 [1049] 옥천푸드가공협동조합 [1050] 온세까세로 [1051] 올가푸드 [1052] 올네이션스트레이딩 [1053] 올바름 [1054] 올인원랩 [1055] 와우커머스 [1056] 와이케이 인터 [1057] 완도바다식품 [1058] 용궁식품 [1059] 우닉(UNIK) [1060] 우리명과 [1061] 우리밀 푸드 [1062] 우리식품 [1063] 우리씨앤디(주) [1064] 우리트레이딩 [1065] 우림식품(주) [1066] 우비앤팜스 [1067] 우성식품 [1068] 우승제과 [1069] 우영베이커리 [1070] 우영식품 [1071] 우일 유한책임회사 [1072] 울릉산채영농조합 [1073] 원보식품 [1074] 원스푸드 [1075] 원인터내셔날 [1076] 원조할머니학화호도과자 [1077] 월드웨이(주) [1078] 월매식품 [1079] 월푸상사(주) [1080] 웰가제과 [1081] 웰코리아 [1082] 위버멘쉬코리아 주식회사 [1083] 위캔센터 [1084] 윈윈인터내셔날(주) [1085] 유로라인컴퍼니(EUROLINE COMPANY) [1086] 유로베이커리 [1087] 유로인터글로벌 주식회사 [1088] 유로푸드 [1089] 유림제과 [1090] 유명한안흥찐빵 [1091] 유성씨앤에프(주) [1092] 유진에프엔비 [1093] 유창성업(주) [1094] 유창푸드 [1095] 유풍제과 [1096] 유한책임회사 이천쌀강정 [1097] 유한푸드 [1098] 유한회사 마더구스 [1099] 유한회사 오가네 [1100] 유한회사 징코푸드시스템 [1101] 윤 푸드 [1102] 은가비식품 [1103] 은성제과 [1104] 의성흑마늘빵 [1105] 이담푸드 [1106] 이든또르띠아 [1107] 이든푸드영농조합법인 [1108] 이룸무역 [1109] 이멕스무역(주) [1110] 이봉환제과 [1111] 이시스무역 [1112] 이앤에스(주) [1113] 이조명과 [1114] 이츠얌에프엔비 [1115] 이케아코리아 유한회사 [1116] 일광제과 [1117] 일동후디스(주) [1118] 임실농부(주) [1119] 임페리아 [1120] 임페리아 브레드 [1121] 자이연팜 [1122] 장복용과자공방 [1123] 장원급제빵,찰보리빵 [1124] 전통맛경주빵 [1125] 정담에프앤비 상도지점 [1126] 정든식품 [1127] 정선아라리한과 [1128] 정성제과 [1129] 정일식품 [1130] 정일제과 [1131] 제너럴밀스코리아(주) [1132] 제다푸드시스템 [1133] 제로베이커리 [1134] 제이브라운씨엔엠 [1135] 제이씨컴퍼니 [1136] 제이에이치 코퍼레이션(JH Corp) [1137] 제이에이치디인터내셔널 [1138] 제이엠 [1139] 제이엠에프엔비 주식회사 [1140] 제이제이엔터프라이즈 [1141] 제이티푸드 [1142] 제이피컴퍼니(JP COMPANY) [1143] 제일가식품 [1144] 제일물산 [1145] 제일제과 [1146] 제제에프비에스(주) [1147] 제주담다 [1148] 제주마미 [1149] 젤리상점 [1150] 조은명가 [1151] 조은식품 [1152] 좋은직업재활센터 [1153] 주)경주제과 [1154] 주)미스터베이커리농업회사법인 [1155] 주)북해도스위트코리아 [1156] 주)비지에프푸드 [1157] 주)신라명가 [1158] 주)에스에이치에스 [1159] 주)인카이로스 [1160] 주)짱죽 [1161] 주)한살림우리밀제과 [1162] 주식회사 글로션 [1163] 주식회사 가온앤푸드 [1164] 주식회사 거누 [1165] 주식회사 그레닉스 [1166] 주식회사 그레닉스 제3공장 [1167] 주식회사 기업과사람들 [1168] 주식회사 나무인터내셔널 [1169] 주식회사 나이스커피시스템 [1170] 주식회사 늘푸른 [1171] 주식회사 다인경주빵 [1172] 주식회사 달그락푸드팩토리 [1173] 주식회사 달롤컴퍼니 [1174] 주식회사 대신에프에스 [1175] 주식회사 대웅생명과학 [1176] 주식회사 더 스윗(The Sweet Co.,Ltd) [1177] 주식회사 더미앤밀 [1178] 주식회사 더블스윗 [1179] 주식회사 델리팜 [1180] 주식회사 도투락 [1181] 주식회사 두손웰푸드 [1182] 주식회사 디앙뜨 [1183] 주식회사 디엔타르 [1184] 주식회사 랑컴퍼니 [1185] 주식회사 레헴(삼송지점) [1186] 주식회사 렐라코리아 [1187] 주식회사 루츠앤푸룻 [1188] 주식회사 루트비 [1189] 주식회사 르뺑 [1190] 주식회사 마켓빌더즈코리아 [1191] 주식회사 맛사랑 [1192] 주식회사 메종엠오 [1193] 주식회사 미래본 [1194] 주식회사 미스티 [1195] 주식회사 바로인터내셔널 [1196] 주식회사 바이오에비뉴 [1197] 주식회사 본 [1198] 주식회사 본만제 [1199] 주식회사 비브이 [1200] 주식회사 비에스푸드빌 [1201] 주식회사 비욘드마켓 [1202] 주식회사 비즈바이오 [1203] 주식회사 사리원 씨에프디 [1204] 주식회사 서광식품 [1205] 주식회사 성실푸드 [1206] 주식회사 세진병과 [1207] 주식회사 소담인터내셔널 [1208] 주식회사 수버킷 [1209] 주식회사 스위트드림 [1210] 주식회사 스위트바이킹 [1211] 주식회사 스위트컵 [1212] 주식회사 스토비 [1213] 주식회사 시온올앤지 [1214] 주식회사 시즈너FS [1215] 주식회사 신흥제과 [1216] 주식회사 씨엔피코퍼레이션 [1217] 주식회사 아름다운맛 [1218] 주식회사 아스트로스 [1219] 주식회사 아푸 [1220] 주식회사 알피엠코퍼레이션 [1221] 주식회사 얼리키친 [1222] 주식회사 에스디에프인터내셔널 [1223] 주식회사 에스알 인터내셔날 [1224] 주시고히사 에스에이치글로벌코리아 [1225] 주식회사 에스피씨삼립 [1226] 주식회사 에스피씨삼립 성남2공장 [1227] 주식회사 에이앤제우스 [1228] 주식회사 에이치티인더스트리얼트레이딩 [1229] 주식회사 엘티엠푸드 [1230] 주식회사 오늘도 [1231] 주식회사 오뚜기 [1232] 주식회사 오키스비스테까 [1233] 주식회사 올곧은 [1234] 주식회사 우드앤브릭 [1235] 주식회사 우리가스토리 [1236] 주식회사 우리밀 새말공장 [1237] 주식회사 웰하임 [1238] 주식회사 위너스 [1239] 주식회사 위레스코 [1240] 주식회사 위스트 [1241] 주식회사 유로에이치엔제이 [1242] 주식회사 유로푸드서비스 [1243] 주식회사 유앤아이트레이드 [1244] 주식회사 유진에프에스 [1245] 주식회사 이든에프앤씨 [1246] 주식회사 이마트24 [1247] 주식회사 이안상사 [1248] 주식회사 이음새 농업회사법인 [1249] 주식회사 인코트레이딩 [1250] 주식회사 자노탁트코리아 [1251] 주식회사 자주민인터내셔널 [1252] 주식회사 제이브라운 [1253] 주식회사 제이씨푸드빌 [1254] 주식회사 젤리젤리 [1255] 주식회사 조이인터내셔널 [1256] 주식회사 쥬니쿠키 [1257] 주식회사 지브레인 [1258] 주식회사 지푸드 [1259] 주식회사 차이오 [1260] 주식회사 천우물산 [1261] 주식회사 초록에프앤비(F&B) [1262] 주식회사 치즈앤푸드 [1263] 주식회사 카비르인터프라이시스 [1264] 주식회사 카카오파크 [1265] 주식회사 케이에프씨코리아 [1266] 주식회사 케이티에스씨(KTSC) [1267] 주식회사 케익드라마 [1268] 주식회사 코끼리와친구들 [1269] 주식회사 코리안파인 [1270] 주식회사 코비스트레이드 [1271] 주식회사 코스팜 [1272] 주식회사 크레타케이알 [1273] 주식회사 클라나드 [1274] 주식회사 키푸디 [1275] 주식회사 타르틴코리아 [1276] 주식회사 태웅푸드 [1277] 주식회사 테라코어 [1278] 주식회사 투데이앤투머로우 [1279] 주식회사 투와이코퍼레이션 [1280] 주식회사 트릿지 [1281] 주식회사 펄펫 [1282] 주식회사 푸드앤트리트 [1283] 주식회사 피케이글로벌 [1284] 주식회사 핀브레드 [1285] 주식회사 하나피아 [1286] 주식회사 한국가구 식품사업부 [1287] 주식회사 한영식품 [1288] 주식회사 한진무역 [1289] 주식회사 한투인터내셔널 [1290] 주식회사 해피 [1291] 주식회사 행복식품 [1292] 주식회사 호프인터내셔널 [1293] 주식회사 효쿠앤코 [1294] 주식회사 후앙 [1295] 주식회사강동오케익1공장 [1296] 주식회사과자의성 [1297] 주식회사니코인터내셔널 [1298] 주식회사다우엠에스 [1299] 주식회사두리인터내셔날 [1300] 주식회사디에스푸드 [1301] 주식회사미가 [1302] 주식회사바이오360  [1303] 주식회사삼진씨앤에프 [1304] 주식회사샤니 [1305] 주식회사선유 [1306] 주식회사아인스 [1307] 주식회사에스제이코퍼레이션 [1308] 주식회사에이원에프앤비 [1309] 주식회사엘유코리아 [1310] 주식회사엠오유통 [1311] 주식회사오션스퀘어 [1312] 주식회사원더풀에프엔비 [1313] 주식회사제이엘푸드텍 [1314] 주식회사제키스 [1315] 주식회사제키스 제2공장 [1316] 주식회사조흥 [1317] 주식회사참조은에스에프 [1318] 주식회사코코인터내셔널 [1319] 주식회사탐나는초콜릿 [1320] 주식회사투마루 [1321] 주식회사팜틱 [1322] 주식회사포린푸드코리아 [1323] 주식회사폴라리스 [1324] 주식회사푸름 [1325] 주식회사풍년제과 [1326] 주식회사한이식품 [1327] 주식회사헬스랩 [1328] 중앙 바이오(주) [1329] 쥬쥬베이킹 [1330] 지디앤와이(주) [1331] 지리산 함양 허농부 [1332] 지비코퍼레이션(주) [1333] 지성무역 [1334] 지후쌀과자 [1335] 진스 F&B [1336] 진앤진푸드 [1337] 진터식품 [1338] 진푸드 [1339] 진한제과 [1340] 질마재 농장 [1341] 쫀득한제주 [1342] 참그린식품 [1343] 참맛식품 [1344] 참샘영농조합법인 [1345] 창원생과방 [1346] 천안제과 [1347] 천일식품(주) [1348] 청북제과 [1349] 청오건강농업회사법인주식회사 5공장 [1350] 청원식품 [1351] 청춘푸드 [1352] 총본산경주빵 [1353] 쵸커 [1354] 치즈샵 [1355] 칠성제과 [1356] 카루길식품 [1357] 카리스F&B [1358] 카밀식품 [1359] 카페이노스(주) [1360] 케이더블비 유한회사 [1361] 케이비인터내셔널 [1362] 케이제이씨컴퍼니 [1363] 케이제이푸드 [1364] 케이피라인(주) [1365] 케익부띠끄3  [1366] 코뉴 [1367] 코리아식품 주식회사 [1368] 코리아타이 [1369] 코리아푸드 [1370] 코만스팩토리 [1371] 코스맥스엔비티(주) [1372] 코코브루니 [1373] 코코허브 [1374] 쿠팡 주식회사 [1375] 쿱푸드시스템 주식회사 [1376] 퀸즈푸드 [1377] 크래들 [1378] 크레푸드 [1379] 크리스피크림대전둔산점 [1380] 크리스피크림부천커미서리 [1381] 크림바바 [1382] 클래식에프앤비컴퍼니 [1383] 키커피컴퍼니 연희점 [1384] 키토익스프레스 [1385] 탑푸드시스템 [1386] 태광제과 [1387] 태백산채냉면영농조합법인 [1388] 태성제과 [1389] 태양이엔에스(주) [1390] 태영식품 [1391] 태원통상 [1392] 태진무역 [1393] 태평씨엔에프 [1394] 토리코리아 주식회사 [1395] 토속안흥찐빵 [1396] 토종식품 [1397] 통일식품 [1398] 투썸플레이스 주식회사 [1399] 틔움직업재활센터 [1400] 티니호박 [1401] 티디에프코리아(주) [1402] 티씨엔씨 [1403] 티에이디 [1404] 티엔엠푸드(TnM Food) [1405] 파라디소칸초네 [1406] 파우치코리아 [1407] 파파루 [1408] 파파브레드 [1409] 팍스푸드 [1410] 팜드림(주) [1411] 팡드켜흐 [1412] 페이브베이커리 가산공장 [1413] 평화제과 [1414] 포비아워스 합정점 [1415] 포항장미빵 [1416] 푸드네츄럴(주) [1417] 푸드원(맛을담는사람들) [1418] 푸르네제과 [1419] 푸르미 식품 [1420] 푸른들 [1421] 풍년식품 [1422] 풍전나이스제과(주) [1423] 프라다코리아 유한회사 [1424] 프로엠 2공장 [1425] 프리미엄팝콘스토어홀리팝 [1426] 플랜트베이커리 [1427] 플레어비베이커리랩 [1428] 플레이버랩(주) [1429] 플레이버랩(주) [1430] 피엠투케이인터내셔날 유한회사 [1431] 픽어베이글 [1432] 핑거사인브레드 [1433] 하나트레이딩 [1434] 하나푸드 [1435] 하명식품 [1436] 하우스원푸드 [1437] 하이에나 [1438] 하이원베이커리 F2 [1439] 하이원푸드 [1440] 하임상사 [1441] 하트너카페(Heartener Cafe) [1442] 한국뉴초이스푸드(주) [1443] 한국마즈(유) [1444] 한국벡스팜제약(주) [1445] 한국제과식품협동조합 [1446] 한국토종약초영농조합가공장 [1447] 한국피자헛(유) [1448] 한독제과 [1449] 한마루 호도과자 [1450] 한백에프앤에스 [1451] 한비즌 [1452] 한성식품 [1453] 한성식품 [1454] 한세상 [1455] 한스무역 [1456] 한양제과주식회사 [1457] 한올식품 [1458] 한일물산주식회사 [1459] 한일식품 [1450] 한젠바이오 [1451] 한진푸드 [1452] 한터 [1453] 한화솔루션(주) 갤러리아 사업장 [1454] 할머니학화호두과자터미널본점 [1455] 할미푸드(김해지역자활센터) [1456] 함지박(주) [1457] 핫푸드 [1458] 해륙식품 [1459] 해천한중식품 [1460] 해태가루비(주) [1461] 해태가루비(주) 제 2공장 [1462] 해태제과식품(주) [1463] 해태제과식품(주)광주공장 [1464] 해태제과식품(주)천안2공장 [1465] 해태제과식품(주)청주공장 [1466] 해피드림 [1467] 햇사랑식품 [1468] 햇살담은자연마을영농조합법인 [1469] 현이농산(주) [1470] 현이푸드빌 주식회사 [1471] 현이농산(주) [1472] 현이푸드빌 주식회사 [1473] 혜성식품 [1474] 호매실장애인보호작업장 [1475] 호밀식품 [1476] 호산제과 [1477] 홈플러스 주식회사 [1478] 홈플러스(주) [1479] 홍식이 디저트 [1480] 홍천찐빵 [1481] 화랑경주빵 [1482] 화산영농조합법인 [1483] 화성식품제포협동조합연합회 [1484] 화신영농조합법인 [1485] 화이트도우 [1486] 화인에프앤드비서비스(주) [1487] 화일약품(주) [1488] 황금제과 [1489] 황금찰보리빵 [1490] 황남빵 [1491] 황용당제과 [1492] 효성식품 영농조합법인 [1493] 효성인터내셔날 [1494] 효성인터내셔널(주) [1495] 후덕물산(주)야산공장 [1496] 후아바 [1497] 훼미리식품(주)부산공장 [1498] 훼미리식품주식회사 [1499] 휘앤비농업회사법인(주) [1500] 히피스랩 [1501] 힐링푸드 [1502] (주)면사랑 [1503] 주식회사 대신에프에스 [1504] 남양유업 [1505] 삼양식품(주) 원주공장 [1506] 삼양식품  [1507] 동원산업 [1508] (주)프로엠 2공장 [1509] 조앤스빌 [1510] (주)서울제과 [1511] (주)에스디푸드 [1512] (주)에스피씨삼립 [1513] 매일유업(주) 평택공장 [1514] (주)서울푸드트레이딩 [1515] 훼미리식품 [1516] (주)파리크라상 성남제2공장 [1517] (주)델토리 [1518] 롯데쇼핑(주) [1519] 이엑스트레이딩 [1520] 심플로트코리아(주)영업소 [1521] (주) 조흥 [1522] 미가방유한회사 [1523] (주) 폴라리스 [1524] 로투스베이커리즈코리아(주) [1525] (주) 크라운제과 진천공장 [1526] (주) 오리온 제4청주공장 [1527] (주) 기업과사람들 [1528] (주) 미가 [1529] 주식회사 제이피푸드 [1530] (주) 오플로 서울브레드 [1531] (주) 에스피씨삼립 성남2공장 [1532] 마이비건쉐프 [1533] (주) 파리크라상 인천CK [1534] (주) 파리크라상 제주공장 [1535] (주) 푸드코아 [1536] (주) 제키스 [1537] (주) 참조은에스에프 [1538] 참바다영어조합법인 멀티센터 [1539] 초원의아침 [1540] 미팜에프앤비 [1541] 몬쉘코리아 [1542] 문경새재옛날찹쌀떡 [1453] 마이굿밀(Mygoodmeal) [1454] (주) 거산하역 [1455] (주) 신세계푸드 천안공장 [1456] (주) 쿱스토어 광주전남 자연드림 [1457] 치즈트랩 [1458] 씨제이푸드빌(주) [1459] 에스피엘(주) [1460] (주) 대신에프에스 [1461] (주) 거산하북교역 [1462] (주) 도투락식품 [1463] (주) 모모 [1464] (주) 우양 청양공장 [1465] (주) 리더스에프에스 [1466] 호미곶 전통 찰보리빵 [1467] (주) 강동오케익 1공장 [1468] 비알코리아(주)김해공장 [1469] 주식회사메리푸드 [1470] 우리들 베이커리 [1471] (주) 봉코앙 르푸도레 [1472] (주) 탁촌장 [1473] (주) 경주제과 [1474] 장수식품 [1475] 자연드림 철산점 [1476] 자연드림 분평점 [1477] (주) 한살림우리밀제과 [1478] 오트밀식품 [1479] (주) 이청당 서수공장 [1480] (주) 설탕없는과자공장 [1481] 신라당제과점 [1482] (주) 에스디에프 [1483] 장가네제과 [1484] 거승당 [1485] (주) 광일식품 [1486] 농촌사랑(주) [1487] (주) 더닐크팩토리 [1488] (주) 케익드라마 [1489] (주) 에스알인터내셔널 [1490] 박할머니안흥찐빵 [1491] 푸드인완주 마더쿠키 [1492] (주) 모리닐로 [1493] 주식회사 나무와벽돌 [1494] 자연드림 성북길음점 [1495] 자미원비앤에프 [1496] 오릉경주빵 찰보리빵 [1497] 청룡제과 [1498] 경주가보리 [1499] (주) 아르토스 [1500] (주) 씨엔케이푸드 [1501] (주) 겐츠베이커리 제2공장 [1502] (주) 흥국에프앤비 [1503] (주) 하늘푸드 제2공장 [1504] (주) 쿱스토어 경기동남부 금곡점 ")             # 회사 이름 선택하기
        
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