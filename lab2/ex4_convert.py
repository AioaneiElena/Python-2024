def camel_to_snake_case(s):
    underscorestring= []

    for char in s:
        if char.isupper() and underscorestring:
            underscorestring.append('_')
        underscorestring.append(char.lower())

    return ''.join(underscorestring)

camel_case_string= input("Enter a string in UpperCamelCase: ")
snake_case_string= camel_to_snake_case(camel_case_string)

print(f"Converted string: {snake_case_string}")
