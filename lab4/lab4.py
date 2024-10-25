#1
def set_operations(a, b):
    set_a = set(a)
    set_b = set(b)

    intersection = set_a & set_b
    union = set_a | set_b
    difference_a_b = set_a - set_b
    difference_b_a = set_b - set_a

    return [intersection, union, difference_a_b, difference_b_a]

a = [10, 2, 3, 40]
b = [3, 40, 5, 6]
result = set_operations(a, b)
print(result)

#2
def char_count(s):
    char_dict = {}
    for char in s:

        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

text = "Ana has apples."
result = char_count(text)
print(result)

#3
def compare_dicts(dict1, dict2):
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        if dict1.keys() != dict2.keys():
            return False
        for key in dict1:
            if not compare_dicts(dict1[key], dict2[key]):
                return False
        return True
    elif isinstance(dict1, list) and isinstance(dict2, list):
        if len(dict1) != len(dict2):
            return False
        for a, b in zip(dict1, dict2):
            if not compare_dicts(a, b):
                return False
        return True

    elif isinstance(dict1, set) and isinstance(dict2, set):
            return dict1 == dict2
    else:
            return dict1 == dict2

dict1 = {
    "a": 1,
    "b": {"c": 2, "d": [1, 2, 3]}
}
dict2 = {
    "a": 1,
    "b": {"c": 2, "d": [1, 2, 3]}
}

print(compare_dicts(dict1, dict2))

#4
def build_xml_element(tag, content, **key_val):
    key_value__string = ""
    for key, value in key_val.items():
        key_value__string += f' {key}="{value}"'

    xml_element = f"<{tag}{key_value__string}>{content}</{tag}>"
    return xml_element

result = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
print(result)

#5
def validate_dict(rules, dictionary):
    for key, prefix, middle, suffix in rules:
        if key not in dictionary:
            return False
        value = dictionary[key]
        if not (value.startswith(prefix) and middle in value and value.endswith(suffix)):
            return False
    return True

rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
d = {
    "key1": "come inside, it's too cold out",
    "key2": "start  middle end"
}
print(validate_dict(rules, d))

#6
def unique_and_duplicates(lst):
    print(len(lst))
    unique = set(lst)
    num_unique = len(unique)
    num_duplicates = len(lst) - num_unique
    return (num_unique, num_duplicates)

print(unique_and_duplicates([1,2,2,3,4,4,5,6]))

#7
def set_operations(*sets):
    result = {}
    set_list = list(sets)

    for i in range(len(set_list)):
        for j in range(i + 1, len(set_list)):
            set_a = set_list[i]
            set_b = set_list[j]

            union = set_a | set_b
            intersection = set_a & set_b
            difference_a_b = set_a - set_b
            difference_b_a = set_b - set_a

            result[f"{set_a} | {set_b}"] = union
            result[f"{set_a} & {set_b}"] = intersection
            result[f"{set_a} - {set_b}"] = difference_a_b
            result[f"{set_b} - {set_a}"] = difference_b_a

    return result

print(set_operations({1,2}, {2, 3}))

#8
def loop(mapping):
    current_key = mapping["start"]
    visited = []

    while current_key not in visited:
        visited.append(current_key)
        current_key = mapping.get(current_key)

    return visited

print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))

#9
def my_function(*args, **key):
    key_values = set(key.values())
    count=0
    for arg in args:
        if arg in key_values:
            count += 1

    return count

result = my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5)
print(result)
