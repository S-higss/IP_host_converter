from src.ip_to_host_and_url_converter import convert_ip_to_url
from src.host_to_url_converter import convert_host_to_url
from src.host_to_ip_converter import convert_host_to_ip

if __name__ == "__main__":
    n = input(
        "imput number which you want to do\n"
        + "1: ip-url convert\n"
        + "2: host-url convert\n"
        + "3: host-ip convert\n"
        # + "4: "
        + "number: "
    )
    num = int(n)
    if num == 1:
        convert_ip_to_url()
    elif num == 2:
        convert_host_to_url()
    elif num == 3:
        convert_host_to_ip()
    else: None