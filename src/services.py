import os

from settings import settings


class ConfigurationService():
    def __init__(self):
        if "environment" in os.environ:
            self.env = os.environ["environment"]
        else:
            self.env = "dev"

    def get_env(self):
        return self.env

    def get(self, key):
        if settings[key][self.env]:
            return settings[key][self.env]

        raise SettingsException('Cannot find config key')


class SettingsException(Exception):
    pass
