# find factors are odd or even
num = int(input("Enter the number"))

for i in range(1, num + 1):
    if (num % i) ==0:
        if (i % 2) == 0:
            print(i,"is even")
        else:
            print(i, "odd")

# Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically.

line = input("Enter your sentence")
words = line.split()
words.sort()
for i in words:
    print(i)

# Write a program, whichwill find all the numbers between 1000 and 3000 (both included) such that each digit of a
# number is an even number. The numbers obtained should be printed in a comma separated sequence on a single line.
items = []
for i in range(1000, 401+1):
        s = str(i)
        if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
            items.append(s)
            print( ",".join(items))

# Write a program that accepts a sentence and calculate the number of letters and digits
line = input("Please enter your sentence")
letter = 0
digit = 0
for ch in line:
    if ch.isdigit():
        digit = digit + 1
    elif ch.isalpha():
        letter = letter + 1
    else:
        pass
print("The total number of digits are:",digit)
print("The total number of letters are:",letter)


#Design a code which will find the given number is Palindrome number or not.

string = input("Enter your input")
rev= string[::-1]
if string == rev:
    print("This is a palindrome ")
elif string != rev:
    print("This is not a palindrome ")


