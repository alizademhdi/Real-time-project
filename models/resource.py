from dataclasses import dataclass
from models.task import Task

@dataclass
class Resourse:
    locked: bool
    owner: Task
