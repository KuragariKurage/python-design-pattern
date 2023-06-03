# コンストラクタを private にすることで、インスタンスの生成を制限する
# python は __init__ を private にできないので、__new__ とクラスメソッドを使った方針で実装


class Database:

    __instance = None

    def __init__(self) -> None:
        raise RuntimeError("このクラスのコンストラクタは呼び出せません")

    @classmethod
    def get_instance(cls, database_url=None):
        if cls.__instance is None:
            cls.__instance = cls.__new__(cls)

        if database_url is not None:
            cls.__instance.__database_url = database_url

        return cls.__instance

    @property
    def database_url(self):
        return self.__database_url

    @database_url.setter
    def database_url(self, database_url):
        self.__database_url = database_url

    def connect(self):
        pass


a = Database.get_instance("http://localhost:8080")
b = Database.get_instance()

print(a is b)
print(id(a), id(b))
print(a.database_url, b.database_url)
a.database_url = "http://localhost:8081"
print(a.database_url, b.database_url)
