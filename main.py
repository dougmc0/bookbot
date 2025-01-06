def get_text(file):
    with open(file) as f:
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
        if char.isalpha():
            print(f"The '{char}' character was found {chars[char]} times")


if __name__ == "__main__":
    file = "books/frankenstein.txt"
    print (f"--- Begin report of {file} ---")
    text = get_text(file)
    print_word_count(text)
    print_letter_counts(text)
