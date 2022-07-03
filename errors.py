import sys
#error handles... this way if there is anything that has to be done after an error it can be handled appropriately

number = (str(sys.argv[1]))
if number == "1":
    exit("error code x0000000"+number)
elif number == "1-2":
    exit("error code x0000000"+number)
elif number == "2":
    exit("error code x0000000"+number)
elif number == "3":
    exit("error code x0000000"+number)
elif number == "4":
    exit("error code x0000000"+number)
else:
    exit("error code x00000000")