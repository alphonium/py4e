def count(word, char):
    count = 0
    for letter in word:
        if letter == char:
            count = count + 1
    return count

word = input("Enter a word: ")
char = input("Enter a letter to find: ")
print(count(word, char))
