# print() experiments

# Default: go to next line after printing

print("Hello, ")
print("world!")

#Change the 'end' argument to do something other than add a newline ('\n') character
print("Hello, ", end="")
print("world!")

print("abc", end="---")
print("def")

print("abc", "def", "ghi")
print("abc", "def", "ghi", sep="->")

print("abc", "def", "ghi", sep=", and ", end="\n(\"list complete\")\n" )
