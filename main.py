f1 = open("Demo1.txt", "w")
f1.write("Hello how are you?\n")
f1.write("Welcome to the class of file handling.")
f1.write("\nenjoy the session")
f1.close()

f1 = open("Demo1.txt", "a")
f1.write("\nThis line is appended")
f1.close()

f1 = open("Demo1.txt", "r")
print(f1.read())


f1.close()