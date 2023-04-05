import itertools as its
words = "9876543210" # a set of password characters
r = its.product(words, repeat=8)  # random combination of 11 numbers
dic = open("pwd.txt", "a")      # store wifi combinations in file
for i in r:
    dic.write("".join(i))
    dic.write("".join("\n"))
dic.close()
