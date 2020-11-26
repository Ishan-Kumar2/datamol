from typing import overload
import Boost.Python

@overload
def FindMCS(boost) -> Any: ...
@overload
def FindMCS(boost, RDKit) -> Any: ...

class AtomCompare(Boost.Python.enum):
    CompareAny: Any = ...
    CompareAnyHeavyAtom: Any = ...
    CompareElements: Any = ...
    CompareIsotopes: Any = ...
    names: Any = ...
    values: Any = ...
    __slots__: Any = ...

class BondCompare(Boost.Python.enum):
    CompareAny: Any = ...
    CompareOrder: Any = ...
    CompareOrderExact: Any = ...
    names: Any = ...
    values: Any = ...
    __slots__: Any = ...

class MCSAtomCompare(Boost.Python.instance):
    __instance_size__: Any = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def CheckAtomCharge(self, *args, **kwargs) -> Any: ...
    @classmethod
    def CheckAtomChirality(self, *args, **kwargs) -> Any: ...
    @classmethod
    def CheckAtomRingMatch(self, *args, **kwargs) -> Any: ...
    @classmethod
    def compare(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __call__(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __reduce__(self) -> Any: ...

class MCSAtomCompareParameters(Boost.Python.instance):
    __instance_size__: Any = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def __reduce__(self) -> Any: ...
    @property
    def MatchChiralTag(self) -> Any: ...
    @MatchChiralTag.setter
    def MatchChiralTag(self, val: Any) -> None: ...
    @property
    def MatchFormalCharge(self) -> Any: ...
    @MatchFormalCharge.setter
    def MatchFormalCharge(self, val: Any) -> None: ...
    @property
    def MatchIsotope(self) -> Any: ...
    @MatchIsotope.setter
    def MatchIsotope(self, val: Any) -> None: ...
    @property
    def MatchValences(self) -> Any: ...
    @MatchValences.setter
    def MatchValences(self, val: Any) -> None: ...
    @property
    def RingMatchesRingOnly(self) -> Any: ...
    @RingMatchesRingOnly.setter
    def RingMatchesRingOnly(self, val: Any) -> None: ...

class MCSBondCompare(Boost.Python.instance):
    __instance_size__: Any = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def CheckBondRingMatch(self, *args, **kwargs) -> Any: ...
    @classmethod
    def CheckBondStereo(self, *args, **kwargs) -> Any: ...
    @classmethod
    def compare(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __call__(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __reduce__(self) -> Any: ...

class MCSBondCompareParameters(Boost.Python.instance):
    __instance_size__: Any = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def __reduce__(self) -> Any: ...
    @property
    def CompleteRingsOnly(self) -> Any: ...
    @CompleteRingsOnly.setter
    def CompleteRingsOnly(self, val: Any) -> None: ...
    @property
    def MatchFusedRings(self) -> Any: ...
    @MatchFusedRings.setter
    def MatchFusedRings(self, val: Any) -> None: ...
    @property
    def MatchFusedRingsStrict(self) -> Any: ...
    @MatchFusedRingsStrict.setter
    def MatchFusedRingsStrict(self, val: Any) -> None: ...
    @property
    def MatchStereo(self) -> Any: ...
    @MatchStereo.setter
    def MatchStereo(self, val: Any) -> None: ...
    @property
    def RingMatchesRingOnly(self) -> Any: ...
    @RingMatchesRingOnly.setter
    def RingMatchesRingOnly(self, val: Any) -> None: ...

class MCSParameters(Boost.Python.instance):
    __instance_size__: Any = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def SetAtomTyper(self, *args, **kwargs) -> Any: ...
    @classmethod
    def SetBondTyper(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __reduce__(self) -> Any: ...
    @property
    def AtomCompareParameters(self) -> Any: ...
    @AtomCompareParameters.setter
    def AtomCompareParameters(self, val: Any) -> None: ...
    @property
    def AtomTyper(self) -> Any: ...
    @AtomTyper.setter
    def AtomTyper(self, val: Any) -> None: ...
    @property
    def BondCompareParameters(self) -> Any: ...
    @BondCompareParameters.setter
    def BondCompareParameters(self, val: Any) -> None: ...
    @property
    def BondTyper(self) -> Any: ...
    @BondTyper.setter
    def BondTyper(self, val: Any) -> None: ...
    @property
    def InitialSeed(self) -> Any: ...
    @InitialSeed.setter
    def InitialSeed(self, val: Any) -> None: ...
    @property
    def MaximizeBonds(self) -> Any: ...
    @MaximizeBonds.setter
    def MaximizeBonds(self, val: Any) -> None: ...
    @property
    def ProgressCallback(self) -> Any: ...
    @ProgressCallback.setter
    def ProgressCallback(self, val: Any) -> None: ...
    @property
    def Threshold(self) -> Any: ...
    @Threshold.setter
    def Threshold(self, val: Any) -> None: ...
    @property
    def Timeout(self) -> Any: ...
    @Timeout.setter
    def Timeout(self, val: Any) -> None: ...
    @property
    def Verbose(self) -> Any: ...
    @Verbose.setter
    def Verbose(self, val: Any) -> None: ...

class MCSProgress(Boost.Python.instance):
    __instance_size__: Any = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def callback(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __call__(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __reduce__(self) -> Any: ...

class MCSProgressData(Boost.Python.instance):
    __instance_size__: Any = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def __reduce__(self) -> Any: ...
    @property
    def numAtoms(self) -> Any: ...
    @property
    def numBonds(self) -> Any: ...
    @property
    def seedProcessed(self) -> Any: ...

class MCSResult(Boost.Python.instance):
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def __reduce__(self) -> Any: ...
    @property
    def canceled(self) -> Any: ...
    @property
    def numAtoms(self) -> Any: ...
    @property
    def numBonds(self) -> Any: ...
    @property
    def queryMol(self) -> Any: ...
    @property
    def smartsString(self) -> Any: ...

class RingCompare(Boost.Python.enum):
    IgnoreRingFusion: Any = ...
    PermissiveRingFusion: Any = ...
    StrictRingFusion: Any = ...
    names: Any = ...
    values: Any = ...
    __slots__: Any = ...
