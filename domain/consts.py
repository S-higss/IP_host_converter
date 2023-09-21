class ConstantMeta(type):
    """定数を管理するクラスのためのメタクラス。
    クラス変数の上書きや新たなクラス変数の追加をできないようにする。
    """

    # クラスが初期化されたどうかを表す変数
    _initialized = False

    def __setattr__(cls, name, value):
        if cls._initialized:
            if name in cls.__dict__:
                raise ValueError(f"{name} is a read-only property")
            else:
                raise AttributeError("Cannot add new attribute to Constants class")
        super().__setattr__(name, value)

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls._initialized = True


# 定数を管理するためのクラス
class SystemConstants(metaclass=ConstantMeta):
    config = "./lib/config/config.toml"
    encode = "utf-8"
    windowsize = "1200x800"
    db_path = "./db"
    data_path = "./data"
    link_path = data_path + "/links"
    hash_path = data_path + "/hash"
    malware_log_path = data_path + "/malware"
    zip_path = data_path + "/logs/zip/"