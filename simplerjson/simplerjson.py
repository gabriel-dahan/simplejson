import json
from types import SimpleNamespace
from typing import (
    Union, Optional, Type, Tuple, Any, Callable, Dict, List
)

def read(path: str, 
            cls: Optional[Type[json.JSONDecoder]] = None, 
            object_hook: Optional[Callable[[Dict[Any, Any]], Any]] = None, 
            parse_float: Optional[Callable[[str], Any]] = None, 
            parse_int: Optional[Callable[[str], Any]] = None, 
            parse_constant: Optional[Callable[[str], Any]] = None, 
            object_pairs_hook: Optional[Callable[[List[Tuple[Any, Any]]], Any]] = None, 
            **kwds: Any) -> dict:
    with open(path, 'r') as f:
        f = json.load(
            f, 
            cls = cls, 
            object_hook = object_hook, 
            parse_float = parse_float, 
            parse_int = parse_int, 
            parse_constant = parse_constant, 
            object_pairs_hook = object_pairs_hook, 
            **kwds
        )
    return f

def write(data: dict, path: str, 
            skipkeys: bool = False, 
            ensure_ascii: bool = True, 
            check_circular: bool = True, 
            allow_nan: bool = True, 
            cls: Optional[Type[json.JSONEncoder]] = None, 
            indent: Union[None, int, str] = None, 
            separators: Optional[Tuple[str, str]] = None, 
            default: Optional[Callable[[Any], Any]] = None, 
            sort_keys: bool = False, 
            **kwds: Any):
    with open(path, 'w') as f:
        json.dump(
            data, f, 
            shipkeys = skipkeys, 
            ensure_ascii = ensure_ascii, 
            check_circular = check_circular, 
            allow_nan = allow_nan, 
            cls = cls, 
            indent = indent, 
            separators = separators, 
            default = default, 
            sort_keys = sort_keys, 
            **kwds
        )

def to_obj(data: Union[dict, str]):
    if isinstance(data, dict):
        data = str(data).replace('\'', '"')
    return json.loads(data, object_hook = lambda d: SimpleNamespace(**d))