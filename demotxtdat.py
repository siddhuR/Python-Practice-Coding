f1=open("demo1.txt","w+")
text1=f1.write("hello how are you...?   \nwelcome to the chapter file handling   \nenjoy the session")
text1
f1.close()
f2=open("demo1.txt",'r')
text2=f2.read()
text2
f2.close()

f = open("test.dat","w")
f.write("line one\nline two\nline three\n")
f1.close()