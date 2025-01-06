def sort_on(dict):
    return dict["num"]


def get_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

file_contents = get_text()

words = file_contents.split()
print(f"Number of words in file: {len(words)}")

chars = {}
for word in words:
    for char in word:
        char = char.lower()
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

for char in sorted(chars, key=chars.get, reverse=True):
    print(f"Number of '{char}' in file: {chars[char]}") 

