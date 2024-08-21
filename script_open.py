file = "inventory.txt"
def read_text(file):
    with open(file,"r") as f:
        print(f.read())
    pass