from flask import Blueprint
from bs4 import BeautifulSoup
import json
import requests
from pymongo import MongoClient
import time
from pymongo.cursor import CursorType

# Blueprint(이름, 모듈명, url 프리픽스)
bp = Blueprint('crawling', __name__, url_prefix='/')
separator = '$$$'

# mongo
mongo = MongoClient("")
test = mongo['test']
bjh = test['bjh']


# 해당 url의 html을 BeautifulSoup 객체로 리턴
def get_html(url: str) -> BeautifulSoup:
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    return soup


# soup 객체에서 특정 css data 리턴
def select_area(area_css: str, soup: BeautifulSoup) -> list:
    html = soup.select(area_css)
    rtn = []

    for row in html:
        row = row.get_text(separator, strip=True).split(separator)
        for i in range(len(row)):
            if not str(row[i])[0].isdigit():
                rtn.append({"area": row[i], "total": str(row[i + 1]).replace(',', '')})

    return rtn


@bp.route('/crawling')
def crawling():
    soup = get_html("http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubu"
                    "n=")

    seoul = select_area("div#zone_popup1 tbody", soup)
    busan = select_area("div#zone_popup2 tbody", soup)
    daegu = select_area("div#zone_popup3 tbody", soup)
    incheon = select_area("div#zone_popup4 tbody", soup)
    gwangju = select_area("div#zone_popup5 tbody", soup)
    daejeon = select_area("div#zone_popup6 tbody", soup)
    ulsan = select_area("div#zone_popup7 tbody", soup)
    sejong = select_area("div#zone_popup8 tbody", soup)
    gyeonggi = select_area("div#zone_popup9 tbody", soup)
    gangwon = select_area("div#zone_popup10 tbody", soup)
    chungbuk = select_area("div#zone_popup11 tbody", soup)
    chungnam = select_area("div#zone_popup12 tbody", soup)
    jeonbuk = select_area("div#zone_popup13 tbody", soup)
    jeonnam = select_area("div#zone_popup14 tbody", soup)
    gyeongbuk = select_area("div#zone_popup15 tbody", soup)
    gyeongnam = select_area("div#zone_popup16 tbody", soup)
    jeju = select_area("div#zone_popup17 tbody", soup)

    '''
    data = json.dumps({'seoul': seoul, 'busan': busan, 'daegu': daegu, 'incheon': incheon,
                       'gwangju': gwangju, 'daejeon': daejeon, 'ulsan': ulsan, 'sejong': sejong,
                       'gyeonggi': gyeonggi, 'gangwon': gangwon, 'chungbuk': chungbuk, 'chungnam': chungnam,
                       'jeonbuk': jeonbuk, 'jeonnam': jeonnam, 'gyeongbuk': gyeongbuk, 'gyeongnam': gyeongnam,
                       'jeju': jeju}, indent=4, ensure_ascii=False)
    '''

    bjh.insert({'date': '2021-06-15', 'seoul': seoul, 'busan': busan, 'daegu': daegu, 'incheon': incheon,
                'gwangju': gwangju, 'daejeon': daejeon, 'ulsan': ulsan, 'sejong': sejong,
                'gyeonggi': gyeonggi, 'gangwon': gangwon, 'chungbuk': chungbuk, 'chungnam': chungnam,
                'jeonbuk': jeonbuk, 'jeonnam': jeonnam, 'gyeongbuk': gyeongbuk, 'gyeongnam': gyeongnam,
                'jeju': jeju})

    return 'success'


@bp.route('/mongoSelect')
def select():

    result = bjh.find({'date': '2021-06-13'})
    print(result)
    for val in result:
        print(val)

    return 'select'

