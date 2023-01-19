from abc import ABC, abstractmethod


class IFilter(ABC):

    @abstractmethod
    def apply(self, stmt):
        pass
