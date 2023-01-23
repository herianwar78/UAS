#Function and recursive

def pangkat (x,y):
    if y == 0:
        return 1
    else:
        return x * pangkat (x,y-1)

x = int(input("masukkan nilai x : "))
y = int(input("masukkan nilai y : "))

print("%d dipangkatkan %d = %d" % (x,y,pangkat(x,y)))