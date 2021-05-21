from configparser import ConfigParser, BasicInterpolation


class Config:
    configParser = ConfigParser(interpolation=BasicInterpolation())
    config_file = 'config.ini'

    @classmethod
    def get_value(cls, section, key):
        cls.configParser.read(cls.config_file)
        """Get value from config.ini."""
        return cls.configParser.get(section, key)
