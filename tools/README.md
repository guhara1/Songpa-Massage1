# 색인(인덱싱) 자동화 도구

송파 출장마사지 사이트의 빠른 색인을 위한 도구 모음입니다.

## 0. 매번의 흐름 요약

```bash
python build.py                 # 사이트 + sitemap.xml + rss.xml + IndexNow 키파일 생성
git add -A && git commit -m "..." && git push   # 배포(Cloudflare Pages 자동 반영)
python tools/indexnow.py        # 빙·네이버 등에 전체 URL 즉시 통보
# (새 글만 통보) python tools/indexnow.py <새 글 URL>
```

## 1. 검색엔진 소유확인 + 사이트맵 등록 (가장 먼저, 1회)

빠른 색인의 90%는 "사이트맵을 콘솔에 제출"하는 데서 나옵니다.

- **네이버 서치어드바이저** (https://searchadvisor.naver.com)
  - 사이트 등록 → 소유확인. `content/site.py` 의 `NAVER_VERIFY` 값이 모든 페이지
    `<head>` 에 `naver-site-verification` 메타로 이미 삽입되어 있습니다.
  - 요청 → 사이트맵 제출: `https://songpa-massage1.pages.dev/sitemap.xml`
  - 요청 → RSS 제출: `https://songpa-massage1.pages.dev/rss.xml`
- **구글 서치콘솔** (https://search.google.com/search-console)
  - 'HTML 태그' 방식으로 확인하려면 `content/site.py` 의 `GOOGLE_VERIFY` 에
    값을 넣고 `python build.py` 재실행 → 배포 후 확인.
  - Sitemaps 메뉴에 `sitemap.xml` 제출.
- **빙 웹마스터** (https://www.bing.com/webmasters) — 사이트맵 제출(선택, IndexNow 와 별개).

## 2. IndexNow — 빙·네이버 즉시 통보 (추가 설치 없음)

`build.py` 가 루트에 `사이트맵키.txt`(IndexNow 키 파일)를 자동 생성합니다.
키는 `content/site.py` 의 `INDEXNOW_KEY` 에 있고, 키 파일 URL 은
`https://songpa-massage1.pages.dev/<KEY>.txt` 입니다.

```bash
# 최초 일괄 통보 — 사이트맵의 모든 URL
python tools/indexnow.py

# 글 올릴 때마다 — 바뀐 URL만 통보
python tools/indexnow.py https://songpa-massage1.pages.dev/magazine/<새글>/

# 보낼 내용만 미리보기
python tools/indexnow.py --dry-run
```

`api.indexnow.org` 한 곳에 보내면 IndexNow 참여 엔진(빙·네이버·얀덱스 등)
전체로 분배됩니다. 200/202 응답이면 정상 접수입니다.

## 3. (선택) 구글 Indexing API — 구글 즉시 크롤 요청

구글은 IndexNow 에 참여하지 않습니다. 구글 색인은 **서치콘솔 사이트맵 제출**이
기본이고, 더 빠르게 하려면 Indexing API 를 추가로 쓸 수 있습니다.

```bash
pip install google-auth requests
export GOOGLE_APPLICATION_CREDENTIALS=/path/service-account.json
python tools/google_index.py            # 사이트맵 전체
python tools/google_index.py <URL> ...  # 특정 URL
```

준비: Google Cloud 에서 Indexing API 활성화 → 서비스 계정 JSON 키 →
서치콘솔 속성에 그 서비스 계정을 '소유자'로 추가. (일일 기본 할당량 200건)

> 참고: 구글·빙의 옛 `?ping=sitemap` 핑 방식은 2023년에 폐기되었습니다.
> 지금의 "가장 빠른" 경로는 **콘솔 사이트맵 제출 + IndexNow + (구글)Indexing API** 입니다.
