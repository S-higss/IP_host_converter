import os, requests
from lib.config.config import load_config
from domain.consts import SystemConstants

class GetAS:
    def __init__(self):
        pass

    def get_AS(self, ip):
        # register.txtファイルを書き込みモードで開く
            # IPアドレスを用いてAS番号,ISPを検索する
            response = requests.get(f"https://ipinfo.io/{ip}/org")
            result = response.text.strip()

            # ipと第三レベルドメイン及びAS番号をカンマ区切りでsearch_result.txtに書き込む
            print(result + '\n')
                
if __name__ == "__main__":
    while(1):
        ip = input("IP: ")
        ins = GetAS()
        ins.get_AS(ip=ip)