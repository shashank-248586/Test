n = int(input("Enter the no of emploee"))
file  = r"employee.txt"
content =""
for i in range(n):
    name = input(f"Enter the name of {i+1}th employee ")
    age = input(f"Enter the age of {i+1}th employee ")
    salary = input(f"Enter the salary of {i+1}th employee ")
    string = f"name-{name} age-{age} salary{salary}"
    content+=string+"\n"

with open(file,"w") as f:
    f.read(content)