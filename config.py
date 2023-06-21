

class Config :

    # DB 관련정보

    HOST = 'yhdb1004.co4tgwoguyyt.ap-northeast-2.rds.amazonaws.com'
    DATABASE = 'memo_db2'
    DB_USER = 'memo_db2_user'
    DB_PASSWORD = '1234'

    SALT = '0619@HELLO~'


    # JWT 변수 셋팅 ( ID 암호화 )
    JWT_SECRET_KEY = 'hello~!by@' # 아무글자 또는 기호를 넣어준다.
    JWT_ACCESS_TOKEN_EXPIRES = False   # 자동로그인 해제 또는 유지하도록 세팅
    PROPAGATE_EXCEPTIONS = True