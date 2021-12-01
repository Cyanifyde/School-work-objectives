class Squares:
    def __init__(self, start, stop, numfrom, numto, type):
        self.start = start
        self.stop = stop
        self.numfrom = numfrom
        self.numto = numto
        self.type = type

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.stop:
            raise StopIteration
        else:
            if self.type == 1:
                multi = 2
            else:
                multi = 3
            res = self.start**multi
            self.start += 1
            if res >= self.numfrom and res <= self.numto:
                return res, self.start - 1


x = int(input("what number do you want to start from?"))
y = int(input("what number do you want to go to?"))
z = int(input("please input the number correlating\n1--squared\n2--cubed\n"))
p = Squares(x, y, x, y, z)
for i in p:
    if not i == None:
        if p.type == 1:
            v = "squared"
        else:
            v = "cubed"
        print(str(i[1]), v, "is", str(i[0]))
