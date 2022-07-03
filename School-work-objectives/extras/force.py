class math():
    def __init__(self,*vars: float):
        self.force: float = vars[0]
        self.mass: float = vars[1]
        self.acceleration: float = vars[2]
        self.answer: float = 0
        self.search: str =""
    def calc(self):
        try:force=int(self.force)
        except:force="";_="force"
        try:mass=int(self.mass)
        except:mass="";_="mass"
        try:acceleration=int(self.acceleration)
        except:acceleration="";_="acceleration"
        try:self.search=_
        except:self.search=True
        if force=="":
            self.answer=mass*acceleration
        elif mass == "":
            self.answer=force/acceleration
        elif acceleration == "":
            self.answer=force/mass
        print((f"the {self.search} is {self.answer}")if self.search != True else "incorrct input")
vars=[]
types=["force","mass","acceleration"]
for x in types:
    vars.append(input(f"please input the {x} or nothing if thats the output you want\n"))
math(*[x for x in vars]).calc()