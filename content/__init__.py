# 전체 페이지 목록 집계
from . import main, areas, stations, districts, themes, info, magazine, about

PAGES = (
    [main.PAGE]
    + areas.PAGES
    + stations.PAGES
    + districts.PAGES
    + themes.PAGES
    + info.PAGES
    + magazine.PAGES
    + [about.PAGE]
)
