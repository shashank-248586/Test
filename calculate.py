file = "expenses.txt" 
def sum(file):
    with open(file,"r") as f:
        a = f.read()
        sum  = 0
        for i in a:
            sum+= i
        return sum
    