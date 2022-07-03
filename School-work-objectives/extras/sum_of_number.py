class number():
    def __init__(self, stop):
        self.start: int = 1
        self.stop: int = stop + 1
        self.out: list = []
        self.sum: int = None

    def run(self):
        for x in range(self.start, self.stop):
            self.out.append(x)
        total = 0
        for x in self.out:
            total += x
        self.sum = total
        return self

    def output(self):
        list = self.out
        string = str(self.out[0])
        list.remove(int(string))
        for x in list:
            string += (f"+{str(x)}")
        string += f"={str(self.sum)}"
        return string


print(number(int(input("please input a number"))).run().output())