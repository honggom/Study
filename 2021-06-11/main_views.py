from flask import Blueprint
from config import config
import json


#Blueprint(이름, 모듈명, url 프리픽스)
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'hello pypy'

@bp.route('/')
def index():
    
    #config 정보 가져오기
    cur = config.db.cursor()

    #쿼리 실행
    cur.execute("select * from orn limit 0, 5")

    #쿼리 결과 data return
    rtn = json.dumps({"data" : cur.fetchall(), 'result_status': 'OK'}, indent=4, ensure_ascii=False)
    print(cur.statement)
    print(rtn)
    return rtn
