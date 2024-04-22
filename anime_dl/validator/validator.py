from __future__ import annotations
from abc import ABC, abstractmethod


class Validator(ABC):
    @abstractmethod
    def set_next(self, validator: Validator) -> Validator:
        pass

    @abstractmethod
    def validate(self, data: dict) -> None:
        pass
