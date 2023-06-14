from abc import ABC, abstractmethod


class ModelAdaptee(ABC):
    @abstractmethod
    def load_headers(self):
        pass

    @abstractmethod
    def yield_row(self):
        pass


class UserModel(ModelAdaptee):
    def __init__(self) -> None:
        self.__users = []
        self.__headers = ["Name", "Age"]

    def load_headers(self):
        return self.__headers

    def yield_row(self):
        for user in self.__users:
            yield user

    @property
    def users(self):
        return self.__users

    def add_user(self, user):
        self.users.append(user)


class ModelAdapter(ABC):
    @abstractmethod
    def write_to_csv(self):
        pass


class UserModelAdapter(ModelAdapter):
    def __init__(self, user_model: UserModel) -> None:
        self.__user_model = user_model

    def write_to_csv(self, file_name):
        with open(file_name, "w", encoding="utf-8", newline="\n") as f:
            f.write(",".join(self.__user_model.load_headers()) + "\n")
            for user in self.__user_model.yield_row():
                f.write(",".join(map(str, user)) + "\n")


users = UserModel()
users.add_user(["Taro", 19])
users.add_user(["Hanako", 29])
# print(users.load_headers())

adapter = UserModelAdapter(users)

adapter.write_to_csv("users.csv")

# for user in users.yield_row():
#     print(user)
