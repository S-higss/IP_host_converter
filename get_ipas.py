import os, tldextract, requests, re, socket, random
from lib.config.config import load_config
from domain.consts import SystemConstants
from urllib.parse import urlparse

class GetIPAS:
    def __init__(self, url_file, output_file):
        os.makedirs(SystemConstants.data_path, exist_ok=True)
        # URLのみが記載されたファイルのパス
        self.url_file = url_file
        # 検索結果を出力するファイルのパス
        self.output_file = output_file
        pass

    # register_init.txt内を正規化する関数
    def normalization(self):
        # register_init.txt内のリンクのリスト
        link_list = []

        # register_init.txtファイルから登録対象のurlを読み込む
        try:
            with open(self.url_file, "r") as f:
                link_list = [url.strip() for url in f.readlines() if url.strip()]
        except FileNotFoundError as e:
            print(e)
            print('\033[31m'+'ERROR: Cannot find register_init.txt. Create it first.'+'\033[0m')
            return
        
        # register_init.txtファイルを書き込みモードで開く
        with open(self.url_file, "w", encoding=SystemConstants.encode) as f:
            for link in link_list:
                # 末尾に/があれば削除
                norm = link.rstrip("/")
                f.write(f"{norm}\n")

    def get_IPAS(self):
        # register_init.txt内を正規化
        self.normalization()
        # ランダム整数のリスト
        randoms = []
        # 実行前に登録済みの辞書(URLを鍵とする)
        Registered = {}
        # 実行前に登録済みで，登録リストにも入っているURLのリスト
        Registered_list = []

        # register_init.txtファイルから登録対象のurlを読み込む
        try:
            with open(self.url_file, "r") as f:
                url_list = [url.strip() for url in f.readlines() if url.strip()]
        except FileNotFoundError as e:
            print(e)
            print('\033[31m'+'ERROR: Cannot find register_init.txt. Create it first.'+'\033[0m')
            return

        # register.txtファイルから登録済みのデータを読み込む
        try:
            with open(self.output_file, "r") as f:
                print('\033[33m'+'NOTICE: This is Additional registration'+'\033[0m')
                for line in f:
                    line = line.rstrip()
                    if line == "":
                        continue # 空行をスキップ
                    url, domain, asn, rand = line.split(",")
                    Registered[url] = [domain, asn, rand]
                    randoms.append(rand)
        except FileNotFoundError:
            print('\033[33m'+'NOTICE: This is Initial registration'+'\033[0m')
            pass

        # register.txtファイルを書き込みモードで開く
        with open(self.output_file, "w", encoding=SystemConstants.encode) as f:
            # 登録対象のurlリストから登録済みのURLを削除/そのURLをRegistered_listに保存
            for url in list(url_list):
                if url in Registered:
                    url_list.remove(url)
                    Registered_list.append(url)

            # 登録済みだが，登録対象に入っていないURLの削除
            ## ->登録対象以外の情報も入っていたRegistered内は登録対象のみとなる．
            for url in list(Registered.keys()):
                if url not in Registered_list:
                    del Registered[url]
                    
            # 登録済みのデータを先に登録
            for url in Registered:
                f.write(url + ',' + Registered[url][0] + ',' + Registered[url][1] + ',' + Registered[url][2] + '\n')
                
            # 登録対象のURLが全て登録済みの場合，以降の処理を省略.
            if len(url_list) == 0:
                return
            
            # 各URLについて処理を実行
            for url in url_list:
                # URLから第三レベルドメインを抜き出す
                ext = tldextract.extract(url)
                third_level_domain = ext.domain
                # 第三レベルドメインをsqlite3の正規表現にする
                norm_third_level_domain = re.sub(r'[/:%#\$&\?\(\)~\.=\+]+', '', third_level_domain.replace('-', '_'))

                # URLからIPアドレスを検索
                parsed_url = urlparse(url)
                domain = parsed_url.netloc
                ip = socket.gethostbyname(domain)
                # IPアドレスを用いてAS番号を検索する
                response = requests.get(f"https://ipinfo.io/{ip}/org")
                result = response.text.strip()
                match = re.search(r"AS(\d+)",result)
                if match:
                    asn = match.group(1)
                else:
                    # AS番号が検索できなかった場合0をAS番号とする
                    asn = "0"
                    print(f"[ERROR]-Domain:{domain}--Can't find AS number.")

                # 重複しないランダムな整数を生成
                while True:
                    rand = random.randint(1, 1000)
                    if rand not in randoms:
                        break
                randoms.append(rand)
                
                # 末尾に/があれば削除
                url = url.rstrip("/")

                # URLと第三レベルドメイン及びAS番号をカンマ区切りでsearch_result.txtに書き込む
                f.write(url.strip() + ',' + norm_third_level_domain + ',' + asn + ',' + str(rand) + '\n')
                
if __name__ == "__main__":
    config = load_config(SystemConstants.config)

    url_file = config["data"]["register_init"]
    output_file = config["data"]["register"]

    ins = GetIPAS(url_file, output_file)
    ins.get_IPAS()