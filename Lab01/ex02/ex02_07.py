print("Type a paragraph (Type 'done' to finish):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
print("Your paragraph has been turn to uppercase:")
for line in lines:
    print(line.upper())
# The code above is a simple program that allows the user to input multiple lines of text until they type 'done'.