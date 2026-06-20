#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 — 빙·네이버·얀덱스 등 IndexNow 참여 엔진에 한 번에 통보.

표준 라이브러리만 사용하므로 추가 설치가 필요 없습니다.

사용법:
  # 사이트맵의 모든 URL을 통보 (최초 일괄 통보)
  python tools/indexnow.py

  # 새 글/수정한 페이지만 통보 (글 올릴 때마다)
  python tools/indexnow.py https://songpa-massage1.pages.dev/seoul/songpa-gu/jamsil-dong/ \
                           https://songpa-massage1.pages.dev/magazine/first-time-guide/

  # 통보할 내용만 확인하고 실제 전송은 안 함
  python tools/indexnow.py --dry-run

엔드포인트(api.indexnow.org)는 참여 검색엔진 전체로 자동 분배됩니다.
네이버 서치어드바이저도 IndexNow를 지원하므로 함께 통보됩니다.
"""
import json
import os
import re
import sys
import urllib.request
import urllib.error

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.site import BASE_URL, INDEXNOW_KEY

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = BASE_URL.rstrip("/")
HOST = re.sub(r"^https?://", "", BASE).split("/")[0]
KEY_LOCATION = f"{BASE}/{INDEXNOW_KEY}.txt"

# 통보 엔드포인트 — 하나에 보내면 참여 엔진 전체로 분배된다.
ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow",
]


def urls_from_sitemap():
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 `python build.py` 를 실행하세요.")
    xml = open(path, encoding="utf-8").read()
    return re.findall(r"<loc>(.*?)</loc>", xml)


def submit(endpoint, urls):
    payload = json.dumps({
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }).encode("utf-8")
    req = urllib.request.Request(
        endpoint, data=payload,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.read().decode("utf-8", "ignore").strip()
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "ignore").strip()
    except Exception as e:  # noqa: BLE001
        return None, str(e)


def main():
    args = [a for a in sys.argv[1:] if a != "--dry-run"]
    dry = "--dry-run" in sys.argv

    urls = args if args else urls_from_sitemap()
    # 같은 호스트만 통보 (IndexNow 규칙)
    urls = [u for u in urls if HOST in u]
    if not urls:
        sys.exit("통보할 URL 이 없습니다.")

    print(f"host={HOST}  key={INDEXNOW_KEY[:8]}…  URL {len(urls)}개")
    for u in urls[:10]:
        print("  -", u)
    if len(urls) > 10:
        print(f"  … 외 {len(urls) - 10}개")

    if dry:
        print("[dry-run] 실제 전송하지 않았습니다.")
        return

    # IndexNow 는 1회 최대 10,000 URL. 안전하게 1,000 단위로 분할.
    for endpoint in ENDPOINTS:
        ok = True
        for i in range(0, len(urls), 1000):
            status, body = submit(endpoint, urls[i:i + 1000])
            print(f"[{endpoint}] {status} {body or 'OK'}")
            if status not in (200, 202):
                ok = False
        if ok:
            # 한 엔드포인트만 성공해도 전체 분배되므로 종료
            break


if __name__ == "__main__":
    main()
