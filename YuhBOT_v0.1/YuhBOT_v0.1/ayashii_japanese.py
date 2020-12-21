import urllib
import ssl
import error_log
ssl._create_default_https_context = ssl._create_unverified_context  #非暗号化サイトも読み込めるように

print(f"<<{str(__name__)}.py>>Module was loaded")

#怪しい日本語(はむすけさん提供)
def convert(TadasiiNihongo) -> str:
    try:
        html = urllib.request.urlopen(urllib.request.Request('https://nnn1590.org/correctJP/', urllib.parse.urlencode({'main': TadasiiNihongo}).encode('utf-8'))).read().decode('utf-8')
        return str(html[html.find('<textarea') + 38 : html.find('</textarea>')])
    except urllib.error.URLError as err:
        error_log.error_log("ayashii_japanese",str(err))
        return "[Error] サーバーに接続できませんでした、時間を空けてもう一度お試しください"
