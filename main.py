def get_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def print_word_count(text):
    words = text.split()
    print(f"Number of words in file: {len(words)}")

def print_letter_counts(text):
    chars = {}
    for word in text:
        for char in word:
            char = char.lower()
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1

    for char in sorted(chars, key=chars.get, reverse=True):
        print(f"Number of '{char}' in file: {chars[char]}")


if __name__ == "__main__":
    text = get_text()
    print_word_count(text)
    print_letter_counts(text)
