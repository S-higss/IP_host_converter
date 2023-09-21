from src.converter import resolve_ip_to_url

if __name__ == "__main__":
    input = input(
        "imput number which you want to do\n"
        + "1: ip-hostname converter\n"
        # + "2: \n"
        # + "3: \n"
        # + "4: "
        + "number: "
    )
    num = int(input)
    if num == 1:
        resolve_ip_to_url()
    # elif num == 2:
    #     a.main()
    # elif num == 3:
    #     b.main()
    else: None