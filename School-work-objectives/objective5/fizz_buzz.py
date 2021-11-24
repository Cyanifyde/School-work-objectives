"""
Write a subroutine that outputs the numbers from 1 to X. For the multiples of three output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
"""


def do(y):
    for x in range(1, y + 1):
        if (x % 3) == 0 and (x % 5) == 0:
            print("FizzBuzz")
        elif (x % 3) == 0:
            print("Fizz")
        elif (x % 5) == 0:
            print("Buzz")
        else:
            print(x)


do(int(input("please input a nuber to go to\n")))
