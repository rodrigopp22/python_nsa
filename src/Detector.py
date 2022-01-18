from Geometry import Geometry
from Result import Result
from random import uniform

class Detector:
    def __init__(self, configFile, selfDataset) -> None:
        self._configFile = configFile
        self._geometry = Geometry(self._configFile.problemSize)
        self._selfDataset = selfDataset

    def randomVector(self, vector: list) -> list:
        for i in range(self._configFile.problemSize):
            vector[i] = self._configFile.getSearchSpaceIndex(2*i) + (self._configFile.getSearchSpaceIndex(
                2*i+1) - self._configFile.getSearchSpaceIndex(2*i))*uniform(0.0, 1.0)
        return vector

    def generateDetectors(self) -> list:
        detectors = list()
        print("Generating detectors...")
        detector: list = [None]*self._configFile.problemSize
        while len(detectors) < self._configFile.maxDetectors:
            self.randomVector(detector)
            if not self._geometry.matches(detector, self._selfDataset, self._configFile.minDist):
                if not self._geometry.matches(detector, detectors, 0.0):
                    detectors.append(detector)
                    detector = [None]*self._configFile.problemSize
                    print(f"{len(detectors)}/{self._configFile.maxDetectors}")
        if detector != None:
            del detector
        return detectors

    def applyDetectors(self, detectors: list) -> Result:
        detected = set()
        trial = 1
        for it in self._selfDataset:
            actual: bool = self._geometry.matches(
                it, detectors, self._configFile.minDist)
            expected: bool = self._geometry.matches(
                it, self._selfDataset, self._configFile.minDist)
            if actual == expected:
                detected.add(trial)
            trial += 1

        print("Expected to be detected: ", end='')
        configExpectedDetected = self._configFile.expectedDetected
        for it in configExpectedDetected:
            print(it, end='')
            it += 1
            if it != configExpectedDetected[-1]:
                print(",", end=' ')

        print("\nFound: ", end = '')
        for it in detected:
            print(it, end='')
            it += 1
            if it != configExpectedDetected[-1]:
                print(",", end=' ')

        expectedDetected = set(configExpectedDetected)
        expectedDetectedSize = len(expectedDetected)
        for it in detected:
            for found in expectedDetected:
                if it == found:
                    expectedDetected.remove(found)
                    break
        newExpectedDetectedSize = len(expectedDetected)

        result = Result()
        result.DR = (-(newExpectedDetectedSize -
                       expectedDetectedSize) / expectedDetectedSize)

        expectedDetected.clear()
        expectedDetected = [value for value in configExpectedDetected]
        for it in expectedDetected:
            for found in detected:
                if it == found:
                    detected.remove(found)
                    break
        newDetectedSize = len(detected)
        result.FAR = newDetectedSize / expectedDetectedSize
        return result
