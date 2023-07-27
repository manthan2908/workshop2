import sys
import string

word_dict ={}
total = 0
lines = sys.stdin.readline()
while lines != "":
    value_word = lines.split()
    key_word = value_word[0]
    count= int(value_word[1])
    total += count
    word_dict[key_word] = count
    lines = sys.stdin.readline()

for label,count in word_dict.items():
    print(label, "\t[")
    percentage = int(count)*100//total
    for i in range(0,percentage,5):
        print("*")
    print("]", percentage, "%")