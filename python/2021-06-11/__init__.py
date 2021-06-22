# --------------------------------- [edit] ---------------------------------- #
'''

app = Flask(__name__)은 플라스크 애플리케이션을 생성하는 코드다.
이 코드에서 __name__이라는 변수에는 모듈명이 담긴다. 즉,
이 파일이 실행되면 main.py라는 모듈이 실행되는 것이므로 __name__ 변수에는 ‘main’라는 문자열이 담긴다.
@app.route는 특정 주소에 접속하면 바로 다음 줄에 있는 함수를 호출하는 플라스크의 데코레이터다.

'''

from flask import Flask

def create_app():
    app = Flask(__name__)

    # 블루 프린트
    from views import main_views
    app.register_blueprint(main_views.bp)

    from crawling import crawling
    app.register_blueprint(crawling.bp)

    return app
# --------------------------------------------------------------------------- #