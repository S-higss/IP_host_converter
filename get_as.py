import os, requests
from lib.config.config import load_config
from domain.consts import SystemConstants

class GetAS:
    def __init__(self, ip_file, output_file):
        os.makedirs(SystemConstants.data_path, exist_ok=True)
        # ipのみが記載されたファイルのパス
        self.ip_file = ip_file
        # 検索結果を出力するファイルのパス
        self.output_file = output_file
        pass

    def get_AS(self):
        # ip_list.txtファイルから登録対象のipを読み込む
        try:
            with open(self.ip_file, "r") as f:
                ip_list = [ip.strip() for ip in f.readlines() if ip.strip()]
        except FileNotFoundError as e:
            print(e)
            print('\033[31m'+'ERROR: Cannot find register_init.txt. Create it first.'+'\033[0m')
            return

        # register.txtファイルを書き込みモードで開く
        with open(self.output_file, "w", encoding=SystemConstants.encode) as f:            
            # 各ipについて処理を実行
            for ip in ip_list:
                # IPアドレスを用いてAS番号,ISPを検索する
                response = requests.get(f"https://ipinfo.io/{ip}/org")
                result = response.text.strip()

                # ipと第三レベルドメイン及びAS番号をカンマ区切りでsearch_result.txtに書き込む
                f.write(ip + ': ' + result + '\n')
                
if __name__ == "__main__":
    config = load_config(SystemConstants.config)

    ip_file = config["data"]["ip_list"]
    output_file = config["data"]["ip_as_list"]

    ins = GetAS(ip_file, output_file)
    ins.get_AS()