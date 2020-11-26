from qt import *
from qtcanvas import *
from math import *
from rdkit.sping import pid as pid
from typing import Any, Optional

class QCanvasRotText(QCanvasText):
    def __init__(self, txt: Any, canvas: Any, angle: int = ...) -> None: ...
    def draw(self, qP: Any) -> None: ...

class QtCanvas(pid.Canvas):
    size: Any = ...
    objs: Any = ...
    nObjs: int = ...
    def __init__(self, destCanvas: Any, size: Any = ..., name: str = ...) -> None: ...
    def clear(self) -> None: ...
    def flush(self) -> None: ...
    def save(self, file: Optional[Any] = ..., format: Optional[Any] = ...) -> None: ...
    def drawLine(self, x1: Any, y1: Any, x2: Any, y2: Any, color: Optional[Any] = ..., width: Optional[Any] = ..., dash: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def drawPolygon(self, pointlist: Any, edgeColor: Optional[Any] = ..., edgeWidth: Optional[Any] = ..., fillColor: Any = ..., closed: int = ..., dash: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def drawString(self, s: Any, x: Any, y: Any, font: Optional[Any] = ..., color: Optional[Any] = ..., angle: int = ..., **kwargs: Any) -> None: ...
    def drawImage(self, image: Any, x1: Any, y1: Any, x2: Optional[Any] = ..., y2: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def stringWidth(self, s: Any, font: Optional[Any] = ...): ...
    def fontAscent(self, font: Optional[Any] = ...): ...
    def fontDescent(self, font: Optional[Any] = ...): ...

def test(canvas: Any): ...
def dashtest(canvas: Any): ...
