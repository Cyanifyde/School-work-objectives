"""
When keeping fish, one of the goals to reduce algae is to keep nitrates to a minimum. One way of doing this is to dose a carbon source which nitrifying bacteria within an aquarium consume together with nitrates. The carbon source must be dosed very precisely.
Write this function to determine and return the dose.
The program should output:
“For x nitrate dose y ml”
Where x is the parameter and y is the returned value.
"""

class dosage():
    def __init__(self, dose: float, ammount: float):
        self.dose: float= dose
        self.ammount: float= ammount
def gather_input():
    try:
        fish.append(dosage(float(input("please input the dosage")),0))
    except:
        gather_input()
def grade(run_count,dosage):
    num=0;found=None;not_found=True
    while not_found:
        if dosage>=list1[num] and dosage< list1[num+1]:
            found=num;not_found=False
        num+=1
    if not_found==False and not found==None:
        fish[run_count].ammount=list2[found]
    else:
        print("error")
        fish[run_count].ammount=None
fish=[]
list1=[0,1,2.5,10,100]
list2=[0.5,1,2,3]
run_count=0;run=True
while run==True:
    gather_input()
    try:
        grade(run_count,fish[run_count].dose)
    except:
        print("error")
        fish[run_count].dose=None
        fish[run_count].ammount=None
    run_count+=1
    x=input("would you like to do more dosages?")
    if not x=="yes":
        run=False
for x in fish:
    if not x.dose==None or not x.ammount==None:
        print("dosage no:",fish.index(x)+1,"with a nitrate of",x.dose,"needs",x.ammount,"ml")