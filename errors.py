import sys
number=(str(sys.argv[1]))
if number=="1":
    exit("error code x00000001")
elif number=="1-2":
    exit("error code x00000001-2")
elif number=="2":
    exit("error code x00000002")
elif number=="3":
    exit("error code x00000003")
else:
    exit("error code x00000000")