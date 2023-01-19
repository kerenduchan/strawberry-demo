from abc import ABC, abstractmethod


class IDbFilter(ABC):

    @abstractmethod
    def apply(self, stmt):
        pass
