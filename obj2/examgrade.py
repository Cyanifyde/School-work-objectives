list1=[0,2,4,13,22,31,41,54,67,80,81]
list2=["u","1","2","3","4","5","6","7","8","9"]
def grade():
    a=int(input())
    num=0;found=None;not_found=True
    while not_found:
        if a>=list1[num] and a< list1[num+1]:
            print("found at",list1[num])
            found=num;not_found=False
        if a>80:not_found=False
        num+=1
    if not_found==False and not found==None:
        return list2[found],1
    else:
        return None,2

print(grade())

