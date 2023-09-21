from src.converter import resolve_ip_to_url

if __name__ == "__main__":
    n = input(
        "imput number which you want to do\n"
        + "1: ip-url converter\n"
        # + "2: \n"
        # + "3: \n"
        # + "4: "
        + "number: "
    )
    num = int(n)
    if num == 1:
        resolve_ip_to_url()
    # elif num == 2:
    #     a.main()
    # elif num == 3:
    #     b.main()
    else: None