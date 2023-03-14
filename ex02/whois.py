import sys

try:
    assert len(sys.argv) == 2, "more than one argument are provided"
    assert not len(sys.argv) == 1
    int(sys.argv[1])

except AssertionError as msg:
    print(msg)
    sys.exit()
except:
    print("argument is not an integer")
    sys.exit()
num = int(sys.argv[1])
if num == 0:
    print("I'm Zero")
elif num % 2 == 0:
    print("I'm even")
else:
    print("I'm odd")
