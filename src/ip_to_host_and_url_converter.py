from domain.consts import SystemConstants
# import libs
from lib.config.config import load_config
# import modules
import time, socket
from src.progress_bar import Progbar
from src.url_maker import url_maker
from src.url_checker import is_valid_url

config = load_config(SystemConstants.config)

def convert_ip_to_url():
    # A text file containing IP addresses one line at a time
    ip_filename = config["data"]["ip_list"]
    # A text file containing hostname one line at a time
    output_hostname_filename = config["data"]["host_list"]
    # A text file containing valid url one line at a time
    output_url_filename = config["data"]["url_list"]

    total_lines = count_lines(ip_filename)
    with Progbar(total_lines) as pb:
        try:
            with open(ip_filename, 'r', encoding=SystemConstants.encode) as ip_file, open(output_hostname_filename, 'w', encoding=SystemConstants.encode) as hostname_file, open(output_url_filename, 'w', encoding=SystemConstants.encode) as url_file:
                i = 0
                for line in ip_file:
                    # ---convert ip to hostname---
                    pb.update(i, f"{i}/{total_lines} convert ip address to hostname...")
                    ip_address = line.strip()
                    hostname = resolve_ip(ip_address)
                    if hostname:
                        hostname_file.write(hostname + '\n')
                        # ---make valid url from hostname---
                        pb.update(i, f"{i}/{total_lines}  make valid url from hostname ...")
                        urls = url_maker(hostname)
                        valid_url = []
                        for url in urls:
                            if is_valid_url(url):
                                valid_url.append(url)
                        if valid_url:
                            url_file.write(valid_url[0] + '\n')
                    i += 1
                    pb.update(i, f"{i}/{total_lines}")
                    time.sleep(0.1)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

def resolve_ip(ip_address):
    try:
        # get host by ip address
        url = socket.gethostbyaddr(ip_address)[0]
        return url
    except (socket.herror, socket.gaierror):
        return ip_address

def count_lines(file):
    with open(file, 'r', encoding=SystemConstants.encode) as ip_file:
        total_lines = sum([1 for _ in ip_file])
    return total_lines

if __name__ == "__main__":
    convert_ip_to_url()