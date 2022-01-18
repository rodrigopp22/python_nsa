import math


class Geometry:

    def __init__(self, problemSize: int) -> None:
        self._problemSize = problemSize

    @property
    def problemSize(self):
        return self._problemSize

    @problemSize.setter
    def problemSize(self, problemSize):
        self._problemSize = problemSize

    def euclideanDistance(self, vector: list, points: list) -> float:
        distance: float = 0
        for i in range(self.problemSize):
            tmp = vector[i] - points[i]
            distance += tmp * tmp
        return math.sqrt(distance)

    def matches(self, vector: list, dataset: list, minDist: int) -> bool:
        for it in dataset:
            dist: float = self.euclideanDistance(vector, it)
            if dist <= minDist:
                return True
        return False
