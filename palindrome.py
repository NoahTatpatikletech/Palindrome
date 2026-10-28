import sys

num = int(sys.argv[1])

original_num = num   
rev = 0

while num != 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10  

print("The reversed number is =", rev)

if original_num == rev:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
