from abc import ABC, abstractmethod, abstractproperty


# product
class SetMeal:
    @property
    def main_dish(self):
        return self.__main_dish

    @main_dish.setter
    def main_dish(self, main_dish):
        self.__main_dish = main_dish

    @property
    def side_dish(self):
        return self.__side_dish

    @side_dish.setter
    def side_dish(self, side_dish):
        self.__side_dish = side_dish

    def __str__(self) -> str:
        return f"maindish: {self.main_dish}, sidedish: {self.side_dish}"


# builder interface
class SetMealBuilder(ABC):
    def __init__(self):
        self._set_meal = SetMeal()

    @abstractproperty
    def product(self):
        pass

    @abstractmethod
    def build_main_dish(self):
        pass

    @abstractmethod
    def build_side_dish(self):
        pass


class SanmaSetBuilder(SetMealBuilder):
    def __init__(self):
        super().__init__()

    @property
    def product(self):
        return self._set_meal

    def build_main_dish(self):
        self._set_meal.main_dish = "さんま"
        return self

    def build_side_dish(self):
        self._set_meal.side_dish = "お味噌汁"
        return self


class PastaSetBuilder(SetMealBuilder):
    def __init__(self):
        super().__init__()

    @property
    def product(self):
        return self._set_meal

    def build_main_dish(self):
        self._set_meal.main_dish = "パスタ"
        return self

    def build_side_dish(self):
        self._set_meal.side_dish = "スープ"
        return self


# director
class Director:
    def __init__(self, builder: SetMealBuilder) -> None:
        self.__builder = builder

    @property
    def builder(self):
        return self.__builder

    @builder.setter
    def builder(self, builder):
        self.__builder = builder

    def build(self):
        # self.builder.build_main_dish()
        # self.builder.build_side_dish()
        self.builder.build_main_dish().build_side_dish()
        return self.__builder


sanma_builder = SanmaSetBuilder()
pasta_builder = PastaSetBuilder()

director = Director(sanma_builder)
# director.build()
# print(director.builder.product)
print(director.build().product)

director.builder = pasta_builder
# director.build()
# print(director.builder.product)
print(director.build().product)
