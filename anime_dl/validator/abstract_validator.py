from __future__ import annotations
from abc import abstractmethod

from .validator import Validator


class AbstractValidator(Validator):
    _next_validator: Validator = None

    def set_next(self, validator: Validator) -> Validator:
        self._next_validator = validator
        return validator

    @abstractmethod
    def validate(self, data: dict) -> None:
        if self._next_validator:
            return self._next_validator.validate(data)

        return None
