string_to_count="abecedar"
vowels=0
for char in string_to_count :
    if char.lower() in "aeiou":
        vowels+=1

print(f"The number of vowels is: {vowels}")