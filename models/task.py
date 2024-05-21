from dataclasses import dataclass

@dataclass
class Task:
    execution_time: int
    deadline: int
    period: int
    property: int

