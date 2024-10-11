def is_palindrome(number):
    copy_num=number
    new_number=0
    while copy_num>0:
        new_number=new_number*10+copy_num%10
        copy_num=copy_num//10;

    if number==new_number:
        return 1
    else:
        return 0

num = int(input("Enter a number: "))

if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")