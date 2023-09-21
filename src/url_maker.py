import re

def url_maker(hostname):
    norm_hostname = hostname
    
    parts = hostname.split('.')
    if parts[0] == "www" or re.match(r"www\w+", parts[0]):
        for i, part in enumerate(parts):
            if i == 0:
                continue
            else:
                parts[i-1] = part
        parts.pop()
        norm_hostname = '.'.join(parts)
    
    # make 2 patterns of url
    urls = [f"https://www.{norm_hostname}", f"http://www.{norm_hostname}"]
    return urls