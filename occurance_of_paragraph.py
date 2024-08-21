file=  "paragraph.txt" 
context =""
with open(file,"r")as f:
    context = f.read()
context = context.lower()
lists = context.split(" ")
lists.sort()
print(lists)
ans = []
i =0
while(i<len(lists)-1):
    j = 0
    result = {}
    while(lists[i] == lists[i+j]):
        j+=1
        if(i+j == len(lists)-1):break
    result[lists[i]] =j
    ans.append(result)
    i = i+j
if(lists[i-1] == lists[i]):
    ans[-1][lists[i]] +=1 
else:
    ans[-1][lists[i]] =1
print(ans)