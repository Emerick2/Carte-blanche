from abc import ABC, abstractmethod
import io, hashlib, hmac

class GameElement :
    def __init__(self, newId : str, name : str, description : str) :
        self.id = newId
        self.name = name
        self.description = description
    
    def to_dict(self):
        pass


class Item(GameElement) :
    pass


class Door(GameElement) :
    def __init__(self, is_locked : bool, required_item_id : str = "") :
        self.is_locked = is_locked
        self.required_item_id = required_item_id


class Puzzle(ABC):
    @abstractmethod
    def check_solution(self, answer : str) :
        return True

class CodePuzzle(Puzzle):
    def check_solution(self, answer : str) :
        return answer == "1234"
    

class HashPuzzle(Puzzle):
    def check_solution(self, answer : str) :
        mac1 = hmac.HMAC(b"key", b"somedata", digestmod=hashlib.sha512)
        mac2 = hmac.HMAC(b"key", b"somedata", digestmod=hashlib.sha512)
        return mac1.digest() == mac2.digest()


HashPuzzle().check_solution("secret")

class Room :
    def __init__(self):
        self.id : int = 0
        self.name : str = ""
        self.description : str = "" 
        self.item = [] # Item[] 
        self.doors = [] # Door[] 
        self.puzzles = [] # Puzzle[] 

