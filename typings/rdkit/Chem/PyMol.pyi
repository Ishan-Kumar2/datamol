from rdkit import Chem as Chem
from typing import Any, Optional

class MolViewer:
    server: Any = ...
    def __init__(self, host: Optional[Any] = ..., port: int = ..., force: int = ..., **kwargs: Any) -> None: ...
    def InitializePyMol(self) -> None: ...
    def DeleteAll(self) -> None: ...
    def DeleteAllExcept(self, excludes: Any) -> None: ...
    def LoadFile(self, filename: Any, name: Any, showOnly: bool = ...): ...
    def ShowMol(self, mol: Any, name: str = ..., showOnly: bool = ..., highlightFeatures: Any = ..., molB: str = ..., confId: int = ..., zoom: bool = ..., forcePDB: bool = ..., showSticks: bool = ...): ...
    def GetSelectedAtoms(self, whichSelection: Optional[Any] = ...): ...
    def SelectAtoms(self, itemId: Any, atomIndices: Any, selName: str = ...) -> None: ...
    def HighlightAtoms(self, indices: Any, where: Any, extraHighlight: bool = ...) -> None: ...
    def SetDisplayStyle(self, obj: Any, style: str = ...) -> None: ...
    def SelectProteinNeighborhood(self, aroundObj: Any, inObj: Any, distance: float = ..., name: str = ..., showSurface: bool = ...) -> None: ...
    def AddPharmacophore(self, locs: Any, colors: Any, label: Any, sphereRad: float = ...) -> None: ...
    def SetDisplayUpdate(self, val: Any) -> None: ...
    def GetAtomCoords(self, sels: Any): ...
    def HideAll(self) -> None: ...
    def HideObject(self, objName: Any) -> None: ...
    def DisplayObject(self, objName: Any) -> None: ...
    def Redraw(self) -> None: ...
    def Zoom(self, objName: Any) -> None: ...
    def DisplayHBonds(self, objName: Any, molName: Any, proteinName: Any, molSelText: str = ..., proteinSelText: str = ...) -> None: ...
    def DisplayCollisions(self, objName: Any, molName: Any, proteinName: Any, distCutoff: float = ..., color: str = ..., molSelText: str = ..., proteinSelText: str = ...) -> None: ...
    def SaveFile(self, filename: Any) -> None: ...
    def GetPNG(self, h: Optional[Any] = ..., w: Optional[Any] = ..., preDelay: int = ...): ...
