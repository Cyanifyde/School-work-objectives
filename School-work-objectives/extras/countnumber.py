from random import randint
g=[]
p = {}
p2 = ["A","B","C","D"]
for x in range (365):
    c=randint(1,len(p2))
    g.append(c)
print(g)
for x in range (1,len(p2)+1):
    p.update({x:0})
print(p)
def add1(p,var):
    p.update({var: p[var]+1})
    return p
for x in g:
    p=add1(p,x)
print(p)
string=""
for x in range (len(p2)):
    string+=f"band {p2[x]}: {p[x+1]}\n"
print(string)