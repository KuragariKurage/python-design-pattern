from abc import ABC, abstractmethod
from copy import deepcopy


class Prototype(ABC):
    @abstractmethod
    def use(self, msg):
        pass

    @abstractmethod
    def _clone(self):
        pass


class MessageBox(Prototype):
    def __init__(self, decochar):
        self.decochar = decochar

    def use(self, msg):
        str_msg = str(msg)
        print(self.decochar * (len(str_msg) + 4))
        print(self.decochar + " " + str_msg + " " + self.decochar)
        print(self.decochar * (len(str_msg) + 4))

    def _clone(self):
        print("cloning message box...")
        return deepcopy(self)

    @property
    def decoration_char(self):
        return self.decochar

    @decoration_char.setter
    def decoration_char(self, decochar):
        self.decochar = decochar


class UnderlinePen(Prototype):
    def __init__(self, underline_char):
        self.__underline_char = underline_char

    def use(self, msg):
        str_msg = str(msg)
        print(str_msg)
        print(self.__underline_char * len(str_msg))

    def _clone(self):
        print("cloning underline pen...")
        return deepcopy(self)

    @property
    def underline_char(self):
        return self.__underline_char

    @underline_char.setter
    def underline_char(self, underline_char):
        self.__underline_char = underline_char


class Manager:
    def __init__(self):
        self.__products = {}

    def register(self, name, proto: Prototype):
        self.__products[name] = proto

    def create_product(self, name):
        product = self.__products.get(name)
        return product._clone()


manager = Manager()

msg_box = MessageBox("*")
msg_box.use("Hello, World!")

ul_pen = UnderlinePen("-")
ul_pen.use("Hello, World!")

manager.register("msg_box", msg_box)
manager.register("ul_pen", ul_pen)

msg_box_2 = manager.create_product("msg_box")
msg_box_2.use("Goodbye, World!")

ul_pen_2 = manager.create_product("ul_pen")
ul_pen_2.use("Goodbye, World!")
