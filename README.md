# 바로GO — 송파 출장마사지·홈타이 안내 사이트

송파구 전지역 방문 관리(출장마사지·홈타이) 안내용 정적 사이트입니다.
예약전화: **0508-202-4719**

## 구조

- 정적 HTML 사이트 — 어느 호스팅(GitHub Pages, Netlify, 일반 웹서버)에서든 그대로 서빙 가능
- `build.py` + `content/` 패키지에서 페이지를 생성하는 빌드 방식
- 생성물(각 디렉터리의 `index.html`, `sitemap.xml`, `robots.txt`)도 저장소에 포함

```
build.py            # 빌드 스크립트 (레이아웃·글자수·디스크립션 검사·sitemap 생성)
content/
  site.py           # 상호·전화·BASE_URL·텔레그램·메뉴 구조
  main.py           # 메인 페이지 (+ Organization/WebPage/BreadcrumbList/FAQPage JSON-LD)
  areas.py          # 지역별: 송파구 허브 + 대표동 14개
  stations.py       # 역세권: 허브 + 18개 역
  districts.py      # 생활권: 허브 + 11개 생활권
  themes.py         # 테마별: 허브 + 14개 테마
  info.py           # 출장마사지 안내·코스·예약·가이드·후기·고객센터·약관
assets/             # CSS(프리미엄 토큰·Pretendard), 모바일 내비 JS
```

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수와 80자 초과 디스크립션 경고가 출력됩니다.

## SEO 운영 원칙 (빌드에 강제됨)

- 본문 **2,000자 미만 페이지는 자동 `noindex`** 처리되고 sitemap에서 제외
- 메타 디스크립션은 **80자 이내** (빌드 시 초과분 경고)
- 지역은 대표동 14개만 — 숫자 행정동(잠실2동·가락1동 등) 개별 페이지 없음
- 역은 역 1개당 페이지 1개 — 환승역도 URL 하나, 출구별 페이지 없음
- 복정역은 송파·성남 경계라 장지·위례 인접 생활권으로 처리
- **지역+역+테마 조합 페이지 없음** (도어웨이 방지) — 테마는 독립 페이지로만 운영
- 상단/하위 메뉴와 푸터에 키워드("출장마사지") 대량 반복 없음 (지역명·역명만 표기)
- 모든 페이지 본문은 페이지별 고유 작성 (지역명만 바꾼 복붙 없음)

## URL 구조

- 메인: `/`
- 지역별 안내(허브): `/seoul/songpa-gu/`, 대표동: `/seoul/songpa-gu/jamsil-dong/` 등
- 역세권: `/seoul/songpa-gu/station/jamsil-station/` 등
- 생활권: `/seoul/songpa-gu/area/jamsil-lotte-world/` 등

## 배포 전 해야 할 일

1. `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경
2. `python3 build.py` 재실행 (canonical·sitemap·robots.txt에 반영됨)
3. Google Search Console에 `sitemap.xml` 제출
