from enum import Enum

class ConfigEnum(str, Enum):
    ZIP_DIR = 'zip_dir'
    ZIP_NAME = 'zip_name'
    UNZIP_DIR = 'unzip_dir'
    UNZIP_NAME = 'unzip_name'
    UNZIP_SCHEMA = 'unzip_schema'


class SchemaEnum(str, Enum):
    FIELD_NAME = 'field_name'
    FIELD_TYPE = 'field_type'