from abc import ABCMeta, abstractmethod

class User(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def createNum(self):
        pass