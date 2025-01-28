import random 
from typing import Dict, List

REPETITIONS: int = 1_000_000

def simulate_dice(dices: List[int]):
    buffer: Dict[int, int] = dict()
    for _ in range(REPETITIONS):
        throw = sum([random.randint(1, faces) for faces in dices])
        buffer[throw] = buffer.get(throw, 0) + 1
    for possibility in range(sum(dices) + 1):
        print(f"{possibility: >4}    {buffer.get(possibility, 0.00) / REPETITIONS * 100.0:.2f}%")

        
if __name__ == "__main__":
    simulate_dice([4, 6, 6])
