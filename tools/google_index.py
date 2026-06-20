#!/usr/bin/env python3
"""구글 Indexing API 로 즉시 크롤 요청 — (선택) 구글은 IndexNow 미참여.

구글은 IndexNow 에 참여하지 않으므로, 구글 색인을 빠르게 하려면
(1) 서치콘솔에 sitemap.xml 제출(기본), (2) 본 Indexing API(선택) 를 씁니다.

※ 주의: Indexing API 는 공식적으로 JobPosting/BroadcastEvent 용도입니다.
   일반 페이지에도 크롤 요청이 동작하지만 구글 정책상 보장되지 않습니다.
   가장 확실한 방법은 서치콘솔 sitemap 제출 + URL 검사 도구입니다.

사전 준비:
  1) Google Cloud 프로젝트에서 'Indexing API' 활성화
  2) 서비스 계정 생성 → JSON 키 다운로드
  3) 서치콘솔 속성에 그 서비스 계정 이메일을 '소유자'로 추가
  4) pip install google-auth requests

사용법:
  export GOOGLE_APPLICATION_CREDENTIALS=/path/service-account.json
  python tools/google_index.py                 # 사이트맵 전체
  python tools/google_index.py <URL> [<URL> ...]  # 특정 URL
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from content.site import BASE_URL  # noqa: E402

ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]


def urls_from_sitemap():
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 `python build.py` 를 실행하세요.")
    return re.findall(r"<loc>(.*?)</loc>", open(path, encoding="utf-8").read())


def main():
    try:
        import requests
        from google.oauth2 import service_account
        from google.auth.transport.requests import AuthorizedSession
    except ImportError:
        sys.exit("pip install google-auth requests 가 필요합니다.")

    cred_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred_path or not os.path.exists(cred_path):
        sys.exit("GOOGLE_APPLICATION_CREDENTIALS 환경변수에 서비스 계정 JSON 경로를 지정하세요.")

    creds = service_account.Credentials.from_service_account_file(cred_path, scopes=SCOPES)
    session = AuthorizedSession(creds)

    urls = sys.argv[1:] or urls_from_sitemap()
    host = re.sub(r"^https?://", "", BASE_URL).split("/")[0]
    urls = [u for u in urls if host in u]
    print(f"구글 Indexing API 로 {len(urls)}개 URL 요청")

    ok = 0
    for u in urls:
        r = session.post(ENDPOINT, json={"url": u, "type": "URL_UPDATED"})
        tag = "OK" if r.status_code == 200 else f"ERR {r.status_code}"
        print(f"  [{tag}] {u}")
        if r.status_code == 200:
            ok += 1
        elif r.status_code == 429:
            print("  일일 할당량 초과(기본 200/일). 내일 다시 시도하세요.")
            break
    print(f"완료: {ok}/{len(urls)} 성공")


if __name__ == "__main__":
    main()
