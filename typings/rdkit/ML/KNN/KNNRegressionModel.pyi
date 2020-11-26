from rdkit.ML.KNN import KNNModel as KNNModel
from typing import Any, Optional

class KNNRegressionModel(KNNModel.KNNModel):
    def __init__(self, k: Any, attrs: Any, dfunc: Any, radius: Optional[Any] = ...) -> None: ...
    def type(self): ...
    def SetBadExamples(self, examples: Any) -> None: ...
    def GetBadExamples(self): ...
    def NameModel(self, varNames: Any) -> None: ...
    def PredictExample(self, example: Any, appendExamples: int = ..., weightedAverage: int = ..., neighborList: Optional[Any] = ...): ...
