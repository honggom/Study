from flask import Blueprint
from bs4 import BeautifulSoup
import json
import requests

# Blueprint(이름, 모듈명, url 프리픽스)
bp = Blueprint('crawling02', __name__, url_prefix='/')
separator = '$$$'

#해당 url의 html을 BeautifulSoup 객체로 리턴
def get_html(url:str) -> BeautifulSoup:
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    return soup

#soup 객체에서 특정 css data 리턴
def select_area(area_css:str, soup:BeautifulSoup) -> list:
    html = soup.select(area_css)
    rtn = []

    for row in html:
        row = row.get_text(separator, strip=True).split(separator)
        for i in range(len(row)):
            if not str(row[i])[0].isdigit():
                rtn.append({"area": row[i], "total": str(row[i+1]).replace(',', '')})

    return rtn

@bp.route('/crawling02')
def crawling():
    soup = get_html("http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun=")

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

    return json.dumps({'seoul': seoul, 'busan': busan, 'daegu': daegu, 'incheon': incheon,
                       'gwangju': gwangju, 'daejeon': daejeon, 'ulsan': ulsan, 'sejong': sejong,
                       'gyeonggi': gyeonggi, 'gangwon': gangwon, 'chungbuk': chungbuk, 'chungnam': chungnam,
                       'jeonbuk': jeonbuk, 'jeonnam': jeonnam, 'gyeongbuk': gyeongbuk, 'gyeongnam': gyeongnam,
                       'jeju': jeju}, indent=4, ensure_ascii=False)

'''
@bp.route('/seoul')
def seoul():
    soup = get_html("https://www.seoul.go.kr/coronaV/coronaStatus.do")

    area_name_html_1 = soup.select("table.tstyle-status tr")[0]
    area_total_html_1 = soup.select("table.tstyle-status tr")[1]
    area_today_html_1 = soup.select("table.tstyle-status tr")[2]

    area_name_html_2 = soup.select("table.tstyle-status tr")[3]
    area_total_html_2 = soup.select("table.tstyle-status tr")[4]
    area_today_html_2 = soup.select("table.tstyle-status tr")[5]

    area_name_list = area_name_html_1.get_text(separator, strip=True).split(separator) + area_name_html_2.get_text(separator, strip=True).split(separator)
    total_list = area_total_html_1.get_text(separator, strip=True).split(separator) + area_total_html_2.get_text(separator, strip=True).split(separator)
    today_list = area_today_html_1.get_text(separator, strip=True).split(separator) + area_today_html_2.get_text(separator, strip=True).split(separator)

    rtn = []

    for index in range(len(area_name_list)):
        rtn.append({'area': area_name_list[index], 'today': today_list[index].replace("+", ""), 'total': total_list[index]})

    return json.dumps(rtn, indent=4, ensure_ascii=False)

@bp.route('/busan')
def busan():
    soup = get_html("https://www.busan.go.kr/covid19/Corona19.do")

    area_name_html = soup.select("div.covid-state-table thead")[0]
    area_count_html = soup.select("div.covid-state-table tbody tr")

    area_name_list = area_name_html.get_text(separator, strip=True).split(separator)
    today_list = area_count_html[0].get_text(separator, strip=True).split(separator)
    total_list = area_count_html[1].get_text(separator, strip=True).split(separator)

    rtn = []

    for index in range(1, len(area_name_list)):
        rtn.append({'area': area_name_list[index], 'today': today_list[index], 'total': total_list[index]})

    return json.dumps(rtn, indent=4, ensure_ascii=False)


@bp.route('/incheon')
def incheon():
    soup = get_html("https://www.incheon.go.kr/health/HE020409")

    html = soup.select("div.mob-scroll ul dl")

    for index in range(1, len(html)):
        print(html[index].get_text(separator, strip=True).split(separator))

    return None
'''

