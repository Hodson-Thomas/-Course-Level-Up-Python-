def sort_string_by_words(string: str) -> str:
    return " ".join(sorted(string.split(), key=lambda w : w.lower()))

if __name__ == "__main__":
    assert sort_string_by_words("strings of words") == "of strings words"
    assert sort_string_by_words("banana ORANGE apple") == "apple banana ORANGE"
