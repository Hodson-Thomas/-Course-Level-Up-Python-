def sort_string_by_words(string: str) -> str:
    words = string.split()
    words = sorted(words, key=lambda w : w.lower())
    return " ".join(words)

if __name__ == "__main__":
    assert sort_string_by_words("strings of words") == "of strings words"
    assert sort_string_by_words("banana ORANGE apple") == "apple banana ORANGE"
