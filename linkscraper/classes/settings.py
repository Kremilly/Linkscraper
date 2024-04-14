#!/usr/bin/python3

import yaml

from helper.configs import Configs

from exceptions.settings_exception import SettingsException

class Settings:

    @classmethod
    def search_property_in_file(cls, prop):
        with open(Configs.CONFIGS_FILE, 'r') as file:
            lines = file.readlines()

            for line_number, line in enumerate(lines, start=1):
                if prop.split('.')[-1] in line:
                    return f"{line_number} -> '{line.strip()}'"

    @classmethod
    def get_wrong_property_position(cls, prop, open_file=False):
        configs_file = Configs.CONFIGS_FILE
        line_position = cls.search_property_in_file(prop)

        if open_file:
            line_position = line_position.split(' -> ')[0]
            return f'{configs_file}:{line_position}'

        return f"Please fix it in: {configs_file.replace('./', '')}:{line_position}"

    @classmethod
    def is_valid(cls, prop, value, data_type):
        if type(value) == str:
            value_type = 'STRING'
        elif type(value) == int:
            value_type = 'INT'
        elif type(value) == float:
            value_type = 'FLOAT'
        elif type(value) == bool:
            value_type = 'BOOLEAN'
        elif type(value) == list:
            value_type = 'LIST'

        data_type = data_type.upper()
        property_position = cls.get_wrong_property_position(prop)

        if data_type != value_type:
            raise SettingsException(f"The '{prop}' configuration is invalid. Expected type {data_type}, but "
                                    f"instead a {value_type} was passed. {property_position}.")

        return value

    @classmethod
    def get(cls, prop, data_type):
        try:
            with open(Configs.CONFIGS_FILE, 'r') as content:
                data = yaml.safe_load(content)

            value = data
            property_parts = prop.split('.')

            for part in property_parts:
                value = value[part]

            return cls.is_valid(prop, value, data_type)

        except FileNotFoundError:
            raise SettingsException(f"File '{Configs.CONFIGS_FILE.replace('./', '')}' not found.")

        except yaml.YAMLError as e:
            raise SettingsException(f'Error while parsing the YAML file.: {e}')
