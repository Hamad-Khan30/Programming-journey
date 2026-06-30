with open("dirct.txt","w") as f:
    f.write("This is the AI world. ")
    f.write("\nToday i'm Working on my last week work.")

with open("dirct.txt","r") as f:
    print(f.readlines())

with open("dirct.txt","a") as f:
    f.write("\nThis is hammad khan.")

with open("dirct.txt","r") as f:
    contents= f.read()
print(contents)
