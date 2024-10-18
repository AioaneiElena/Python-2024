#1
def fibonacci(n):
    if n<= 0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0, 1]

    fib_secv= [0, 1]
    for i in range(2, n):
        next_number= fib_secv[i-1]+fib_secv[i-2]
        fib_secv.append(next_number)

    return fib_secv

#2
def is_prime(num):
    if num<= 1:
        return False
    for i in range(2, int(num ** 0.5)+1):
        if num% i==0:
            return False
    return True

def get_prime(numbers):
    return [num for num in numbers if is_prime(num)]

#3
def list_operations(a, b):
    a_set= set(a)
    b_set= set(b)

    intersection= list(a_set.intersection(b_set))
    union= list(a_set.union(b_set))
    a_minus_b= list(a_set.difference(b_set))
    b_minus_a= list(b_set.difference(a_set))

    return (intersection, union, a_minus_b, b_minus_a)
#4
def compose(notes, moves, poz):
    song= []
    current_poz= poz
    song.append(notes[current_pos])

    for move in moves:
        current_poz= (current_poz+ move)% len(notes)
        song.append(notes[current_poz])

    return song

#5
def zero_diagonal(matrix):
    n=len(matrix)

    for i in range(n):
        for j in range(i):
            matrix[i][j]= 0
    return matrix

#6
def find_elements(x, *lists):
    counts= {}
    for lst in lists:
        for item in lst:
            if item in counts:
                counts[item]+= 1
            else:
                counts[item]= 1

    result = []
    for element, count in counts.items():
        if count==x:
            result.append(element)

    return result

#7
def palindrome(numbers):

    def is_palindrome(n):
        copy = n
        new_num = 0
        while copy > 0:
            a = copy % 10
            new_num = new_num * 10 + a
            copy = copy // 10

        return n==new_num

    palindromes= [num for num in numbers if is_palindrome(num)]
    return (len(palindromes), max(palindromes) if palindromes else None)

#8
def ascii_chars(x=1, string_list=[], flag=True):
    result= []
    for string in string_list:
        if flag:
            chars= [char for char in string if ord(char) % x == 0]
        else:
            chars= [char for char in string if ord(char) % x != 0]
        result.append(chars)
    return result

#9
def spectators(matrix):
    spectators=[]
    rows=len(matrix)
    cols=len(matrix[0])

    for i in range(1, rows):
        for j in range(cols):
            for k in range(i):
                if matrix[k][j] >= matrix[i][j]:
                    spectators.append((i, j))
                    break
    return spectators

#10
def tuple_lists(*lists):
    max_len=max(len(lst) for lst in lists)
    result=[]
    for i in range(max_len):
        tuple_elements=[]
        for lst in lists:
            if i < len(lst):
                tuple_elements.append(lst[i])
            else:
                tuple_elements.append(None)

        result.append(tuple(tuple_elements))

    return result

#11
def get_third_char(tup):
    if len(tup[1]) >= 3:
        return tup[1][2]
    else:
        return ""

def sort_by_third_char(tuples_list):
    sorted_list = sorted(tuples_list, key=get_third_char)
    return sorted_list

#12
def group_by_rhyme(words):
    rhyme={}
    for word in words:
        if len(word) >= 2:
            end= word[-2:]
        else:
            end= word

        if end not in rhyme:
            rhyme[end] = []
        rhyme[end].append(word)
    return list(rhyme.values())

print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))