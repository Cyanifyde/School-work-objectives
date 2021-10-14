class size():
    def __init__(self,length,depth,height):
        self.length: float=length
        self.depth: float=depth
        self.height: float=height
        self.volume: float=length*depth*height/1000
def gather_inputs():
    variables.append(size(float(input("please input the length")),float(input("please input the depth")),float(input("please input the height"))))
    return variables
variables=[]
run_count=0
run=True
while run==True:
    gather_inputs()
    print(variables[run_count].volume)
    agree=input("would you like to do another volume?")
    if agree!="yes":
        run=False
    run_count+=1
for x in variables:
    print("volume no:",variables.index(x)+1,"was",x.volume)