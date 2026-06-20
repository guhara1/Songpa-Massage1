# 메인 페이지 — 허브 역할. 모든 키워드를 밀어 넣지 않고 상세 페이지로 연결한다.
# 실제 오프라인 사업장 주소가 없는 방문형 사이트이므로 LocalBusiness 대신
# Organization·WebPage·BreadcrumbList·FAQPage 스키마를 사용한다.
from .site import BASE_URL, BRAND, PHONE, PHONE_DISPLAY
from .pricing import PRICING

_JSONLD = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{BRAND}",
  "url": "{BASE_URL}/",
  "telephone": "{PHONE}",
  "logo": {{
    "@type": "ImageObject",
    "url": "{BASE_URL}/assets/og-image.png",
    "width": 1200,
    "height": 630
  }},
  "image": "{BASE_URL}/assets/og-image.png",
  "description": "송파구 전지역 방문 출장마사지·홈타이 예약 안내",
  "areaServed": {{
    "@type": "AdministrativeArea",
    "name": "서울특별시 송파구"
  }},
  "contactPoint": {{
    "@type": "ContactPoint",
    "telephone": "{PHONE}",
    "contactType": "reservations",
    "availableLanguage": "Korean"
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "송파구 출장마사지·홈타이 지역별 예약 안내",
  "url": "{BASE_URL}/",
  "primaryImageOfPage": {{
    "@type": "ImageObject",
    "url": "{BASE_URL}/assets/og-image.png"
  }},
  "breadcrumb": {{ "@id": "{BASE_URL}/#breadcrumb" }},
  "inLanguage": "ko-KR"
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "@id": "{BASE_URL}/#breadcrumb",
  "itemListElement": [
    {{ "@type": "ListItem", "position": 1, "name": "홈", "item": "{BASE_URL}/" }},
    {{ "@type": "ListItem", "position": 2, "name": "송파구 지역별 안내", "item": "{BASE_URL}/seoul/songpa-gu/" }}
  ]
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "송파구 전지역 방문이 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 지역별 안내에서 잠실동, 문정동, 가락동, 방이동, 위례동 등 14개 대표동 기준으로 확인할 수 있습니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "잠실역이나 문정역 근처도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "잠실역, 문정역, 가락시장역, 석촌역 등 주요 역세권은 역 상세 페이지에서 주변 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "잠실2동, 잠실3동은 왜 따로 없나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "잠실본동부터 잠실7동까지 번호 행정동은 잠실동 대표 페이지와 신천동·잠실 생활권에서 통합 안내하여 중복 페이지 위험을 줄입니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "당일 예약도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "가능할 수 있지만 저녁 시간대와 주말은 문의가 많을 수 있어 사전 예약을 권장합니다."
      }}
    }}
  ]
}}
</script>
"""

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Premium Visiting Spa · 송파구 전지역</p>
    <h1>송파구 출장마사지·홈타이<br>지역별 예약 안내</h1>
    <p class="hero-lead">샵까지 갈 필요 없이, 계신 곳에서 받는 프리미엄 방문 관리.<br>자택·오피스텔·숙소 어디든 전화 한 통이면 예약이 끝납니다.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="/seoul/songpa-gu/">지역별 안내 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>14개</strong><span>대표동</span></li>
      <li><strong>18개</strong><span>역세권</span></li>
      <li><strong>11개</strong><span>생활권</span></li>
      <li><strong>24시간</strong><span>예약 상담</span></li>
    </ul>
  </div>
</section>
"""

_BODY = f"""
<section id="standard">
<h2>송파구에서 출장마사지를 찾을 때 먼저 확인할 기준</h2>
<p>송파구 출장마사지를 찾는 분들은 보통 현재 위치에서 가까운 방문 가능 지역을 먼저 확인합니다. 송파구는 서울 동남권의 자치구로, 잠실역과 롯데월드를 중심으로 한 대형 상권, 석촌호수와 송리단길 주변 생활권, 문정법조단지와 장지역 주변의 업무·주거 생활권, 가락시장과 경찰병원 주변 역세권, 거여·마천·위례로 이어지는 주거 생활권이 함께 있습니다. 그래서 단순히 "송파 전지역 가능"만 적기보다 대표동과 역세권, 생활권을 나누어 안내하는 구조가 정확합니다. {BRAND}는 예약 확인부터 방문 관리까지 정해진 절차에 따라 진행하며, 더 자세한 내용은 <a href="/seoul/songpa-gu/">송파구 지역별 안내</a>와 <a href="/massage/">송파 출장마사지 안내</a>에서 확인하실 수 있습니다.</p>
</section>

<section id="districts">
<h2>잠실·문정·가락·방이·위례 생활권 차이</h2>
<p>같은 송파구라도 생활권마다 분위기와 방문 조건이 다릅니다. <a href="/seoul/songpa-gu/area/jamsil-lotte-world/">잠실·롯데월드 생활권</a>은 상권과 숙소 방문이 많고, <a href="/seoul/songpa-gu/area/munjeong-law-town/">문정법조단지 생활권</a>은 업무 지구 특성상 평일 저녁 수요가 높습니다. <a href="/seoul/songpa-gu/area/garak-market-police-hospital/">가락시장·경찰병원 생활권</a>은 새벽·심야 생활 리듬이 뚜렷하고, <a href="/seoul/songpa-gu/area/bangi-food-street/">방이동 먹자골목 생활권</a>과 <a href="/seoul/songpa-gu/area/seokchon-lake-songridan/">석촌호수·송리단길 생활권</a>은 모임 뒤 자택·숙소 방문이 잦습니다. <a href="/seoul/songpa-gu/area/wirye-jangji/">위례·장지 생활권</a>과 <a href="/seoul/songpa-gu/area/geoyeo-macheon/">거여·마천 생활권</a>은 주거 중심이라 차량 이동 기준을 더 자세히 안내합니다. 생활권 전체 구성은 <a href="/seoul/songpa-gu/area/">생활권 안내</a>에서 한눈에 보실 수 있습니다.</p>
</section>

<section id="areas">
<h2>대표동별 방문 가능 지역 안내</h2>
<p>지역별 안내는 잠실동, 방이동, 오륜동, 오금동, 송파동, 석촌동, 삼전동, 가락동, 문정동, 장지동, 위례동, 풍납동, 거여동, 마천동 14개 대표동을 기준으로 구성됩니다. 잠실본동·잠실2동·잠실3동·잠실7동, 가락본동·가락1동·가락2동, 문정1동·문정2동처럼 번호로 나뉜 행정동은 별도 페이지를 만들지 않고 각 대표동 페이지에서 통합 안내합니다. 아래에서 거주하시거나 머무시는 동을 선택해 주세요.</p>
<ul class="card-grid">
<li><a href="/seoul/songpa-gu/jamsil-dong/">잠실동</a></li>
<li><a href="/seoul/songpa-gu/bangi-dong/">방이동</a></li>
<li><a href="/seoul/songpa-gu/oryun-dong/">오륜동</a></li>
<li><a href="/seoul/songpa-gu/ogeum-dong/">오금동</a></li>
<li><a href="/seoul/songpa-gu/songpa-dong/">송파동</a></li>
<li><a href="/seoul/songpa-gu/seokchon-dong/">석촌동</a></li>
<li><a href="/seoul/songpa-gu/samjeon-dong/">삼전동</a></li>
<li><a href="/seoul/songpa-gu/garak-dong/">가락동</a></li>
<li><a href="/seoul/songpa-gu/munjeong-dong/">문정동</a></li>
<li><a href="/seoul/songpa-gu/jangji-dong/">장지동</a></li>
<li><a href="/seoul/songpa-gu/wirye-dong/">위례동</a></li>
<li><a href="/seoul/songpa-gu/pungnap-dong/">풍납동</a></li>
<li><a href="/seoul/songpa-gu/geoyeo-dong/">거여동</a></li>
<li><a href="/seoul/songpa-gu/macheon-dong/">마천동</a></li>
</ul>
<p>송파구 전체 구조가 궁금하시면 <a href="/seoul/songpa-gu/">송파구 지역별 안내</a>에서 한눈에 확인하실 수 있습니다. 행정 구역 기준은 <a href="https://www.songpa.go.kr/" target="_blank" rel="noopener">송파구청 공식 누리집</a>에서도 확인하실 수 있습니다.</p>
</section>

<section id="stations">
<h2>잠실역·문정역·가락시장역·석촌역 역세권 안내</h2>
<p>역세권 안내는 송파구를 지나는 2·3·5·8·9호선 주요 역을 기준으로 구성합니다. 각 역 페이지에서는 인근 생활권, 주변 대표동, 예약 가능 시간, 방문 전 준비사항을 설명하며, 출구별 페이지나 역과 테마를 조합한 페이지는 만들지 않습니다. 잠실역, 석촌역, 가락시장역, 오금역, 올림픽공원역처럼 환승 성격이 있는 역도 역명 기준 1개 페이지만 운영합니다.</p>
<ul class="card-grid">
<li><a href="/seoul/songpa-gu/station/jamsil-station/">잠실역</a></li>
<li><a href="/seoul/songpa-gu/station/jamsilsaenae-station/">잠실새내역</a></li>
<li><a href="/seoul/songpa-gu/station/jamsillaru-station/">잠실나루역</a></li>
<li><a href="/seoul/songpa-gu/station/songpanaru-station/">송파나루역</a></li>
<li><a href="/seoul/songpa-gu/station/seokchon-station/">석촌역</a></li>
<li><a href="/seoul/songpa-gu/station/garak-market-station/">가락시장역</a></li>
<li><a href="/seoul/songpa-gu/station/munjeong-station/">문정역</a></li>
<li><a href="/seoul/songpa-gu/station/jangji-station/">장지역</a></li>
<li><a href="/seoul/songpa-gu/station/olympic-park-station/">올림픽공원역</a></li>
</ul>
<p>전체 18개 역 안내는 <a href="/seoul/songpa-gu/station/">역세권 안내</a>에서 확인하실 수 있습니다.</p>
</section>

<section id="check">
<h2>송파구 홈타이 예약 전 확인사항</h2>
<p>송파구 출장마사지·홈타이 예약 전에는 방문 가능 지역, 예약 가능 시간, 추가 이동비, 결제 방식, 취소 기준, 개인정보 처리 기준을 먼저 확인하는 것이 좋습니다. 잠실역과 문정역처럼 접근성이 좋은 지역도 있지만, 위례동·마천동·풍납동 일부 주거지는 시간대에 따라 차량 이동 기준이 달라질 수 있습니다. 홈타이는 자택, 숙소, 사무실 인근에서 예약 가능 여부를 확인한 뒤 이용하는 방문형 관리 서비스입니다. 자세한 절차는 <a href="/reservation/">예약안내</a>와 <a href="/guide/">이용가이드</a>에서, 홈타이 자체에 대한 설명은 <a href="/massage/#hometai">홈타이 안내</a>에서 확인해 주세요.</p>
</section>

<section id="dedup">
<h2>송파구 페이지 중복 방지 운영 기준</h2>
<p>송파구 사이트에서 가장 중요한 것은 번호 동을 무리하게 쪼개지 않는 것입니다. 풍납1동·풍납2동, 거여1동·거여2동, 마천1동·마천2동, 방이1동·방이2동, 송파1동·송파2동, 가락본동·가락1동·가락2동, 문정1동·문정2동을 각각 개별 페이지로 만들면 본문이 비슷해질 위험이 큽니다. 그래서 대표동으로 통합하고 각 페이지 안에서 세부 생활권을 설명합니다. 잠실본동·잠실2동·잠실3동·잠실7동은 <a href="/seoul/songpa-gu/jamsil-dong/">잠실동</a> 대표 페이지에서, 잠실4동·잠실6동·신천동 생활권은 <a href="/seoul/songpa-gu/area/sincheon-jamsil-business/">신천동·잠실 업무권</a>에서 나누어 설명합니다. 환승역도 노선별로 쪼개지 않고 역명 기준 1개 페이지로 운영하며, 복정역은 송파구·성남 경계 성격이 있어 <a href="/seoul/songpa-gu/station/bokjeong-nearby-area/">장지·위례 인접 생활권</a>으로 처리합니다.</p>
</section>

<section id="how">
<h2>송파구 출장마사지 사이트 이용 방법</h2>
<p>이용 흐름은 간단합니다. 먼저 거주하시거나 머무시는 위치를 <a href="/seoul/songpa-gu/">대표동</a> 또는 <a href="/seoul/songpa-gu/station/">역세권</a>에서 찾고, 원하시는 관리 유형을 <a href="/themes/">테마별 안내</a>에서 고른 뒤, <a href="/reservation/">예약안내</a> 절차에 따라 전화로 예약하시면 됩니다. 메인 페이지는 송파구 전체 안내를 담당하고, 대표동 페이지는 잠실동·방이동·송파동·가락동·문정동 같은 세부 검색을, 역세권 페이지는 잠실역·석촌역·송파나루역·가락시장역 같은 실제 검색 수요를 담당합니다. 처음 이용하시는 분도 어렵지 않게 예약할 수 있도록 각 단계를 명확하게 안내해 드립니다.</p>
</section>

{PRICING}
<section id="contact" class="cta">
<h2>예약문의</h2>
<p>송파구 방문 관리 예약과 상담은 전화로 가장 빠르게 진행됩니다. 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "송파구 출장마사지｜잠실·문정·가락·위례 홈타이 지역 안내",
    "desc": "송파구 출장마사지·홈타이 예약 전 잠실, 문정, 가락, 방이, 위례 생활권을 확인하세요.",
    "h1": "송파구 출장마사지 · 송파구 홈타이 지역별 예약 안내",
    "body": _BODY,
    "extra_head": _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
