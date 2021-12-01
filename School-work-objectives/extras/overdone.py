import time


class difference():
    def __init__(self, no1: float, no2: float):
        self.no1: float = no1
        self.no2: float = no2

    def max(self):
        if self.no1 > self.no2: return "no1"
        elif self.no1 < self.no2: return "no2"
        else: return "same size"


def gather_input(numbers):
    try:
        numbers.append(
            difference(float(input("please input no1")),
                       (float(input("please input no2")))))
    except:
        print("number not accepted")
        gather_input()
    return numbers


def main():
    numbers = []
    run_count = 0
    run = True
    while run == True:
        gather_input(numbers)
        run_count += 1
        x = input("would you like to do more numbers?")
        if not x == "yes": run = False
    for x in numbers:
        print("input",
              numbers.index(x) + 1, "have the numbers", x.no1, "and", x.no2,
              "\nthe one that is bigger is", x.max())
    time.sleep(10)


if __name__ == "__main__":
    main()
