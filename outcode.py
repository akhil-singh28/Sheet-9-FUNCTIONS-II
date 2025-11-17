name ="Suyash"
print(name)
def test():
    global name
    print(name)
    name ="Chaudhary"
    print(name)
test()
print(name)
# OUTPUT
# Suyash
# Suyash
# Chaudhary
# Chaudhary