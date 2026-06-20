# 사이트 공통 설정
# 배포 도메인 확정 후 BASE_URL 을 실제 도메인으로 변경하세요.
BASE_URL = "https://songpa-massage1.pages.dev"

BRAND = "바로GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 외부 제휴·제작 문의 텔레그램 링크
TELEGRAM_URL = "https://t.me/googleseolab"

# 검색엔진 사이트 소유확인 — 값을 받은 뒤 채우면 모든 페이지 <head>에 자동 삽입된다.
NAVER_VERIFY = "7f327c8ac29796a1df48699694e98356e28704a1"
GOOGLE_VERIFY = ""  # 구글 서치콘솔 'HTML 태그' 확인값을 넣으세요.

# IndexNow 키 — 글 게시 시 빙·네이버 등에 즉시 색인 통보에 사용.
# build.py 가 루트에 "<INDEXNOW_KEY>.txt" 키 파일을 생성한다.
INDEXNOW_KEY = "a162d761934d434ab46171941f879043c671687eb1844cc29add855b283ccfac"

# 상단 메뉴 — 하위 메뉴에는 키워드("출장마사지")를 반복하지 않고 지역명·역명만 표시한다.
NAV = [
    ("홈", "/", []),
    ("송파 출장마사지", "/massage/", [
        ("출장마사지 안내", "/massage/#service"),
        ("홈타이 안내", "/massage/#hometai"),
        ("전지역 방문 안내", "/massage/#coverage"),
        ("역세권 인근 안내", "/massage/#stations"),
        ("예약 가능 시간", "/massage/#hours"),
        ("코스 선택 안내", "/massage/#course"),
        ("이용 전 확인사항", "/massage/#check"),
        ("위생·안전 안내", "/massage/#safety"),
        ("자주 묻는 질문", "/massage/#faq"),
    ]),
    ("지역별 안내", "/seoul/songpa-gu/", [
        ("송파구 전체", "/seoul/songpa-gu/"),
        ("잠실동", "/seoul/songpa-gu/jamsil-dong/"),
        ("방이동", "/seoul/songpa-gu/bangi-dong/"),
        ("오륜동", "/seoul/songpa-gu/oryun-dong/"),
        ("오금동", "/seoul/songpa-gu/ogeum-dong/"),
        ("송파동", "/seoul/songpa-gu/songpa-dong/"),
        ("석촌동", "/seoul/songpa-gu/seokchon-dong/"),
        ("삼전동", "/seoul/songpa-gu/samjeon-dong/"),
        ("가락동", "/seoul/songpa-gu/garak-dong/"),
        ("문정동", "/seoul/songpa-gu/munjeong-dong/"),
        ("장지동", "/seoul/songpa-gu/jangji-dong/"),
        ("위례동", "/seoul/songpa-gu/wirye-dong/"),
        ("풍납동", "/seoul/songpa-gu/pungnap-dong/"),
        ("거여동", "/seoul/songpa-gu/geoyeo-dong/"),
        ("마천동", "/seoul/songpa-gu/macheon-dong/"),
    ]),
    ("역세권 안내", "/seoul/songpa-gu/station/", [
        ("역 전체", "/seoul/songpa-gu/station/"),
        ("잠실역", "/seoul/songpa-gu/station/jamsil-station/"),
        ("잠실새내역", "/seoul/songpa-gu/station/jamsilsaenae-station/"),
        ("잠실나루역", "/seoul/songpa-gu/station/jamsillaru-station/"),
        ("몽촌토성역", "/seoul/songpa-gu/station/mongchontoseong-station/"),
        ("송파나루역", "/seoul/songpa-gu/station/songpanaru-station/"),
        ("석촌역", "/seoul/songpa-gu/station/seokchon-station/"),
        ("석촌고분역", "/seoul/songpa-gu/station/seokchon-gobun-station/"),
        ("삼전역", "/seoul/songpa-gu/station/samjeon-station/"),
        ("가락시장역", "/seoul/songpa-gu/station/garak-market-station/"),
        ("경찰병원역", "/seoul/songpa-gu/station/national-police-hospital-station/"),
        ("오금역", "/seoul/songpa-gu/station/ogeum-station/"),
        ("방이역", "/seoul/songpa-gu/station/bangi-station/"),
        ("문정역", "/seoul/songpa-gu/station/munjeong-station/"),
        ("장지역", "/seoul/songpa-gu/station/jangji-station/"),
        ("복정역 인접 생활권", "/seoul/songpa-gu/station/bokjeong-nearby-area/"),
        ("거여역", "/seoul/songpa-gu/station/geoyeo-station/"),
        ("마천역", "/seoul/songpa-gu/station/macheon-station/"),
        ("올림픽공원역", "/seoul/songpa-gu/station/olympic-park-station/"),
    ]),
    ("생활권 안내", "/seoul/songpa-gu/area/", [
        ("생활권 전체", "/seoul/songpa-gu/area/"),
        ("잠실·롯데월드 생활권", "/seoul/songpa-gu/area/jamsil-lotte-world/"),
        ("신천동·잠실 업무권", "/seoul/songpa-gu/area/sincheon-jamsil-business/"),
        ("석촌호수·송리단길 생활권", "/seoul/songpa-gu/area/seokchon-lake-songridan/"),
        ("방이동 먹자골목 생활권", "/seoul/songpa-gu/area/bangi-food-street/"),
        ("올림픽공원·오륜 생활권", "/seoul/songpa-gu/area/olympic-park-oryun/"),
        ("문정법조단지 생활권", "/seoul/songpa-gu/area/munjeong-law-town/"),
        ("가락시장·경찰병원 생활권", "/seoul/songpa-gu/area/garak-market-police-hospital/"),
        ("위례·장지 생활권", "/seoul/songpa-gu/area/wirye-jangji/"),
        ("거여·마천 생활권", "/seoul/songpa-gu/area/geoyeo-macheon/"),
        ("풍납·잠실나루 생활권", "/seoul/songpa-gu/area/pungnap-jamsillaru/"),
        ("송파대로 중심 생활권", "/seoul/songpa-gu/area/songpa-daero/"),
    ]),
    ("테마별 안내", "/themes/", [
        ("전체 테마", "/themes/"),
        ("스웨디시", "/themes/swedish/"),
        ("로미로미", "/themes/lomilomi/"),
        ("타이마사지", "/themes/thai/"),
        ("중국마사지", "/themes/chinese/"),
        ("아로마테라피", "/themes/aroma/"),
        ("홈케어", "/themes/homecare/"),
        ("호텔식마사지", "/themes/hotel-style/"),
        ("발마사지", "/themes/foot/"),
        ("스포츠·경락", "/themes/sports/"),
        ("스킨케어", "/themes/skincare/"),
        ("왁싱", "/themes/waxing/"),
        ("커플 관리", "/themes/couple/"),
        ("24시간", "/themes/24hours/"),
        ("수면 가능", "/themes/overnight/"),
    ]),
    ("코스안내", "/courses/", [
        ("전체 코스", "/courses/"),
        ("피로 회복 관리", "/courses/#recovery"),
        ("아로마 관리", "/courses/#aroma"),
        ("스포츠 관리", "/courses/#sports"),
        ("홈타이 코스", "/courses/#hometai"),
        ("커플·가족 방문 관리", "/courses/#couple"),
        ("기업·단체 방문 관리", "/courses/#group"),
        ("가격 안내", "/courses/#price"),
        ("코스 선택 가이드", "/courses/#guide"),
    ]),
    ("예약안내", "/reservation/", [
        ("예약 방법", "/reservation/#how"),
        ("예약 가능 시간", "/reservation/#hours"),
        ("방문 가능 장소", "/reservation/#place"),
        ("결제 안내", "/reservation/#payment"),
        ("변경·취소 안내", "/reservation/#change"),
        ("예약 전 체크사항", "/reservation/#check"),
    ]),
    ("이용가이드", "/guide/", [
        ("처음 이용하시는 분", "/guide/#first"),
        ("방문 전 준비사항", "/guide/#prepare"),
        ("위생 및 안전 기준", "/guide/#hygiene"),
        ("관리 후 주의사항", "/guide/#after"),
        ("금지행위 안내", "/guide/#prohibited"),
        ("이용 FAQ", "/guide/#faq"),
    ]),
    ("매거진", "/magazine/", [
        ("전체 글", "/magazine/"),
        ("마사지 비교 가이드", "/magazine/swedish-vs-thai/"),
        ("처음 이용 가이드", "/magazine/first-time-guide/"),
        ("수면과 마사지", "/magazine/sleep-and-massage/"),
        ("운동 후 회복", "/magazine/post-workout-timing/"),
        ("어깨·목 결림 관리", "/magazine/neck-shoulder-care/"),
        ("부모님 선물 가이드", "/magazine/parents-gift/"),
    ]),
    ("후기", "/reviews/", [
        ("전체 후기", "/reviews/"),
        ("지역별 후기", "/reviews/#area"),
        ("역세권 후기", "/reviews/#station"),
        ("후기 작성 안내", "/reviews/#write"),
    ]),
    ("고객센터", "/support/", [
        ("공지사항", "/support/#notice"),
        ("자주 묻는 질문", "/support/#faq"),
        ("1:1 문의", "/support/#contact"),
        ("제휴·기업 문의", "/support/#biz"),
        ("개인정보처리방침", "/support/privacy/"),
        ("이용약관", "/support/terms/"),
    ]),
]
