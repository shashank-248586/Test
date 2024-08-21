def reading(file):
    with open (file,"r") as f:
        print(f.read())
    pass
def writting(file,content):
    with open(file,"w") as f:
        f.write(content)
    pass
def appending(file,content):
    with open(file,"a") as f:
        f.write(content)
    pass