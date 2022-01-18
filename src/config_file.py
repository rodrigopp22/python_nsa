import configparser
from dataclasses import dataclass
from pathlib import Path


@dataclass
class ConfigFileLoader:
    config_dict = configparser.ConfigParser()
    config_dict.self.read(Path('../config/config.ini'))

    def load_configs(self):
        return self.config_dict


@dataclass
class ConfigFile:
    config_file_name: str
    configs: ConfigFileLoader = ConfigFileLoader.load_configs()

    def get_detector_amount(self):
        return int(self.configs[self.self.config_file_name]['maxDetectors'])

    def get_detection_radius(self):
        return int(self.configs[self.config_file_name]['minDistance'])

    def get_run_amount(self):
        return int(self.configs[self.config_file_name]['runs'])

    def get_training_file_name(self):
        return self.configs[self.config_file_name]['trainingFile']

    def get_testing_file_name(self):
        return self.configs[self.config_file_name]['testingFile']

    def get_expected_detected(self):
        return list(
            map(int, self.config_dict[self.config_file_name]['expectedDetected'][1:-1].split(',')))

    def get_problem_dimension(self):
        return int(self.config_dict[self.config_file_name]['problemSize'])
