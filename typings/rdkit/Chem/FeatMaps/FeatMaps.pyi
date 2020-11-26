from rdkit.Chem.FeatMaps.FeatMapPoint import FeatMapPoint as FeatMapPoint
from typing import Any, Optional

class FeatMapScoreMode:
    All: int = ...
    Closest: int = ...
    Best: int = ...

class FeatDirScoreMode:
    Ignore: int = ...
    DotFullRange: int = ...
    DotPosRange: int = ...

class FeatMapParams:
    radius: float = ...
    width: float = ...
    class FeatProfile:
        Gaussian: int = ...
        Triangle: int = ...
        Box: int = ...
    featProfile: Any = ...

class FeatMap:
    dirScoreMode: Any = ...
    scoreMode: Any = ...
    params: Any = ...
    def __init__(self, params: Optional[Any] = ..., feats: Optional[Any] = ..., weights: Optional[Any] = ...) -> None: ...
    def AddFeature(self, feat: Any, weight: Optional[Any] = ...) -> None: ...
    def AddFeatPoint(self, featPt: Any) -> None: ...
    def GetFeatures(self): ...
    def GetNumFeatures(self): ...
    def GetFeature(self, i: Any): ...
    def DropFeature(self, i: Any) -> None: ...
    def GetFeatFeatScore(self, feat1: Any, feat2: Any, typeMatch: bool = ...): ...
    def ScoreFeats(self, featsToScore: Any, mapScoreVect: Any = ..., featsScoreVect: Any = ..., featsToFeatMapIdx: Any = ...): ...
