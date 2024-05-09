# IP_host_converter

## About
Converter of IP to Hostname

## How to use

### setup
```bash
git clone https://github.com/S-higss/IP_host_converter.git
make
```

### Edit File
- If you want to convert ip-address into URL  
    Edit ./data/ip_list.txt  
    Ex.
    ```bash
    192.168.aaa.bbb
    10.230.0.ccc
    172.16.ddd.eee
    ```

- If you want to convert host into URL or ip  
    Edit ./data/host_list.txt  
    Ex.
    ```bash
    github.com
    www.kobe-u.ac.jp
    ...
    ```

### Run app
```bash
make run
```
And then console display
```bash
imput number which you want to do
1: ip-url convert
2: host-url convert
3: host-ip convert
number:
```

And input the number you want to do.

## License
**IP_host_converter** licensed under [MIT license](https://github.com/S-higss/IP_host_converter/blob/main/LICENSE). Basically you can do whatever you want to with it.
