import csv


class Dataset:

    def __init__(self, file_name) -> None:
        self.__file_name = '../../data/' + file_name

    def read(self):
        data: list = []
        with open(self.__file_name, newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=' ')
            for row in csv_reader:
                for field in row:
                    data.append([float(x) for x in field.split(',')])
        return data
