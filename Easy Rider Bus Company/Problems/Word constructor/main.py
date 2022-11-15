string_1 = input()
string_2 = input()

for word_1, word_2 in zip(string_1, string_2):
    print(word_1, word_2, sep="", end="")
