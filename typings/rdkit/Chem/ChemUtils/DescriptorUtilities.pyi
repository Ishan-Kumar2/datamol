from typing import Any

def setDescriptorVersion(version: str = ...): ...

class VectorDescriptorNamespace:
    def __init__(self, **kwargs: Any) -> None: ...

class VectorDescriptorWrapper:
    func: Any = ...
    names: Any = ...
    func_key: Any = ...
    namespace: Any = ...
    def __init__(self, func: Any, names: Any, version: Any, namespace: Any): ...
    def call_desc(self, mol: Any, index: Any): ...
