from domain.consts import SystemConstants
# import libs
from lib.config.config import load_config
# import modules
import sys, time, socket

config = load_config(SystemConstants.config)

def test():
    # A text file containing IP addresses one line at a time
    ip_filename = config["data"]["ip_list"]

    count = 0

    # with open(ip_filename, 'r', encoding=SystemConstants.encode) as ip_file:
    #     for line in ip_file:
    #         count += 1
    # print(count)

    with open(ip_filename, 'r', encoding=SystemConstants.encode) as ip_file:
        total_lines = sum([1 for _ in ip_file])
    print(total_lines)

if __name__ == "__main__":
    test()