from __future__ import annotations

from src.segment import Segment


class Event:
    """
    Esta classe tem dois propósitos:
        1. Evitar o uso de tuplas, provendo acesso direto aos membros com nomes mais descritivos
        2. Prover um comparador para os eventos, levando em consideração coordenadas e orientação
    """

    def __init__(self, x: float, y: float, l: bool, s: Segment, i: int = -1) -> None:
        self.x = x
        self.y = y
        self.isLeft = l
        self.segment = s
        self.id = i

    def __repr__(self) -> str:
        return f"[({self.x}, {self.y}, {self.isLeft})]"

    def compare(self, other: Event):
        if self.x < other.x:
            return -1
        if self.x == other.x and self.isLeft == True and other.isLeft == False:
            return -1
        if self.x == other.x and self.isLeft == False and other.isLeft == True:
            return 1
        if self.x == other.x and self.y < other.y:
            return -1
        if self.x == other.x and self.y == other.y:
            return 0
        else:
            return 1

    def __lt__(self, other: Event):
        return self.compare(other) < 0