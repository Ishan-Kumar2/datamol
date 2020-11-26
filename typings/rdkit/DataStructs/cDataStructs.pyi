from typing import overload
import Boost.Python
EIGHTBITVALUE: Any
FOURBITVALUE: Any
ONEBITVALUE: Any
SIXTEENBITVALUE: Any
TWOBITVALUE: Any

def AllBitSimilarity(*args, **kwargs) -> Any: ...
def AllProbeBitsMatch(*args, **kwargs) -> Any: ...
def AsymmetricSimilarity(*args, **kwargs) -> Any: ...
@overload
def BitVectToBinaryText(SparseBitVect) -> Any: ...
@overload
def BitVectToBinaryText(ExplicitBitVect) -> Any: ...
@overload
def BitVectToFPSText(SparseBitVect) -> Any: ...
@overload
def BitVectToFPSText(ExplicitBitVect) -> Any: ...
@overload
def BitVectToText(SparseBitVect) -> Any: ...
@overload
def BitVectToText(ExplicitBitVect) -> Any: ...
def BraunBlanquetSimilarity(*args, **kwargs) -> Any: ...
@overload
def BulkAllBitSimilarity(ExplicitBitVect, boost) -> Any: ...
@overload
def BulkAllBitSimilarity(ExplicitBitVect, boost) -> Any: ...
@overload
def BulkAsymmetricSimilarity(SparseBitVect, boost) -> Any: ...
@overload
def BulkAsymmetricSimilarity(ExplicitBitVect, boost) -> Any: ...
@overload
def BulkBraunBlanquetSimilarity(SparseBitVect, boost) -> Any: ...
@overload
def BulkBraunBlanquetSimilarity(ExplicitBitVect, boost) -> Any: ...
@overload
def BulkCosineSimilarity(SparseBitVect, boost) -> Any: ...
@overload
def BulkCosineSimilarity(ExplicitBitVect, boost) -> Any: ...
@overload
def BulkDiceSimilarity(SparseBitVect, boost) -> Any: ...
@overload
def BulkDiceSimilarity(ExplicitBitVect, boost) -> Any: ...
@overload
def BulkDiceSimilarity(RDKit, boost) -> Any: ...
@overload
def BulkDiceSimilarity(RDKit, boost) -> Any: ...
@overload
def BulkDiceSimilarity(RDKit, boost) -> Any: ...
@overload
def BulkDiceSimilarity(RDKit, boost) -> Any: ...
@overload
def BulkKulczynskiSimilarity(SparseBitVect, boost) -> Any: ...
@overload
def BulkKulczynskiSimilarity(ExplicitBitVect, boost) -> Any: ...
@overload
def BulkMcConnaugheySimilarity(SparseBitVect, boost) -> Any: ...
@overload
def BulkMcConnaugheySimilarity(ExplicitBitVect, boost) -> Any: ...
@overload
def BulkOnBitSimilarity(ExplicitBitVect, boost) -> Any: ...
@overload
def BulkOnBitSimilarity(ExplicitBitVect, boost) -> Any: ...
@overload
def BulkRogotGoldbergSimilarity(SparseBitVect, boost) -> Any: ...
@overload
def BulkRogotGoldbergSimilarity(ExplicitBitVect, boost) -> Any: ...
@overload
def BulkRusselSimilarity(SparseBitVect, boost) -> Any: ...
@overload
def BulkRusselSimilarity(ExplicitBitVect, boost) -> Any: ...
@overload
def BulkSokalSimilarity(SparseBitVect, boost) -> Any: ...
@overload
def BulkSokalSimilarity(ExplicitBitVect, boost) -> Any: ...
@overload
def BulkTanimotoSimilarity(SparseBitVect, boost) -> Any: ...
@overload
def BulkTanimotoSimilarity(ExplicitBitVect, boost) -> Any: ...
@overload
def BulkTanimotoSimilarity(RDKit, boost) -> Any: ...
@overload
def BulkTanimotoSimilarity(RDKit, boost) -> Any: ...
@overload
def BulkTanimotoSimilarity(RDKit, boost) -> Any: ...
@overload
def BulkTanimotoSimilarity(RDKit, boost) -> Any: ...
def BulkTverskySimilarity(*args, **kwargs) -> Any: ...
def ComputeL1Norm(*args, **kwargs) -> Any: ...
def ConvertToExplicit(*args, **kwargs) -> Any: ...
@overload
def ConvertToNumpyArray(ExplicitBitVect, boost) -> Any: ...
@overload
def ConvertToNumpyArray(RDKit, boost) -> Any: ...
@overload
def ConvertToNumpyArray(RDKit, boost) -> Any: ...
@overload
def ConvertToNumpyArray(RDKit, boost) -> Any: ...
@overload
def ConvertToNumpyArray(RDKit, boost) -> Any: ...
@overload
def ConvertToNumpyArray(RDKit, boost) -> Any: ...
def CosineSimilarity(*args, **kwargs) -> Any: ...
def CreateFromBinaryText(*args, **kwargs) -> Any: ...
def CreateFromBitString(*args, **kwargs) -> Any: ...
def CreateFromFPSText(*args, **kwargs) -> Any: ...
def DiceSimilarity(*args, **kwargs) -> Any: ...
def FoldFingerprint(*args, **kwargs) -> Any: ...
def InitFromDaylightString(*args, **kwargs) -> Any: ...
def KulczynskiSimilarity(*args, **kwargs) -> Any: ...
def McConnaugheySimilarity(*args, **kwargs) -> Any: ...
def NumBitsInCommon(*args, **kwargs) -> Any: ...
def OffBitProjSimilarity(*args, **kwargs) -> Any: ...
def OffBitsInCommon(*args, **kwargs) -> Any: ...
def OnBitProjSimilarity(*args, **kwargs) -> Any: ...
def OnBitSimilarity(*args, **kwargs) -> Any: ...
def OnBitsInCommon(*args, **kwargs) -> Any: ...
def RogotGoldbergSimilarity(*args, **kwargs) -> Any: ...
def RusselSimilarity(*args, **kwargs) -> Any: ...
def SokalSimilarity(*args, **kwargs) -> Any: ...
def TanimotoSimilarity(*args, **kwargs) -> Any: ...
def TverskySimilarity(*args, **kwargs) -> Any: ...

class DiscreteValueType(Boost.Python.enum):
    EIGHTBITVALUE: Any = ...
    FOURBITVALUE: Any = ...
    ONEBITVALUE: Any = ...
    SIXTEENBITVALUE: Any = ...
    TWOBITVALUE: Any = ...
    names: Any = ...
    values: Any = ...
    __slots__: Any = ...

class DiscreteValueVect(Boost.Python.instance):
    __instance_size__: Any = ...
    __safe_for_unpickling__: Any = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def GetTotalVal(RDKit) -> Any: ...
    @classmethod
    def GetValueType(RDKit) -> Any: ...
    @classmethod
    def __add__(self, other) -> Any: ...
    @classmethod
    def __and__(self, other) -> Any: ...
    @classmethod
    def __getinitargs__(RDKit) -> Any: ...
    @classmethod
    def __getitem__(RDKit, unsignedint) -> Any: ...
    @classmethod
    def __iadd__(boost, RDKit) -> Any: ...
    @classmethod
    def __isub__(boost, RDKit) -> Any: ...
    @classmethod
    def __len__(RDKit) -> Any: ...
    @classmethod
    def __or__(self, other) -> Any: ...
    @classmethod
    def __reduce__(self) -> Any: ...
    @classmethod
    def __setitem__(self, index, object) -> Any: ...
    @classmethod
    def __sub__(self, other) -> Any: ...

class ExplicitBitVect(Boost.Python.instance):
    __instance_size__: Any = ...
    __safe_for_unpickling__: Any = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def FromBase64(self, *args, **kwargs) -> Any: ...
    @classmethod
    def GetBit(self, *args, **kwargs) -> Any: ...
    @classmethod
    def GetNumBits(self, *args, **kwargs) -> Any: ...
    @classmethod
    def GetNumOffBits(self, *args, **kwargs) -> Any: ...
    @classmethod
    def GetNumOnBits(self, *args, **kwargs) -> Any: ...
    @classmethod
    def GetOnBits(ExplicitBitVect) -> Any: ...
    @classmethod
    def SetBit(self, *args, **kwargs) -> Any: ...
    @classmethod
    def SetBitsFromList(self, *args, **kwargs) -> Any: ...
    @classmethod
    def ToBase64(self, *args, **kwargs) -> Any: ...
    @classmethod
    def ToBinary(ExplicitBitVect) -> Any: ...
    @classmethod
    def ToBitString(self, *args, **kwargs) -> Any: ...
    @classmethod
    def UnSetBit(self, *args, **kwargs) -> Any: ...
    @classmethod
    def UnSetBitsFromList(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __add__(self, other) -> Any: ...
    @classmethod
    def __and__(self, other) -> Any: ...
    @classmethod
    def __eq__(self, other) -> Any: ...
    @classmethod
    def __getinitargs__(ExplicitBitVect) -> Any: ...
    @classmethod
    def __getitem__(ExplicitBitVect, int) -> Any: ...
    @classmethod
    def __iadd__(boost, ExplicitBitVect) -> Any: ...
    @classmethod
    def __invert__(self) -> Any: ...
    @classmethod
    def __len__(self) -> Any: ...
    @classmethod
    def __ne__(self, other) -> Any: ...
    @classmethod
    def __or__(self, other) -> Any: ...
    @classmethod
    def __reduce__(self) -> Any: ...
    @classmethod
    def __setitem__(self, index, object) -> Any: ...
    @classmethod
    def __xor__(self, other) -> Any: ...

class FPBReader(Boost.Python.instance):
    __instance_size__: Any = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def GetBytes(RDKit, unsignedint) -> Any: ...
    @classmethod
    def GetContainingNeighbors(self, *args, **kwargs) -> Any: ...
    @classmethod
    def GetFP(RDKit, unsignedint) -> Any: ...
    @classmethod
    def GetId(RDKit, unsignedint) -> Any: ...
    @classmethod
    def GetNumBits(RDKit) -> Any: ...
    @classmethod
    def GetTanimoto(self, *args, **kwargs) -> Any: ...
    @classmethod
    def GetTanimotoNeighbors(self, *args, **kwargs) -> Any: ...
    @classmethod
    def GetTversky(self, *args, **kwargs) -> Any: ...
    @classmethod
    def GetTverskyNeighbors(self, *args, **kwargs) -> Any: ...
    @classmethod
    def Init(RDKit) -> Any: ...
    @classmethod
    def __getitem__(RDKit, unsignedint) -> Any: ...
    @classmethod
    def __len__(RDKit) -> Any: ...
    @classmethod
    def __reduce__(self) -> Any: ...

class IntSparseIntVect(Boost.Python.instance):
    __instance_size__: Any = ...
    __safe_for_unpickling__: Any = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def GetLength(RDKit) -> Any: ...
    @classmethod
    def GetNonzeroElements(RDKit) -> Any: ...
    @classmethod
    def GetTotalVal(RDKit) -> Any: ...
    @classmethod
    def ToBinary(RDKit) -> Any: ...
    @classmethod
    def UpdateFromSequence(RDKit, boost) -> Any: ...
    @classmethod
    def __add__(self, other) -> Any: ...
    @classmethod
    def __and__(self, other) -> Any: ...
    @classmethod
    def __eq__(self, other) -> Any: ...
    @classmethod
    def __getinitargs__(RDKit) -> Any: ...
    @classmethod
    def __getitem__(RDKit, int) -> Any: ...
    @classmethod
    @overload
    def __iadd__(boost, RDKit) -> Any: ...
    @overload
    def __iadd__(boost, int) -> Any: ...
    @classmethod
    def __idiv__(boost, int) -> Any: ...
    @classmethod
    def __imul__(boost, int) -> Any: ...
    @classmethod
    @overload
    def __isub__(boost, RDKit) -> Any: ...
    @overload
    def __isub__(boost, int) -> Any: ...
    @classmethod
    def __ne__(self, other) -> Any: ...
    @classmethod
    def __or__(self, other) -> Any: ...
    @classmethod
    def __reduce__(self) -> Any: ...
    @classmethod
    def __setitem__(self, index, object) -> Any: ...
    @classmethod
    def __sub__(self, other) -> Any: ...

class LongSparseIntVect(Boost.Python.instance):
    __instance_size__: Any = ...
    __safe_for_unpickling__: Any = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def GetLength(RDKit) -> Any: ...
    @classmethod
    def GetNonzeroElements(RDKit) -> Any: ...
    @classmethod
    def GetTotalVal(RDKit) -> Any: ...
    @classmethod
    def ToBinary(RDKit) -> Any: ...
    @classmethod
    def UpdateFromSequence(RDKit, boost) -> Any: ...
    @classmethod
    def __add__(self, other) -> Any: ...
    @classmethod
    def __and__(self, other) -> Any: ...
    @classmethod
    def __eq__(self, other) -> Any: ...
    @classmethod
    def __getinitargs__(RDKit) -> Any: ...
    @classmethod
    def __getitem__(RDKit, long) -> Any: ...
    @classmethod
    @overload
    def __iadd__(boost, RDKit) -> Any: ...
    @overload
    def __iadd__(boost, int) -> Any: ...
    @classmethod
    def __idiv__(boost, int) -> Any: ...
    @classmethod
    def __imul__(boost, int) -> Any: ...
    @classmethod
    @overload
    def __isub__(boost, RDKit) -> Any: ...
    @overload
    def __isub__(boost, int) -> Any: ...
    @classmethod
    def __ne__(self, other) -> Any: ...
    @classmethod
    def __or__(self, other) -> Any: ...
    @classmethod
    def __reduce__(self) -> Any: ...
    @classmethod
    def __setitem__(RDKit, long, int) -> Any: ...
    @classmethod
    def __sub__(self, other) -> Any: ...

class MultiFPBReader(Boost.Python.instance):
    __instance_size__: Any = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def AddReader(self, *args, **kwargs) -> Any: ...
    @classmethod
    def GetContainingNeighbors(self, *args, **kwargs) -> Any: ...
    @classmethod
    def GetNumBits(RDKit) -> Any: ...
    @classmethod
    def GetReader(RDKit, unsignedint) -> Any: ...
    @classmethod
    def GetTanimotoNeighbors(self, *args, **kwargs) -> Any: ...
    @classmethod
    def GetTverskyNeighbors(self, *args, **kwargs) -> Any: ...
    @classmethod
    def Init(RDKit) -> Any: ...
    @classmethod
    def __len__(RDKit) -> Any: ...
    @classmethod
    def __reduce__(self) -> Any: ...

class SparseBitVect(Boost.Python.instance):
    __instance_size__: Any = ...
    __safe_for_unpickling__: Any = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def FromBase64(self, *args, **kwargs) -> Any: ...
    @classmethod
    def GetBit(self, *args, **kwargs) -> Any: ...
    @classmethod
    def GetNumBits(self, *args, **kwargs) -> Any: ...
    @classmethod
    def GetNumOffBits(self, *args, **kwargs) -> Any: ...
    @classmethod
    def GetNumOnBits(self, *args, **kwargs) -> Any: ...
    @classmethod
    def GetOnBits(SparseBitVect) -> Any: ...
    @classmethod
    def SetBit(self, *args, **kwargs) -> Any: ...
    @classmethod
    def SetBitsFromList(self, *args, **kwargs) -> Any: ...
    @classmethod
    def ToBase64(self, *args, **kwargs) -> Any: ...
    @classmethod
    def ToBinary(SparseBitVect) -> Any: ...
    @classmethod
    def ToBitString(self, *args, **kwargs) -> Any: ...
    @classmethod
    def UnSetBit(self, *args, **kwargs) -> Any: ...
    @classmethod
    def UnSetBitsFromList(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __and__(self, other) -> Any: ...
    @classmethod
    def __eq__(self, other) -> Any: ...
    @classmethod
    def __getinitargs__(SparseBitVect) -> Any: ...
    @classmethod
    def __getitem__(SparseBitVect, int) -> Any: ...
    @classmethod
    def __invert__(self) -> Any: ...
    @classmethod
    def __len__(self) -> Any: ...
    @classmethod
    def __ne__(self, other) -> Any: ...
    @classmethod
    def __or__(self, other) -> Any: ...
    @classmethod
    def __reduce__(self) -> Any: ...
    @classmethod
    def __setitem__(self, index, object) -> Any: ...
    @classmethod
    def __xor__(self, other) -> Any: ...

class UIntSparseIntVect(Boost.Python.instance):
    __instance_size__: Any = ...
    __safe_for_unpickling__: Any = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def GetLength(RDKit) -> Any: ...
    @classmethod
    def GetNonzeroElements(RDKit) -> Any: ...
    @classmethod
    def GetTotalVal(RDKit) -> Any: ...
    @classmethod
    def ToBinary(RDKit) -> Any: ...
    @classmethod
    def UpdateFromSequence(RDKit, boost) -> Any: ...
    @classmethod
    def __add__(self, other) -> Any: ...
    @classmethod
    def __and__(self, other) -> Any: ...
    @classmethod
    def __eq__(self, other) -> Any: ...
    @classmethod
    def __getinitargs__(RDKit) -> Any: ...
    @classmethod
    def __getitem__(RDKit, unsignedint) -> Any: ...
    @classmethod
    @overload
    def __iadd__(boost, RDKit) -> Any: ...
    @overload
    def __iadd__(boost, int) -> Any: ...
    @classmethod
    def __idiv__(boost, int) -> Any: ...
    @classmethod
    def __imul__(boost, int) -> Any: ...
    @classmethod
    @overload
    def __isub__(boost, RDKit) -> Any: ...
    @overload
    def __isub__(boost, int) -> Any: ...
    @classmethod
    def __ne__(self, other) -> Any: ...
    @classmethod
    def __or__(self, other) -> Any: ...
    @classmethod
    def __reduce__(self) -> Any: ...
    @classmethod
    def __setitem__(RDKit, unsignedint, int) -> Any: ...
    @classmethod
    def __sub__(self, other) -> Any: ...

class ULongSparseIntVect(Boost.Python.instance):
    __instance_size__: Any = ...
    __safe_for_unpickling__: Any = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def GetLength(RDKit) -> Any: ...
    @classmethod
    def GetNonzeroElements(RDKit) -> Any: ...
    @classmethod
    def GetTotalVal(RDKit) -> Any: ...
    @classmethod
    def ToBinary(RDKit) -> Any: ...
    @classmethod
    def UpdateFromSequence(RDKit, boost) -> Any: ...
    @classmethod
    def __add__(self, other) -> Any: ...
    @classmethod
    def __and__(self, other) -> Any: ...
    @classmethod
    def __eq__(self, other) -> Any: ...
    @classmethod
    def __getinitargs__(RDKit) -> Any: ...
    @classmethod
    def __getitem__(RDKit, unsignedlong) -> Any: ...
    @classmethod
    @overload
    def __iadd__(boost, RDKit) -> Any: ...
    @overload
    def __iadd__(boost, int) -> Any: ...
    @classmethod
    def __idiv__(boost, int) -> Any: ...
    @classmethod
    def __imul__(boost, int) -> Any: ...
    @classmethod
    @overload
    def __isub__(boost, RDKit) -> Any: ...
    @overload
    def __isub__(boost, int) -> Any: ...
    @classmethod
    def __ne__(self, other) -> Any: ...
    @classmethod
    def __or__(self, other) -> Any: ...
    @classmethod
    def __reduce__(self) -> Any: ...
    @classmethod
    def __setitem__(RDKit, unsignedlong, int) -> Any: ...
    @classmethod
    def __sub__(self, other) -> Any: ...
