class Database:
    _instance = None

    def __init__(self):
        self.__database_url = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def database_url(self):
        return self.__database_url

    @database_url.setter
    def database_url(self, database_url):
        self.__database_url = database_url

    def connect(self):
        pass


a = Database()
# a.database_url = "http://localhost:8080" # ここでsetすると None になる、なんぜ？
b = Database()
a.database_url = "http://localhost:8080"

print(a == b)  # true
print(id(a), id(b))
print(a.database_url, b.database_url)
