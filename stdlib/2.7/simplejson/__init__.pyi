from typing import Any, IO

def dumps(obj: Any) -> str: ...
def dump(obj: Any, fp: IO[str], *args: Any, **kwds: Any) -> None: ...
def loads(s: str, **kwds: Any) -> Any: ...
def load(fp: IO[str]) -> Any: ...

from .scanner import JSONDecodeError
from .decoder import JSONDecoder
from .encoder import JSONEncoder, JSONEncoderForHTML
