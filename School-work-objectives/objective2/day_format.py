"""
Write a function called DayFormat that takes two parameters, the day as a number (e.g. Monday is 1, Tuesday is 2) and the output format required. The function should return the day formatted as shown:
E.g. DayFormat(2, "day") would return Tuesday.
"""


def day_format(inp, out):
    list1 = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
        "Sunday"
    ]
    list2 = ["M", "Tu", "W", "Th", "F", "Sa", "Su"]
    if out == "day":
        return list1[inp - 1]
    elif out == "shortday":
        return list1[inp - 1][:3]
    elif out == "char":
        return list2[inp - 1]
    else:
        return "Error"


print(
    day_format(int(input("please input the day as the number\n")),
               input("please input the output format required\n")))
