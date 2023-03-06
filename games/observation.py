from abc import ABC, abstractmethod
from typing import List
from games.action import Action

class Observation(ABC):
    """Abstract class that will define the observation of the game"""

    @abstractmethod
    def clone(self) -> 'Observation':
        """Return a copy of the observation"""
        pass
    
    @abstractmethod
    def copy_into(self, other: 'Observation') -> None:
        """Copy the observation into another observation"""
        pass

    @abstractmethod
    def is_action_valid(self, action: 'Action') -> bool:
        """Return True if the action is valid"""
        pass

    @abstractmethod
    def get_actions(self) -> List['Action']:
        """Return a list of valid actions"""
        pass

    @abstractmethod
    def get_random_action(self) -> 'Action':
        """Return a random valid action"""
        pass
