from sys import stdin

N = int(stdin.readline())
words = stdin.read().splitlines()
weight = {}
sum = 0

for word in words:
    word = list(word)
    for j, char in enumerate(word):
        if not char in weight:
            weight[char] = pow(10, len(word)-j-1)
        else:
            weight[char] = weight.get(char) + pow(10, len(word)-j-1)

list = sorted(weight, key=lambda x:weight[x], reverse=True)

for i, char in enumerate(list):
    for j, word in enumerate(words):
        words[j] = word.replace(char, str(9-i))

for word in words:
    sum += int(word)

print(sum)