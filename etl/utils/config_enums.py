from enum import Enum

class ConfigEnum(str, Enum):
    ZIP_DIR = 'zip_dir'
    ZIP_NAME = 'zip_name'
    UNZIP_DIR = 'unzip_dir'
    UNZIP_NAME = 'unzip_name'
    UNZIP_SCHEMA = 'unzip_schema'
    OUTPUT_DIR = 'output_dir'
    OUTPUT_NUM_PARTITION = 'output_num_partition'
    DB_FILE = 'db_file'


class SchemaEnum(str, Enum):
    FIELD_NAME = 'field_name'
    FIELD_TYPE = 'field_type'