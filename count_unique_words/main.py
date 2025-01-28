from typing import Dict
import string

def count_unique_words(file_path: str, display_top_n: int):
    buffer: Dict[str, int] = dict()
    with open(file_path, 'r', encoding='utf8') as file:
        for line in file.readlines():
            for p in string.punctuation:
                line = line.replace(p, ' ')
            for word in line.strip().split():
                buffer[word] = buffer.get(word, 0) + 1
    count = sum(buffer.values())
    for i, word in enumerate(sorted(buffer.keys(), key=lambda key: buffer[key])[:display_top_n], start=1):
        print(f"{i: <5}{word: <30}{buffer[word] / count * 100.0:.2f}%") 

if __name__ == "__main__":
    count_unique_words("count_unique_words/data.txt", 20)
