import sys

try:
    assert not len(sys.argv) == 1, ""
    assert len(sys.argv) == 3, "Wrong number of arguments"
    
except AssertionError as msg:
    print (msg)
    sys.exit()
try:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
except ValueError:
    print("Nums must be integers")
    sys.exit()

print("sum:        ", num1 + num2)
print("Difference: ", num1 - num2)
print("Product:    ", num1 * num2)
if (num2) == 0:
    print("QuotError")
    print("Error")
    sys.exit()
else:
    print("Quotient:   ", num1 / num2)
    print("Remainder:  ", num1 % num2)
