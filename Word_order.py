"""https://www.hackerrank.com/challenges/word-order/problem"""

counts = {}
for i in range(int(input())):
    word = input()
    if word in counts:
        counts[word][1] += 1
    else:
        counts.update({word: [i, 1]})

total = [str(value[1]) for value in sorted(counts.values())]
print(len(total))
print(" ".join(total))
