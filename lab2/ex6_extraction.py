import re

def extract_first_number(text):
    found = re.search(r'\d+', text)
    if found:
        return int(found.group())
    return None

text1 = "An apple is 123 USD"
text2 = "abc123abc"
text3 = "No numbers here!"

print(extract_first_number(text1))
print(extract_first_number(text2))
print(extract_first_number(text3))
