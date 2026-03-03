# take input of word
string = input("enter a word: ")
# take input of character
char = input ("Enter a character: ")
i = 0
count = 0
while i < len(string):
    if string[i] == char:
        count = count + 1
    i = i + 1
print("the number of times " ,char , " occurs = ", count)
