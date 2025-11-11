sent=input("Enter a string: ")
word=sent.split()
sent=" ".join(word[::-1])
print(sent)