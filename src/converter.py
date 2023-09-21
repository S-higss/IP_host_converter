from domain.consts import SystemConstants
# import libs
from lib.config.config import load_config
# import modules
import sys, time, socket

config = load_config(SystemConstants.config)

class Progbar:
    def __init__(self, period=100, bars=32):
        self._period  = period
        self.bars     = bars
        self.active   = True
    def __del__(self):
        self.dispose()
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        self.dispose()

    def dispose(self):
        if self.active:
            self.active = False
            self.update(self._period, "")
            sys.stdout.write("\n")
    def update(self, tick, status: str):
        rate = tick / self._period
        # progress rate
        str = "{0:7d}% ".format(int(rate*100))
        # progress bar
        bar_prog = int(rate * self.bars)
        str += "|"
        str += "#" * (            bar_prog)
        str += "-" * (self.bars - bar_prog)
        str += "|"
        str += status
        str += "\r"
        sys.stdout.write(str)

def resolve_ip_to_url():
    # A text file containing IP addresses one line at a time
    ip_filename = config["data"]["ip_list"]
    # A text file containing hostname one line at a time
    output_filename = config["data"]["host_list"]

    total_lines = count_lines(ip_filename)
    with Progbar(total_lines) as pb:
        try:
            with open(ip_filename, 'r', encoding=SystemConstants.encode) as ip_file, open(output_filename, 'w', encoding=SystemConstants.encode) as output_file:
                i = 0
                for line in ip_file:
                    ip_address = line.strip()
                    url = resolve_ip(ip_address)
                    if url:
                        output_file.write(url + '\n')
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
    resolve_ip_to_url()