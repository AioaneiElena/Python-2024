def count_bits(number):
    count=0
    while number>0:
      if number%2==1:
          count+=1
      number=number//2

    return count

print(count_bits(23))