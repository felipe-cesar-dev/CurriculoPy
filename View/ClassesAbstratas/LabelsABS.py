from abc import abstractmethod, ABC


class LabelsAbstrata(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def criarLabels(self, camada):
        pass
    @abstractmethod
    def labels(self, camada, w, h):
        pass