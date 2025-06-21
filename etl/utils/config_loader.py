import os
import json

from typing import Dict
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

from etl.utils.config_enums import ConfigEnum, SchemaEnum


type_map = {
    "string": StringType(),
    "integer": IntegerType(),
    "float": FloatType()
}

class ConfigLoader:
    def __init__(self, config_path: str):
        self.config_path = config_path
        if config_path.endswith(".json"):
            with open(config_path, "r") as f:
                self.config = json.load(f)
        else:
            raise ValueError("Unsupported config format: must be .json")

    def load_config(self) -> dict:
        return self.config

    def load_archive_dir(self) -> str:
        return self.config[ConfigEnum.ZIP_DIR]

    def load_archive_name(self) -> str:
        return self.config[ConfigEnum.ZIP_NAME]

    def load_archive_full_dir(self) -> str:
        return os.path.join(self.load_archive_dir(), self.load_archive_name())

    def load_raw_dir(self) -> str:
        return self.config[ConfigEnum.UNZIP_DIR]

    def load_raw_name(self) -> str:
        return self.config[ConfigEnum.UNZIP_NAME]

    def load_raw_full_dir(self) -> str:
        return os.path.join(self.load_raw_dir(), self.load_raw_name())

    def load_schema(self) -> StructType:
        def build_schema(schema: Dict) -> StructType:
            return StructType([
                StructField(field[SchemaEnum.FIELD_NAME], type_map[field[SchemaEnum.FIELD_TYPE].lower()], True) for field in schema
            ])

        source_schema = self.config[ConfigEnum.UNZIP_SCHEMA]
        return build_schema(source_schema)