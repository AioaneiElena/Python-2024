def count_words(text):
    words = text.split(" ")
    return len(words)

text = "Ana are mere"
print(count_words(text))