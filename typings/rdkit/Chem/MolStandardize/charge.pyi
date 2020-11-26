from .utils import memoized_property as memoized_property
from rdkit import Chem as Chem
from typing import Any

log: Any

class AcidBasePair:
    name: Any = ...
    acid_str: Any = ...
    base_str: Any = ...
    def __init__(self, name: Any, acid: Any, base: Any) -> None: ...
    def acid(self): ...
    def base(self): ...

ACID_BASE_PAIRS: Any

class ChargeCorrection:
    name: Any = ...
    smarts_str: Any = ...
    charge: Any = ...
    def __init__(self, name: Any, smarts: Any, charge: Any) -> None: ...
    def smarts(self): ...

CHARGE_CORRECTIONS: Any

class Reionizer:
    acid_base_pairs: Any = ...
    charge_corrections: Any = ...
    def __init__(self, acid_base_pairs: Any = ..., charge_corrections: Any = ...) -> None: ...
    def __call__(self, mol: Any): ...
    def reionize(self, mol: Any): ...

class Uncharger:
    def __init__(self) -> None: ...
    def __call__(self, mol: Any): ...
    def uncharge(self, mol: Any): ...
