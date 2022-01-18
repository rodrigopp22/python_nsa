import sys
from src.config_file import ConfigFile
from Dataset import Dataset
from Detector import Detector


def initSearchSpace(configFile: ConfigFile):
    configFile.setSearchSpace()
    for i in range(configFile.problemSize):
        configFile.setSearchSpaceIndex(0.0, (2 * i))
        configFile.setSearchSpaceIndex(1.0, (2 * i + 1))


def run(configFile: ConfigFile):
    generalResults: list = list()
    initSearchSpace(configFile)
    trainingDataset = Dataset(
        configFile.trainingDatasetCsvFile
    )
    testingDataset = Dataset(
        configFile.testingDatasetCsvFile
    )
    selfDatasetForTraining = trainingDataset.readDataset()
    generateSelfDatasetForTesting = testingDataset.readDataset()
    trainingDetectors = Detector(configFile, selfDatasetForTraining)
    testingDetectors = Detector(configFile, generateSelfDatasetForTesting)
    detectors: list = list()
    for _ in range(configFile.amountOfProofs):
        detectors = trainingDetectors.generateDetectors()
        generalResults.append(
            testingDetectors.applyDetectors(detectors))
    print(f'Detectors: {configFile.maxDetectors}/{len(detectors)}')
    print(f'Min. distance: {configFile.minDist}')
    print(f'Runs: {configFile.amountOfProofs}')
    sumDR: float = 0
    sumFAR: float = 0
    for r in generalResults:
        print(f'{r.DR}, {r.FAR}')
        sumDR += 1
        sumFAR += 1
    print(f'Average: {sumDR/configFile.amountOfProofs}')


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        configFile = ConfigFile(filename)
        run(configFile)
    else:
        print(f'Usage {sys.argv[0]} <CONFIG-FILE>')
        return -1

    return 0


if __name__ == '__main__':
    main()
