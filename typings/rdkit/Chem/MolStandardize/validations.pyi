from .errors import StopValidateError as StopValidateError
from .fragment import REMOVE_FRAGMENTS as REMOVE_FRAGMENTS
from rdkit import Chem as Chem
from typing import Any

class Validation:
    log: Any = ...
    def __init__(self, log: Any) -> None: ...
    def __call__(self, mol: Any) -> None: ...
    def run(self, mol: Any) -> None: ...

class SmartsValidation(Validation):
    level: Any = ...
    message: str = ...
    entire_fragment: bool = ...
    def __init__(self, log: Any) -> None: ...
    @property
    def smarts(self) -> None: ...
    def run(self, mol: Any) -> None: ...

class IsNoneValidation(Validation):
    def run(self, mol: Any) -> None: ...

class NoAtomValidation(Validation):
    def run(self, mol: Any) -> None: ...

class DichloroethaneValidation(SmartsValidation):
    level: Any = ...
    smarts: str = ...
    entire_fragment: bool = ...
    message: str = ...

class FragmentValidation(Validation):
    fragments: Any = ...
    def run(self, mol: Any) -> None: ...

class NeutralValidation(Validation):
    def run(self, mol: Any) -> None: ...

class IsotopeValidation(Validation):
    def run(self, mol: Any) -> None: ...

VALIDATIONS: Any