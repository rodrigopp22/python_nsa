from dataclasses import dataclass
from random import uniform
import numpy as np 

datatype = float

class Detector:
    def generate(self, search_space, index):
        return search_space.get_search_space(2*index) + (search_space.get_search_space(2*index+1) - search_space.get_search_space(2*index))*uniform(0.0, 1.0)

class DetectorArray:
    def __init__(self, detector) -> None:
        self.detector_array: np.array = 
        self.detector = detector

    def generate_points(self, problem_dimension, search_space):
        for i in range(problem_dimension):
            self.detector_array[i] = self.detector.generate(problem_dimension, search_space)

    @property
    def detector_array(self):
        return self.detector_array