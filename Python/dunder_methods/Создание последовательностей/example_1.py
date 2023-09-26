from collections import UserDict
from typing import Any


class CaseInsensitiveDict(UserDict):
    def __getitem__(self, key: str) -> Any:
        return super().__getitem__(key.lower())

    def __setitem__(self, key: str, value: Any):
        return super().__setitem__(key.lower(), value)

    def __delitem__(self, key: str) -> None:
        return super().__delitem__(key.lower())


headers = CaseInsensitiveDict({
    "Content-Length": 30,
    "Content-Type": "application/json",
})

print(f"{ headers['CONTENT-LENGTH'] = }")
print(f"{ headers['content-type']  = }")
