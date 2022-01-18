import numpy as np

datatype = float


class SearchSpace:
    def __init__(self, shape: int) -> None:
        self.__array: np.array[datatype] = np.zeros(shape)

    def get_value(self, index):
        return self.__array[index]

    def set_value(self, index, value):
        self.__array[index] = value


class SearchSpaceController:
    def __init__(self, problem_dimension: int) -> None:
        self.__problem_dimension: int = problem_dimension
        self.__search_space: SearchSpace = SearchSpace(problem_dimension)

    def initialize(self) -> None:
        for i in range(self.__problem_dimension):
            self.__search_space.set_value(0.0, (2 * i))
            self.__search_space.set_value(1.0, (2 * i + 1))

    def get_search_space(self, index) -> int:
        return self.__search_space.get_value(index)
