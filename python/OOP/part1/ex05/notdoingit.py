#this is false due to floating point error based on how computer stored floating values.
#100 + 1.0/3 means that accuracy is only up to a certain limitations...
a = (100 + 1.0/3) - 100
b = 1.0/3
print (a)
print (b)
print (a == b)
