from domain.consts import SystemConstants
# import libs
from lib.config.config import load_config
# import modules
import time, socket, json
from src.progress_bar import Progbar

config = load_config(SystemConstants.config)

def convert_host_to_ip():
    # A text file containing hostname one line at a time
    hostname_filename = config["data"]["host_list"]
    # A text file containing valid url one line at a time
    output_host_ip_filename = config["data"]["host_ip_list"]
    output_host_ip_dic = config["data"]["host_ip_dic"]

    total_lines = count_lines(hostname_filename)
    host_ip_dic = {}
    with Progbar(total_lines) as pb:
        try:
            with open(hostname_filename, 'r', encoding=SystemConstants.encode) as hostname_file, open(output_host_ip_filename, 'w', encoding=SystemConstants.encode) as host_ip_file, open(output_host_ip_dic, 'w', encoding=SystemConstants.encode) as host_ip_dic_file:
                i = 0
                for line in hostname_file:
                    # ---convert ip to hostname---
                    pb.update(i, f"{i}/{total_lines} convert hostname to ip...")
                    hostname = line.strip()
                    if hostname:
                        # ---make valid url from hostname---
                        ip = get_ip_address(hostname)
                        if not ip:
                            ip = "Error"
                        host_ip_dic[hostname] = ip
                    host_ip_file.write(f"{hostname}: {ip}\n")
                    i += 1
                    pb.update(i, f"{i}/{total_lines}")
                    time.sleep(0.1)
                json.dump(host_ip_dic, host_ip_dic_file)
                # → reuse: loaded_data = json.load(file)
                # host_ip_dic_file.write(host_ip_dic)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

def count_lines(file):
    with open(file, 'r', encoding=SystemConstants.encode) as ip_file:
        total_lines = sum([1 for _ in ip_file])
    return total_lines

def get_ip_address(host):
    try:
        ip_address = socket.gethostbyname(host)
        return ip_address
    except socket.gaierror:
        return None

if __name__ == "__main__":
    convert_host_to_ip()