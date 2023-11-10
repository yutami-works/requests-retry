import json     # TODO:レスポンスの扱い
import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

def requests_get_retry(url: str):
    # セッション
    session = requests.session()

    # オプション
    retries = Retry(
        total=10,                                  # リトライ回数
        backoff_factor=30,                         # 待機時間係数
        status_forcelist=[429, 500, 502, 503, 504] # 対象ステータスコード
    )

    # アダプター設定
    session.mount("http://", HTTPAdapter(max_retries=retries))

    # リクエスト
    response = session.get(
        url=url,
        stream=True,         # イテレータ
        timeout=(10.0, 30.0) # connect timeout, read timeout
    )

    return response

endpoint = "https://zipcloud.ibsnet.co.jp/api/search?zipcode=2100003"

try:
    res = requests_get_retry(url=endpoint)
    print(res.status_code)
    print(res.text)
except:
    print(res)