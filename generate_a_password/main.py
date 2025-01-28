import random
from typing import Dict

def generate_number() -> int:
    result = 0
    for _ in range(5):
        result *= 10
        result += random.randint(1, 6)
    return result

def generate_password(word_count: int) -> str:
    words: Dict[int, str] = dict()
    with open("generate_a_password/word_list.txt", "r") as file:
        for line in file.readlines():
            if len(sline := line.strip().split('\t')) != 2:
                continue
            words[int(sline[0])] = sline[1]
    return ' '.join([words[generate_number()] for _ in range(word_count)])

if __name__ == "__main__":
    print(generate_password(5))
