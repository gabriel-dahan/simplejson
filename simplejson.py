import json
from types import SimpleNamespace
from typing import Union

class Json(object):

    @classmethod
    def read(self, path: str) -> dict:
        with open(path, 'r') as f:
            f = json.load(f)
        return f

    @classmethod
    def write(self, data, path: str, indent: int = None):
        with open(path, 'w') as f:
            json.dump(data, f, indent = indent)

    @classmethod
    def convert_to_obj(self, data: Union[dict, str]):
        if isinstance(data, dict):
            data = str(data).replace('\'', '"')
        return json.loads(data, object_hook = lambda d: SimpleNamespace(**d))